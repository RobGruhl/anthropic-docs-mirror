#!/usr/bin/env python3
"""
Fetch Anthropic Engineering Blog Posts from anthropic.com/engineering

Features:
- HTTP conditional requests (ETag, If-Modified-Since) for efficient updates
- Async concurrent fetching with connection pooling
- CLI flags: --force, --dry-run, --concurrency
- HTML to markdown conversion
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
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Optional

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://www.anthropic.com"
ENGINEERING_INDEX = f"{BASE_URL}/engineering"
OUTPUT_DIR = Path(__file__).parent.parent / "engineering-blog"
MANIFEST_FILE = "blog_manifest.json"

HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

# Defaults
DEFAULT_CONCURRENCY = 5
MAX_RETRIES = 3


def discover_blog_posts_sync() -> List[Dict]:
    """Discover all engineering blog post URLs (synchronous)."""
    import requests

    logger.info(f"Discovering blog posts from {ENGINEERING_INDEX}")

    try:
        response = requests.get(ENGINEERING_INDEX, headers=HEADERS, timeout=30)
        response.raise_for_status()

        post_urls = set()
        for match in re.finditer(r'href="/engineering/([^"]+)"', response.text):
            slug = match.group(1)
            if slug and slug != 'engineering':
                post_urls.add(slug)

        pages = []
        for slug in sorted(post_urls):
            url = f"{BASE_URL}/engineering/{slug}"
            filename = f"{slug}.md"
            pages.append({
                'url': url,
                'slug': slug,
                'filename': filename,
            })

        logger.info(f"Found {len(pages)} blog posts")
        return pages

    except Exception as e:
        logger.error(f"Error discovering blog posts: {e}")
        return []


def html_to_markdown(html_content: str, url: str) -> tuple:
    """Convert HTML content to markdown format. Returns (markdown, title, date, summary)."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Extract title
    title = None
    title_elem = soup.find('h1')
    if title_elem:
        title = title_elem.get_text(strip=True)

    # Extract date
    date = None
    date_elem = soup.find(string=re.compile(r'Published'))
    if date_elem:
        date = date_elem.strip()

    # Extract summary/description
    summary = None
    meta_desc = soup.find('meta', {'name': 'description'})
    if meta_desc:
        summary = meta_desc.get('content', '')

    # Extract main content
    content_parts = []
    article = soup.find('article')
    if article:
        for elem in article.find_all(['p', 'h2', 'h3', 'h4', 'pre', 'code', 'ol', 'ul', 'li', 'blockquote']):
            text = elem.get_text(strip=True)
            if text:
                if elem.name == 'h2':
                    content_parts.append(f"\n## {text}\n")
                elif elem.name == 'h3':
                    content_parts.append(f"\n### {text}\n")
                elif elem.name == 'h4':
                    content_parts.append(f"\n#### {text}\n")
                elif elem.name in ['pre', 'code']:
                    content_parts.append(f"\n```\n{text}\n```\n")
                elif elem.name == 'blockquote':
                    content_parts.append(f"\n> {text}\n")
                else:
                    content_parts.append(text)

    content = '\n\n'.join(content_parts)

    # Build markdown
    md_parts = [
        f"# {title or 'Untitled'}",
        "",
        f"*{date or 'Date unknown'}*",
        "",
        "---",
        "",
    ]

    if summary:
        md_parts.extend([f"**Summary:** {summary}", ""])

    md_parts.extend([
        content,
        "",
        "---",
        "",
        f"**Source:** {url}",
        "",
        "*This is a mirror of the Anthropic engineering blog for offline reading. All content is copyright Anthropic.*",
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

    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/engineering-blog/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["source_site"] = "anthropic.com/engineering"
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
        tasks = []
        for page in pages:
            old_entry = old_manifest.get("files", {}).get(page['filename'], {})
            task = fetch_post(session, page, old_entry, force, semaphore)
            tasks.append((page, old_entry, task))

        total = len(tasks)
        for i, (page, old_entry, task) in enumerate(tasks, 1):
            result = await task

            logger.info(f"[{i}/{total}] {page['slug']}: {result.get('status', 'error')}")

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
                    "date": result.get('date', ''),
                    "summary": result.get('summary', ''),
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
        description='Fetch Anthropic engineering blog efficiently'
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
    logger.info("Starting Anthropic engineering blog fetch")
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
        logger.error("No blog posts discovered!")
        sys.exit(1)

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
        "source_url": ENGINEERING_INDEX,
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

    # Auto-regenerate indexes (unless skipped for parallel fetching)
    logger.info("\n" + "=" * 60)
    try:
        import subprocess
        scripts_dir = Path(__file__).parent

        # Generate blog manifest (always run this)
        gen_script = scripts_dir / 'generate_blog_manifest.py'
        if gen_script.exists():
            logger.info("Generating blog manifest...")
            result = subprocess.run(
                [sys.executable, str(gen_script)],
                capture_output=True,
                text=True
            )
            if result.returncode != 0:
                logger.warning(f"Manifest generation had issues: {result.stderr}")

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
        logger.error("No posts were fetched successfully!")
        sys.exit(1)

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
