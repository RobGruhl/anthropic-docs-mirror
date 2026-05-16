#!/usr/bin/env python3
"""
Fetch MCP (Model Context Protocol) Blog Posts from blog.modelcontextprotocol.io

Features:
- HTTP conditional requests (ETag, If-Modified-Since) for efficient updates
- Async concurrent fetching with connection pooling
- CLI flags: --force, --dry-run, --concurrency
- HTML to markdown conversion

Directory structure:
  mcp-blog/
  ├── *.md
  └── mcp_blog_manifest.json
"""

import argparse
import asyncio
import aiohttp
import hashlib
import json
import logging
import sys
import os
import re
import xml.etree.ElementTree as ET
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Optional
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://blog.modelcontextprotocol.io"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
OUTPUT_DIR = Path(__file__).parent.parent / "mcp-blog"
MANIFEST_FILE = "mcp_blog_manifest.json"

HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

# Defaults
DEFAULT_CONCURRENCY = 5
MAX_RETRIES = 3

# Pattern to match blog post URLs: /posts/YYYY-MM-DD-slug
POST_URL_PATTERN = re.compile(r'/posts/(\d{4}-\d{2}-\d{2})-(.+)$')


def discover_blog_posts_sync() -> List[Dict]:
    """Discover all blog post URLs from sitemap (synchronous)."""
    import requests

    logger.info(f"Fetching sitemap: {SITEMAP_URL}")

    response = requests.get(SITEMAP_URL, headers=HEADERS, timeout=30)
    response.raise_for_status()

    try:
        parser = ET.XMLParser(forbid_dtd=True, forbid_entities=True, forbid_external=True)
        root = ET.fromstring(response.content, parser=parser)
    except TypeError:
        root = ET.fromstring(response.content)

    urls = []
    namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

    for url_elem in root.findall('.//ns:url', namespace):
        loc_elem = url_elem.find('ns:loc', namespace)
        if loc_elem is not None and loc_elem.text:
            urls.append(loc_elem.text)

    if not urls:
        for loc_elem in root.findall('.//loc'):
            if loc_elem.text:
                urls.append(loc_elem.text)

    logger.info(f"Found {len(urls)} total URLs in sitemap")

    pages = []
    seen_slugs = set()

    for url in urls:
        parsed = urlparse(url)
        path = parsed.path.rstrip('/')

        # Only process blog post URLs matching pattern
        match = POST_URL_PATTERN.match(path)
        if not match:
            continue

        date_str = match.group(1)
        slug = match.group(2)

        if slug in seen_slugs:
            continue
        seen_slugs.add(slug)

        filename = f"{date_str}-{slug}.md"

        pages.append({
            'url': url,
            'path': path,
            'date': date_str,
            'slug': slug,
            'filename': filename,
        })

    # Sort by date descending (newest first)
    pages.sort(key=lambda x: x['date'], reverse=True)

    logger.info(f"Discovered {len(pages)} blog posts")

    return pages


