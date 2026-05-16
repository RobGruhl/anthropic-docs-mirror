#!/usr/bin/env python3
"""
Fetch documentation from platform.claude.com - the canonical source for Claude developer docs.

Features:
- HTTP conditional requests (ETag, If-Modified-Since) for efficient updates
- Async concurrent fetching with connection pooling
- CLI flags: --force, --dry-run, --concurrency

Directory structure:
  platform-docs/
  ├── developer-guide/   # Main docs (models, features, tools, agents, etc.)
  ├── api-reference/     # API endpoints
  ├── resources/         # Prompt library, use cases, glossary
  └── platform_manifest.json
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
BASE_URL = "https://platform.claude.com"
SITEMAP_URL = f"{BASE_URL}/sitemap.xml"
OUTPUT_DIR = Path(__file__).parent.parent / "platform-docs"
MANIFEST_FILE = "platform_manifest.json"

HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/markdown, text/plain, */*',
}

# Defaults
DEFAULT_CONCURRENCY = 10
MAX_RETRIES = 3

# Pages to skip - navigation/index pages with no substantive content
SKIP_PATHS = {
    '/docs/en/about-claude/use-case-guides/overview',
    '/docs/en/resources/overview',
    '/docs/en/resources/prompt-library/library',
}


def categorize_url(path: str) -> str:
    """Categorize URL path into api-reference, resources, or developer-guide."""
    if '/api/' in path:
        return 'api-reference'
    elif '/resources/' in path:
        return 'resources'
    return 'developer-guide'


def url_to_filename(path: str) -> str:
    """Convert URL path to safe filename."""
    if '/docs/en/' in path:
        path = path.split('/docs/en/')[-1]
    elif '/docs/' in path:
        path = path.split('/docs/')[-1]

    category = categorize_url(f"/docs/en/{path}")
    if category == 'api-reference' and path.startswith('api/'):
        path = path[4:]
    elif category == 'resources' and path.startswith('resources/'):
        path = path[10:]

    if not path or path == '/':
        path = 'index'

    path = path.rstrip('/')
    filename = path.replace('/', '__')

    if not filename.endswith('.md'):
        filename += '.md'

    return filename


def discover_pages_sync() -> List[Dict]:
    """Discover all English documentation pages from sitemap (synchronous)."""
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
    seen_paths = set()

    for url in urls:
        if '/docs/en/' not in url:
            continue

        parsed = urlparse(url)
        path = parsed.path.rstrip('/')

        if path in seen_paths:
            continue
        seen_paths.add(path)

        if path in SKIP_PATHS:
            continue

        category = categorize_url(path)
        filename = url_to_filename(path)

        pages.append({
            'url': url,
            'path': path,
            'category': category,
            'filename': filename,
            'md_url': f"{BASE_URL}{path}.md"
        })

    pages.sort(key=lambda x: (x['category'], x['path']))

    categories = {}
    for page in pages:
        cat = page['category']
        categories[cat] = categories.get(cat, 0) + 1

    logger.info(f"Discovered {len(pages)} English documentation pages:")
    for cat, count in sorted(categories.items()):
        logger.info(f"  - {cat}: {count}")

    return pages


def validate_markdown(content: str) -> bool:
    """Validate that content appears to be markdown."""
    if not content or len(content.strip()) < 50:
        return False
    if content.strip().startswith('<!DOCTYPE') or '<html' in content[:200]:
        return False

    indicators = ['# ', '## ', '### ', '```', '- ', '* ', '1. ', '[', '**', '_', '> ']
    count = sum(1 for line in content.split('\n')[:50] for ind in indicators if ind in line)
    return count >= 3


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

    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/platform-docs/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["source_site"] = "platform.claude.com"
    manifest["last_updated"] = datetime.now().isoformat()

    manifest_path.write_text(json.dumps(manifest, indent=2))


async def fetch_page(
    session: aiohttp.ClientSession,
    page: Dict,
    old_entry: Dict,
    force: bool,
    semaphore: asyncio.Semaphore
) -> Dict:
    """
    Fetch a single page with conditional request support.
    Returns dict with status, content, cache headers, and page/old_entry for correlation.
    """
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
                    page['md_url'],
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
                            'page': page,
                            'old_entry': old_entry,
                        }

                    if response.status == 200:
                        content = await response.text()

                        if not validate_markdown(content):
                            return {'status': -1, 'error': 'Invalid markdown', 'page': page, 'old_entry': old_entry}

                        # Add source footer
                        footer = f"\n\n---\n📖 **Source:** {page['url']}\n*Mirrored from platform.claude.com for local access.*\n"
                        content = content + footer

                        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

                        return {
                            'status': 200,
                            'content': content,
                            'etag': response.headers.get('ETag'),
                            'last_modified': response.headers.get('Last-Modified'),
                            'hash': content_hash,
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


async def fetch_all_pages(
    pages: List[Dict],
    old_manifest: Dict,
    force: bool,
    concurrency: int,
    dry_run: bool
) -> Dict:
    """Fetch all pages concurrently."""

    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency)

    stats = {
        'successful': 0, 'failed': 0, 'unchanged': 0,
        'updated': 0, 'new': 0, 'skipped_304': 0,
        'by_category': {'developer-guide': 0, 'api-reference': 0, 'resources': 0}
    }
    failed_pages = []
    new_manifest = {"files": {}}
    current_files = set()

    if dry_run:
        logger.info("DRY RUN - checking what would be fetched...")
        # In dry run, just do HEAD requests to check Last-Modified
        async with aiohttp.ClientSession(connector=connector) as session:
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
            fetch_page(session, page, old_manifest.get("files", {}).get(page['filename'], {}), force, semaphore)
            for page in pages
        ]

        total = len(tasks)
        logger.info(f"Fetching {total} pages concurrently (max {concurrency} at a time)...")

        # Run all tasks concurrently with asyncio.gather
        results = await asyncio.gather(*tasks, return_exceptions=True)

        # Process results
        for i, result in enumerate(results, 1):
            # Handle exceptions from gather
            if isinstance(result, Exception):
                stats['failed'] += 1
                failed_pages.append(pages[i-1]['path'])
                logger.warning(f"Failed: {pages[i-1]['filename']} - {str(result)}")
                continue

            page = result['page']
            old_entry = result['old_entry']

            if result['status'] == 304:
                # Unchanged - use existing data
                stats['skipped_304'] += 1
                stats['unchanged'] += 1
                stats['successful'] += 1
                stats['by_category'][page['category']] += 1
                current_files.add(page['filename'])

                # Preserve existing manifest entry
                new_manifest["files"][page['filename']] = old_entry.copy()

            elif result['status'] == 200:
                content = result['content']

                # Check if content actually changed
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

                # Save file
                file_path = OUTPUT_DIR / page['category'] / page['filename']
                file_path.write_text(content, encoding='utf-8')

                # Update manifest with cache headers
                new_manifest["files"][page['filename']] = {
                    "original_url": page['url'],
                    "original_md_url": page['md_url'],
                    "category": page['category'],
                    "path": page['path'],
                    "hash": result['hash'],
                    "etag": result.get('etag'),
                    "last_modified": result.get('last_modified'),
                    "last_updated": last_updated
                }

                current_files.add(page['filename'])
                stats['successful'] += 1
                stats['by_category'][page['category']] += 1

            else:
                stats['failed'] += 1
                failed_pages.append(page['path'])
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
        for category in ['developer-guide', 'api-reference', 'resources']:
            file_path = OUTPUT_DIR / category / filename
            if file_path.exists():
                logger.info(f"Removing obsolete file: {category}/{filename}")
                file_path.unlink()


def main():
    """Main fetcher function."""
    parser = argparse.ArgumentParser(
        description='Fetch platform.claude.com documentation efficiently'
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
    logger.info("Starting platform.claude.com documentation fetch")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'FORCE' if args.force else 'INCREMENTAL'}")
    logger.info(f"Concurrency: {args.concurrency}")
    logger.info("=" * 60)

    # Create output directory structure
    OUTPUT_DIR.mkdir(exist_ok=True)
    for category in ['developer-guide', 'api-reference', 'resources']:
        (OUTPUT_DIR / category).mkdir(exist_ok=True)

    # Load existing manifest
    old_manifest = load_manifest()
    cached_count = sum(1 for f in old_manifest.get("files", {}).values() if f.get('etag') or f.get('last_modified'))
    logger.info(f"Existing manifest: {len(old_manifest.get('files', {}))} files ({cached_count} with cache headers)")

    # Discover pages
    try:
        pages = discover_pages_sync()
    except Exception as e:
        logger.error(f"Failed to discover pages: {e}")
        sys.exit(1)

    if not pages:
        logger.error("No documentation pages discovered!")
        sys.exit(1)

    # Fetch all pages
    stats, failed_pages, new_manifest, current_files = asyncio.run(
        fetch_all_pages(pages, old_manifest, args.force, args.concurrency, args.dry_run)
    )

    if args.dry_run:
        logger.info("\nDry run complete - no files were modified")
        return 0

    # Clean up old files
    cleanup_old_files(current_files, old_manifest)

    # Add fetch metadata
    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
        "total_pages_discovered": len(pages),
        "pages_fetched_successfully": stats['successful'],
        "pages_failed": stats['failed'],
        "pages_unchanged": stats['unchanged'],
        "pages_updated": stats['updated'],
        "pages_new": stats['new'],
        "pages_skipped_304": stats['skipped_304'],
        "failed_pages": failed_pages,
        "by_category": stats['by_category'],
        "source_sitemap": SITEMAP_URL,
        "fetch_tool_version": "5.0",
        "fetch_mode": "force" if args.force else "incremental"
    }

    # Save manifest
    save_manifest(new_manifest)

    # Summary
    duration = datetime.now() - start_time
    logger.info("\n" + "=" * 60)
    logger.info(f"Fetch completed in {duration}")
    logger.info(f"Total pages discovered: {len(pages)}")
    logger.info(f"Successful: {stats['successful']}")
    logger.info(f"  - Skipped (304): {stats['skipped_304']}")
    logger.info(f"  - New: {stats['new']}")
    logger.info(f"  - Updated: {stats['updated']}")
    logger.info(f"  - Unchanged: {stats['unchanged']}")
    logger.info(f"Failed: {stats['failed']}")
    logger.info(f"\nBy category:")
    for cat, count in stats['by_category'].items():
        logger.info(f"  - {cat}: {count}")

    if failed_pages:
        logger.warning("\nFailed pages:")
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

    if stats['successful'] == 0:
        logger.error("No pages were fetched successfully!")
        sys.exit(1)

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
