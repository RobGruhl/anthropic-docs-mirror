#!/usr/bin/env python3
"""
Fetch documentation from code.claude.com - official Claude Code documentation.

Features:
- HTTP conditional requests (ETag, If-Modified-Since) for efficient updates
- Async concurrent fetching with connection pooling
- CLI flags: --force, --dry-run, --concurrency
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
BASE_URL = "https://code.claude.com"
SITEMAP_URL = f"{BASE_URL}/docs/sitemap.xml"
OUTPUT_DIR = Path(__file__).parent.parent / "code-claude-docs"
MANIFEST_FILE = "code_claude_manifest.json"

HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/markdown, text/plain, */*',
}

# Defaults
DEFAULT_CONCURRENCY = 10
MAX_RETRIES = 3


def url_to_filename(path: str) -> str:
    """Convert URL path to safe filename."""
    # Remove /docs/en/ prefix
    if '/docs/en/' in path:
        path = path.split('/docs/en/')[-1]
    elif '/docs/' in path:
        path = path.split('/docs/')[-1]

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
        # Only include English docs
        if '/docs/en/' not in url:
            continue

        parsed = urlparse(url)
        path = parsed.path.rstrip('/')

        if path in seen_paths:
            continue
        seen_paths.add(path)

        filename = url_to_filename(path)

        pages.append({
            'url': url,
            'path': path,
            'filename': filename,
            'md_url': f"{BASE_URL}{path}.md"
        })

    pages.sort(key=lambda x: x['path'])
    logger.info(f"Discovered {len(pages)} English documentation pages")

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

    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/code-claude-docs/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["source_site"] = "code.claude.com"
    manifest["last_updated"] = datetime.now().isoformat()

    manifest_path.write_text(json.dumps(manifest, indent=2))


async def fetch_page(
    session: aiohttp.ClientSession,
    page: Dict,
    old_entry: Dict,
    force: bool,
    semaphore: asyncio.Semaphore
) -> Dict:
    """Fetch a single page with conditional request support."""
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
                        }

                    if response.status == 200:
                        content = await response.text()

                        if not validate_markdown(content):
                            return {'status': -1, 'error': 'Invalid markdown'}

                        # Add source footer
                        footer = f"\n\n---\n**Source:** {page['url']}\n*Mirrored from code.claude.com for local access.*\n"
                        content = content + footer

                        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

                        return {
                            'status': 200,
                            'content': content,
                            'etag': response.headers.get('ETag'),
                            'last_modified': response.headers.get('Last-Modified'),
                            'hash': content_hash,
                        }

                    if response.status == 429:
                        wait = int(response.headers.get('Retry-After', 60))
                        logger.warning(f"Rate limited, waiting {wait}s...")
                        await asyncio.sleep(wait)
                        continue

                    return {'status': response.status, 'error': f'HTTP {response.status}'}

            except asyncio.TimeoutError:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                return {'status': -1, 'error': 'Timeout'}
            except aiohttp.ClientError as e:
                if attempt < MAX_RETRIES - 1:
                    await asyncio.sleep(2 ** attempt)
                    continue
                return {'status': -1, 'error': str(e)}

    return {'status': -1, 'error': 'Max retries exceeded'}


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
        'updated': 0, 'new': 0, 'skipped_304': 0
    }
    failed_pages = []
    new_manifest = {"files": {}}
    current_files = set()

    if dry_run:
        logger.info("DRY RUN - checking what would be fetched...")
        async with aiohttp.ClientSession(connector=connector) as session:
            for page in pages:
                old_entry = old_manifest.get("files", {}).get(page['filename'], {})
                if old_entry.get('etag') or old_entry.get('last_modified'):
                    logger.info(f"  Would check: {page['filename']} (has cache headers)")
                else:
                    logger.info(f"  Would fetch: {page['filename']} (no cache)")
        return stats, failed_pages, old_manifest, set(old_manifest.get("files", {}).keys())

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for page in pages:
            old_entry = old_manifest.get("files", {}).get(page['filename'], {})
            task = fetch_page(session, page, old_entry, force, semaphore)
            tasks.append((page, old_entry, task))

        total = len(tasks)
        for i, (page, old_entry, task) in enumerate(tasks, 1):
            result = await task

            if i % 20 == 0 or i == total:
                logger.info(f"Progress: {i}/{total} ({stats['skipped_304']} cached, {stats['updated']} updated)")

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
                    "original_md_url": page['md_url'],
                    "hash": result['hash'],
                    "etag": result.get('etag'),
                    "last_modified": result.get('last_modified'),
                    "last_updated": last_updated
                }

                current_files.add(page['filename'])
                stats['successful'] += 1

            else:
                stats['failed'] += 1
                failed_pages.append(page['path'])
                logger.warning(f"Failed: {page['filename']} - {result.get('error', 'Unknown error')}")

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
        description='Fetch code.claude.com documentation efficiently'
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
    logger.info("Starting code.claude.com documentation fetch")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'FORCE' if args.force else 'INCREMENTAL'}")
    logger.info(f"Concurrency: {args.concurrency}")
    logger.info("=" * 60)

    OUTPUT_DIR.mkdir(exist_ok=True)

    old_manifest = load_manifest()
    cached_count = sum(1 for f in old_manifest.get("files", {}).values() if f.get('etag') or f.get('last_modified'))
    logger.info(f"Existing manifest: {len(old_manifest.get('files', {}))} files ({cached_count} with cache headers)")

    try:
        pages = discover_pages_sync()
    except Exception as e:
        logger.error(f"Failed to discover pages: {e}")
        sys.exit(1)

    if not pages:
        logger.error("No documentation pages discovered!")
        sys.exit(1)

    stats, failed_pages, new_manifest, current_files = asyncio.run(
        fetch_all_pages(pages, old_manifest, args.force, args.concurrency, args.dry_run)
    )

    if args.dry_run:
        logger.info("\nDry run complete - no files were modified")
        return 0

    cleanup_old_files(current_files, old_manifest)

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
        "source_sitemap": SITEMAP_URL,
        "fetch_tool_version": "5.0",
        "fetch_mode": "force" if args.force else "incremental"
    }

    save_manifest(new_manifest)

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

    if failed_pages:
        logger.warning("\nFailed pages:")
        for page in failed_pages[:10]:
            logger.warning(f"  - {page}")

    # Auto-regenerate indexes (unless skipped for parallel fetching)
    logger.info("\n" + "=" * 60)
    try:
        import subprocess
        scripts_dir = Path(__file__).parent

        # Enhance manifest (always run this)
        enhance_script = scripts_dir / 'enhance_code_claude_manifest.py'
        if enhance_script.exists():
            logger.info("Enhancing manifest...")
            result = subprocess.run(
                [sys.executable, str(enhance_script)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                logger.warning(f"Manifest enhancement had issues: {result.stderr}")

        # Regenerate indexes (skip if --skip-indexes)
        if not args.skip_indexes:
            logger.info("Regenerating indexes...")
            result = subprocess.run(
                [sys.executable, str(scripts_dir / 'generate_indexes.py')],
                capture_output=True,
                text=True
            )
            if result.returncode == 0:
                logger.info("Indexes regenerated successfully")
            else:
                logger.warning(f"Index generation had issues: {result.stderr}")
        else:
            logger.info("Skipping index regeneration (--skip-indexes)")
    except Exception as e:
        logger.warning(f"Failed to regenerate indexes: {e}")

    if stats['successful'] == 0:
        logger.error("No pages were fetched successfully!")
        sys.exit(1)

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