def html_to_markdown(html_content: str, url: str) -> tuple:
    """Convert HTML content to markdown format. Returns (markdown, title, date, summary)."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title = None
    title_elem = soup.find('h1')
    if title_elem:
        title = title_elem.get_text(strip=True)
    if not title:
        og_title = soup.find('meta', property='og:title')
        if og_title:
            title = og_title.get('content', '')

    # Extract date from meta or URL
    date = None
    # Try to find date in the page
    time_elem = soup.find('time')
    if time_elem:
        date = time_elem.get('datetime', '') or time_elem.get_text(strip=True)

    # Extract from URL if not found
    if not date:
        match = POST_URL_PATTERN.search(url)
        if match:
            date = match.group(1)

    # Extract summary/description
    summary = None
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        summary = meta_desc.get('content', '')
    if not summary:
        og_desc = soup.find('meta', property='og:description')
        if og_desc:
            summary = og_desc.get('content', '')

    # Extract main content - look for article or main content area
    content_parts = []

    # Try multiple selectors for main content
    article = soup.find('article')
    if not article:
        article = soup.find('main')
    if not article:
        article = soup.find('div', class_=re.compile(r'content|post|article', re.I))

    if article:
        # Remove navigation, header, footer elements
        for elem in article.find_all(['nav', 'header', 'footer', 'aside']):
            elem.decompose()

        for elem in article.find_all(['p', 'h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'pre', 'code', 'ol', 'ul', 'li', 'blockquote', 'table', 'tr', 'td', 'th']):
            text = elem.get_text(strip=True)
            if not text:
                continue

            # Skip if this is the title we already extracted
            if elem.name == 'h1' and title and text == title:
                continue

            if elem.name == 'h1':
                content_parts.append(f"\n# {text}\n")
            elif elem.name == 'h2':
                content_parts.append(f"\n## {text}\n")
            elif elem.name == 'h3':
                content_parts.append(f"\n### {text}\n")
            elif elem.name == 'h4':
                content_parts.append(f"\n#### {text}\n")
            elif elem.name == 'h5':
                content_parts.append(f"\n##### {text}\n")
            elif elem.name == 'h6':
                content_parts.append(f"\n###### {text}\n")
            elif elem.name in ['pre', 'code']:
                # Check if it's already inside a pre (code block)
                if elem.name == 'code' and elem.parent and elem.parent.name == 'pre':
                    continue
                content_parts.append(f"\n```\n{text}\n```\n")
            elif elem.name == 'blockquote':
                content_parts.append(f"\n> {text}\n")
            elif elem.name == 'li':
                # Check parent to determine bullet type
                parent = elem.parent
                if parent and parent.name == 'ol':
                    content_parts.append(f"1. {text}")
                else:
                    content_parts.append(f"- {text}")
            elif elem.name in ['table', 'tr', 'td', 'th']:
                # Skip table sub-elements, handle at table level
                if elem.name == 'table':
                    content_parts.append(f"\n{text}\n")
            else:
                content_parts.append(text)

    content = '\n\n'.join(content_parts)

    # Build markdown
    md_parts = [
        f"# {title or 'Untitled'}",
        "",
    ]

    if date:
        md_parts.extend([f"*{date}*", ""])

    md_parts.extend(["---", ""])

    if summary:
        md_parts.extend([f"**Summary:** {summary}", ""])

    md_parts.extend([
        content,
        "",
        "---",
        "",
        f"**Source:** {url}",
        "",
        "*This is a mirror of the MCP blog for offline reading. All content is copyright the Model Context Protocol project.*",
    ])

    return '\n'.join(md_parts), title, date, summary


def load_manifest() -> Dict:
    """Load existing manifest if it exists."""
    manifest_path = OUTPUT_DIR / MANIFEST_FILE
    if manifest_path.exists():
        try:
            return json.loads(manifest_path.read_text())
        except Exception as e:
            logger.warning(f"Failed to load manifest: {e}")
    return {"files": {}}


def save_manifest(manifest: Dict) -> None:
    """Save manifest to file."""
    manifest_path = OUTPUT_DIR / MANIFEST_FILE

    github_repo = os.environ.get('GITHUB_REPOSITORY', 'robgruhl/anthropic-docs-mirror')
    github_ref = os.environ.get('GITHUB_REF_NAME', 'main')

    if not re.match(r'^[\w.-]+/[\w.-]+$', github_repo):
        github_repo = 'robgruhl/anthropic-docs-mirror'
    if not re.match(r'^[\w.-]+$', github_ref):
        github_ref = 'main'

    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/mcp-blog/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["source_site"] = "blog.modelcontextprotocol.io"
    manifest["last_updated"] = datetime.now().isoformat()

    manifest_path.write_text(json.dumps(manifest, indent=2))


async def fetch_post(
    session: aiohttp.ClientSession,
    page: Dict,
    old_entry: Dict,
    force: bool,
    semaphore: asyncio.Semaphore
) -> Dict:
    """Fetch a single blog post with conditional request support."""
    headers = dict(HEADERS)

    if not force:
        if old_entry.get('etag'):
            headers['If-None-Match'] = old_entry['etag']
        if old_entry.get('last_modified'):
            headers['If-Modified-Since'] = old_entry['last_modified']

    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                async with session.get(
                    page['url'],
                    headers=headers,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:

                    if response.status == 304:
                        return {
                            'status': 304,
                            'content': None,
                            'etag': old_entry.get('etag'),
                            'last_modified': old_entry.get('last_modified'),
                            'hash': old_entry.get('hash'),
                            'title': old_entry.get('title'),
                            'page': page,
                            'old_entry': old_entry,
                        }

                    if response.status == 200:
                        html_content = await response.text()

                        # Convert HTML to markdown
                        markdown, title, date, summary = html_to_markdown(html_content, page['url'])

                        content_hash = hashlib.sha256(markdown.encode('utf-8')).hexdigest()

                        return {
                            'status': 200,
                            'content': markdown,
                            'etag': response.headers.get('ETag'),
                            'last_modified': response.headers.get('Last-Modified'),
                            'hash': content_hash,
                            'title': title,
                            'date': date,
                            'summary': summary,
                            'page': page,
                            'old_entry': old_entry,
                        }

                    if response.status == 429:
                        wait = int(response.headers.get('Retry-After', 60))
                        logger.warning(f"Rate limited, waiting {wait}s...")
                        await asyncio.sleep(wait)
                        continue

                    return {'status': response.status, 'error': f'HTTP {response.status}', 'page': page, 'old_entry': old_entry}

            except asyncio.TimeoutError:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                return {'status': -1, 'error': 'Timeout', 'page': page, 'old_entry': old_entry}
            except aiohttp.ClientError as e:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                return {'status': -1, 'error': str(e), 'page': page, 'old_entry': old_entry}

    return {'status': -1, 'error': 'Max retries exceeded', 'page': page, 'old_entry': old_entry}


async def fetch_all_posts(
    pages: List[Dict],
    old_manifest: Dict,
    force: bool,
    concurrency: int,
    dry_run: bool
) -> Dict:
    """Fetch all posts concurrently."""

    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency)

    stats = {
        'successful': 0, 'failed': 0, 'unchanged': 0,
        'updated': 0, 'new': 0, 'skipped_304': 0
    }
    failed_pages = []
    new_manifest = {"files": {}}
    current_files = set()

    if dry_run:
        logger.info("DRY RUN - checking what would be fetched...")
        for page in pages:
            old_entry = old_manifest.get("files", {}).get(page['filename'], {})
            if old_entry.get('etag') or old_entry.get('last_modified'):
                logger.info(f"  Would check: {page['filename']} (has cache headers)")
            else:
                logger.info(f"  Would fetch: {page['filename']} (no cache)")
        return stats, failed_pages, old_manifest, set(old_manifest.get("files", {}).keys())

    async with aiohttp.ClientSession(connector=connector) as session:
        # Create all fetch tasks
        tasks = [
            fetch_post(session, page, old_manifest.get("files", {}).get(page['filename'], {}), force, semaphore)
            for page in pages
        ]

        total = len(tasks)
        logger.info(f"Fetching {total} posts concurrently (max {concurrency} at a time)...")

        # Run all tasks concurrently with asyncio.gather
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results
        for i, result in enumerate(results, 1):
            # Handle exceptions from gather
            if isinstance(result, Exception):
                stats['failed'] += 1
                failed_pages.append(pages[i-1]['slug'])
                logger.warning(f"Failed: {pages[i-1]['filename']} - {str(result)}")
                continue

            page = result['page']
            old_entry = result['old_entry']

            if result['status'] == 304:
                stats['skipped_304'] += 1
                stats['unchanged'] += 1
                stats['successful'] += 1
                current_files.add(page['filename'])
                new_manifest["files"][page['filename']] = old_entry.copy()

            elif result['status'] == 200:
                content = result['content']
                old_hash = old_entry.get('hash', '')

                if old_hash == result['hash']:
                    stats['unchanged'] += 1
                    last_updated = old_entry.get('last_updated', datetime.now().isoformat())
                else:
                    if old_hash:
                        stats['updated'] += 1
                    else:
                        stats['new'] += 1
                    last_updated = datetime.now().isoformat()

                file_path = OUTPUT_DIR / page['filename']
                file_path.write_text(content, encoding='utf-8')

                new_manifest["files"][page['filename']] = {
                    "original_url": page['url'],
                    "title": result.get('title', ''),
                    "date": result.get('date', page['date']),
                    "summary": result.get('summary', ''),
                    "slug": page['slug'],
                    "hash": result['hash'],
                    "etag": result.get('etag'),
                    "last_modified": result.get('last_modified'),
                    "last_updated": last_updated
                }

                current_files.add(page['filename'])
                stats['successful'] += 1

            else:
                stats['failed'] += 1
                failed_pages.append(page['slug'])
                logger.warning(f"Failed: {page['filename']} - {result.get('error', 'Unknown error')}")

        logger.info(f"Completed: {stats['successful']} successful, {stats['failed']} failed ({stats['skipped_304']} cached, {stats['updated']} updated, {stats['new']} new)")

    return stats, failed_pages, new_manifest, current_files


def cleanup_old_files(current_files: Set[str], old_manifest: Dict) -> None:
    """Remove files that no longer exist in the source."""
    old_files = set(old_manifest.get("files", {}).keys())
    files_to_remove = old_files - current_files

    for filename in files_to_remove:
        if filename == MANIFEST_FILE:
            continue
        file_path = OUTPUT_DIR / filename
        if file_path.exists():
            logger.info(f"Removing obsolete file: {filename}")
            file_path.unlink()


def main():
    """Main fetcher function."""
    parser = argparse.ArgumentParser(
        description='Fetch MCP blog posts from blog.modelcontextprotocol.io'
    )
    parser.add_argument(
        '--force', action='store_true',
        help='Force full re-fetch, ignoring cache headers'
    )
    parser.add_argument(
        '--dry-run', action='store_true',
        help='Show what would be fetched without downloading'
    )
    parser.add_argument(
        '--concurrency', type=int, default=DEFAULT_CONCURRENCY,
        help=f'Max concurrent requests (default: {DEFAULT_CONCURRENCY})'
    )
    parser.add_argument(
        '--skip-indexes', action='store_true',
        help='Skip index regeneration (for parallel fetching)'
    )
    args = parser.parse_args()

    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("Starting MCP blog fetch (blog.modelcontextprotocol.io)")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'FORCE' if args.force else 'INCREMENTAL'}")
    logger.info(f"Concurrency: {args.concurrency}")
    logger.info("=" * 60)

    OUTPUT_DIR.mkdir(parents=True, exist_ok=True)

    old_manifest = load_manifest()
    cached_count = sum(1 for f in old_manifest.get("files", {}).values() if f.get('etag') or f.get('last_modified'))
    logger.info(f"Existing manifest: {len(old_manifest.get('files', {}))} files ({cached_count} with cache headers)")

    try:
        pages = discover_blog_posts_sync()
    except Exception as e:
        logger.error(f"Failed to discover pages: {e}")
        sys.exit(1)

    if not pages:
        logger.warning("No blog posts discovered - this may be expected if the blog is empty")
        # Don't exit with error - just save empty manifest
        new_manifest = {"files": {}}
        new_manifest["fetch_metadata"] = {
            "last_fetch_completed": datetime.now().isoformat(),
            "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
            "total_posts_discovered": 0,
            "posts_fetched_successfully": 0,
            "source_sitemap": SITEMAP_URL,
            "fetch_tool_version": "5.0",
            "fetch_mode": "force" if args.force else "incremental"
        }
        save_manifest(new_manifest)
        return 0

    stats, failed_pages, new_manifest, current_files = asyncio.run(
        fetch_all_posts(pages, old_manifest, args.force, args.concurrency, args.dry_run)
    )

    if args.dry_run:
        logger.info("\nDry run complete - no files were modified")
        return 0

    cleanup_old_files(current_files, old_manifest)

    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
        "total_posts_discovered": len(pages),
        "posts_fetched_successfully": stats['successful'],
        "posts_failed": stats['failed'],
        "posts_unchanged": stats['unchanged'],
        "posts_updated": stats['updated'],
        "posts_new": stats['new'],
        "posts_skipped_304": stats['skipped_304'],
        "failed_posts": failed_pages,
        "source_sitemap": SITEMAP_URL,
        "fetch_tool_version": "5.0",
        "fetch_mode": "force" if args.force else "incremental"
    }

    save_manifest(new_manifest)

    duration = datetime.now() - start_time
    logger.info("\n" + "=" * 60)
    logger.info(f"Fetch completed in {duration}")
    logger.info(f"Total posts discovered: {len(pages)}")
    logger.info(f"Successful: {stats['successful']}")
    logger.info(f"  - Skipped (304): {stats['skipped_304']}")
    logger.info(f"  - New: {stats['new']}")
    logger.info(f"  - Updated: {stats['updated']}")
    logger.info(f"  - Unchanged: {stats['unchanged']}")
    logger.info(f"Failed: {stats['failed']}")

    if failed_pages:
        logger.warning("\nFailed posts:")
        for page in failed_pages[:10]:
            logger.warning(f"  - {page}")
        if len(failed_pages) > 10:
            logger.warning(f"  ... and {len(failed_pages) - 10} more")

    # Auto-regenerate indexes (unless skipped for parallel fetching)
    if not args.skip_indexes:
        logger.info("\n" + "=" * 60)
        logger.info("Regenerating indexes...")
        try:
            import subprocess
            scripts_dir = Path(__file__).parent
            result = subprocess.run(
                [sys.executable, str(scripts_dir / 'generate_indexes.py')],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                logger.info("Indexes regenerated successfully")
            else:
                logger.warning(f"Index generation had issues: {result.stderr}")
        except Exception as e:
            logger.warning(f"Failed to regenerate indexes: {e}")
    else:
        logger.info("\nSkipping index regeneration (--skip-indexes)")

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
