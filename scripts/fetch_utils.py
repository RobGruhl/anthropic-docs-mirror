#!/usr/bin/env python3
"""
Shared utilities for efficient documentation fetching.

Features:
- HTTP conditional requests (ETag, If-Modified-Since) for 304 responses
- Async concurrent fetching with connection pooling
- Rate limiting via semaphores
- Retry logic with exponential backoff
"""

import asyncio
import aiohttp
import hashlib
import logging
import random
from typing import Dict, Optional, Tuple, Any, List
from dataclasses import dataclass

logger = logging.getLogger(__name__)

# Default headers
DEFAULT_HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/markdown, text/plain, */*',
}

# Rate limiting defaults
DEFAULT_CONCURRENCY = 10
DEFAULT_RETRY_ATTEMPTS = 3
DEFAULT_RETRY_DELAY = 1.0
MAX_RETRY_DELAY = 30.0


@dataclass
class FetchResult:
    """Result of a fetch operation."""
    url: str
    status: int
    content: Optional[str] = None
    etag: Optional[str] = None
    last_modified: Optional[str] = None
    content_hash: Optional[str] = None
    error: Optional[str] = None

    @property
    def is_unchanged(self) -> bool:
        return self.status == 304

    @property
    def is_success(self) -> bool:
        return self.status in (200, 304)

    @property
    def is_not_found(self) -> bool:
        return self.status == 404


async def fetch_with_conditional(
    session: aiohttp.ClientSession,
    url: str,
    etag: Optional[str] = None,
    last_modified: Optional[str] = None,
    force: bool = False,
    timeout: int = 30,
) -> FetchResult:
    """
    Fetch a URL with HTTP conditional request headers.

    If etag or last_modified is provided (and force=False), sends conditional
    headers. Server returns 304 if content unchanged, saving bandwidth.

    Args:
        session: aiohttp session
        url: URL to fetch
        etag: Previous ETag value from manifest
        last_modified: Previous Last-Modified value from manifest
        force: If True, bypass conditional headers
        timeout: Request timeout in seconds

    Returns:
        FetchResult with status, content (if changed), and new headers
    """
    headers = dict(DEFAULT_HEADERS)

    if not force:
        if etag:
            headers['If-None-Match'] = etag
        if last_modified:
            headers['If-Modified-Since'] = last_modified

    try:
        async with session.get(url, headers=headers, timeout=aiohttp.ClientTimeout(total=timeout)) as response:
            new_etag = response.headers.get('ETag')
            new_last_modified = response.headers.get('Last-Modified')

            if response.status == 304:
                return FetchResult(
                    url=url,
                    status=304,
                    etag=etag,  # Keep existing
                    last_modified=last_modified,
                )

            if response.status == 200:
                content = await response.text()
                content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
                return FetchResult(
                    url=url,
                    status=200,
                    content=content,
                    etag=new_etag,
                    last_modified=new_last_modified,
                    content_hash=content_hash,
                )

            return FetchResult(
                url=url,
                status=response.status,
                error=f"HTTP {response.status}",
            )

    except asyncio.TimeoutError:
        return FetchResult(url=url, status=0, error="Timeout")
    except aiohttp.ClientError as e:
        return FetchResult(url=url, status=0, error=str(e))


async def fetch_with_retry(
    session: aiohttp.ClientSession,
    url: str,
    etag: Optional[str] = None,
    last_modified: Optional[str] = None,
    force: bool = False,
    max_retries: int = DEFAULT_RETRY_ATTEMPTS,
    semaphore: Optional[asyncio.Semaphore] = None,
) -> FetchResult:
    """
    Fetch with retry logic and rate limiting.

    Args:
        session: aiohttp session
        url: URL to fetch
        etag: Previous ETag for conditional request
        last_modified: Previous Last-Modified for conditional request
        force: Bypass conditional headers
        max_retries: Maximum retry attempts
        semaphore: Rate limiting semaphore

    Returns:
        FetchResult
    """
    async def _fetch():
        for attempt in range(max_retries):
            result = await fetch_with_conditional(
                session, url, etag, last_modified, force
            )

            if result.is_success or result.is_not_found:
                return result

            if attempt < max_retries - 1:
                delay = min(DEFAULT_RETRY_DELAY * (2 ** attempt), MAX_RETRY_DELAY)
                delay *= random.uniform(0.5, 1.5)  # Jitter
                logger.debug(f"Retry {attempt + 1}/{max_retries} for {url} after {delay:.1f}s")
                await asyncio.sleep(delay)

        return result

    if semaphore:
        async with semaphore:
            return await _fetch()
    return await _fetch()


async def fetch_batch(
    urls_with_cache: List[Tuple[str, Optional[str], Optional[str]]],
    concurrency: int = DEFAULT_CONCURRENCY,
    force: bool = False,
    progress_callback: Optional[callable] = None,
) -> List[FetchResult]:
    """
    Fetch multiple URLs concurrently with connection pooling.

    Args:
        urls_with_cache: List of (url, etag, last_modified) tuples
        concurrency: Maximum concurrent requests
        force: Bypass conditional headers for all requests
        progress_callback: Optional callback(completed, total) for progress

    Returns:
        List of FetchResult in same order as input
    """
    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency)

    results = []
    completed = 0
    total = len(urls_with_cache)

    async with aiohttp.ClientSession(connector=connector) as session:
        async def fetch_one(url: str, etag: Optional[str], last_modified: Optional[str]) -> FetchResult:
            nonlocal completed
            result = await fetch_with_retry(
                session, url, etag, last_modified, force, semaphore=semaphore
            )
            completed += 1
            if progress_callback:
                progress_callback(completed, total)
            return result

        tasks = [
            fetch_one(url, etag, last_modified)
            for url, etag, last_modified in urls_with_cache
        ]
        results = await asyncio.gather(*tasks)

    return results


def validate_markdown(content: str, min_length: int = 50) -> bool:
    """
    Validate that content appears to be markdown.

    Args:
        content: Content to validate
        min_length: Minimum content length

    Returns:
        True if content looks like valid markdown
    """
    if not content or len(content.strip()) < min_length:
        return False

    # Check for HTML instead of markdown
    if content.strip().startswith('<!DOCTYPE') or '<html' in content[:200]:
        return False

    # Check for markdown indicators
    markdown_indicators = ['# ', '## ', '### ', '```', '- ', '* ', '1. ', '[', '**', '_', '> ']
    indicator_count = sum(
        1 for line in content.split('\n')[:50]
        for ind in markdown_indicators
        if ind in line
    )

    return indicator_count >= 3


def get_manifest_cache_info(manifest: Dict, filename: str) -> Tuple[Optional[str], Optional[str]]:
    """
    Extract ETag and Last-Modified from manifest for a file.

    Args:
        manifest: Loaded manifest dict
        filename: File to look up

    Returns:
        (etag, last_modified) tuple, either may be None
    """
    entry = manifest.get('files', {}).get(filename, {})
    return entry.get('etag'), entry.get('last_modified')
