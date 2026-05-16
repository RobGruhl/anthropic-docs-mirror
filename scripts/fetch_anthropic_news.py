#!/usr/bin/env python3
"""
Fetch news articles from anthropic.com/news

Features:
- Sitemap-based URL discovery from anthropic.com/sitemap.xml
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
import xml.etree.ElementTree as ET

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Constants
SITEMAP_URL = "https://www.anthropic.com/sitemap.xml"
BASE_URL = "https://www.anthropic.com/news/"
OUTPUT_DIR = Path(__file__).parent.parent / "anthropic-news"
MANIFEST_FILE = "news_manifest.json"

HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

# Defaults
DEFAULT_CONCURRENCY = 5
MAX_RETRIES = 3

# News categories for classification
NEWS_CATEGORIES = {
    'announcements': ['announce', 'introducing', 'launch', 'release', 'unveil', 'new'],
    'partnerships': ['partner', 'collaboration', 'integrate', 'amazon', 'google', 'microsoft'],
    'policy': ['policy', 'regulation', 'governance', 'government', 'senate', 'congress', 'legislation'],
    'products': ['claude', 'api', 'product', 'feature', 'update', 'improvement'],
    'company': ['team', 'hire', 'office', 'funding', 'investment', 'leadership'],
}


def categorize_news(title: str, content: str) -> List[str]:
    """Categorize news article based on title and content keywords."""
    categories = []
    text = (title + ' ' + content).lower()

    for category, keywords in NEWS_CATEGORIES.items():
        if any(kw in text for kw in keywords):
            categories.append(category)

    if not categories:
        categories = ['news']

    return categories


def discover_news_urls_sync() -> List[Dict]:
    """Discover news article URLs from sitemap (synchronous)."""
    import requests

    logger.info(f"Fetching sitemap: {SITEMAP_URL}")

    try:
        response = requests.get(SITEMAP_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        root = ET.fromstring(response.content)

        urls = []
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        for url_elem in root.findall('.//ns:url', namespace):
            loc_elem = url_elem.find('ns:loc', namespace)
            if loc_elem is not None and loc_elem.text:
                urls.append(loc_elem.text)

        if not urls:
            for url_elem in root.findall('.//url'):
                loc_elem = url_elem.find('loc')
                if loc_elem is not None and loc_elem.text:
                    urls.append(loc_elem.text)

        logger.info(f"Found {len(urls)} total URLs in sitemap")

        # Filter for news URLs
        pages = []
        seen_slugs = set()

        for url in urls:
            # Match pattern: /news/{slug} but not /news itself
            if '/news/' in url:
                # Skip index page and localized versions
                if any(lang in url for lang in ['/ja-jp/', '/de-de/', '/fr-fr/', '/es-es/', '/pt-br/']):
                    continue
                if any(skip in url for skip in ['/news?', '/news#']):
                    continue

                slug = url.rstrip('/').split('/')[-1]
                slug = slug.split('?')[0].split('#')[0]

                if slug and slug not in seen_slugs and slug != 'news':
                    seen_slugs.add(slug)
                    filename = f"{slug}.md"
                    pages.append({
                        'url': url,
                        'slug': slug,
                        'filename': filename,
                    })

        pages.sort(key=lambda x: x['slug'])
        logger.info(f"Found {len(pages)} news articles")
        return pages

    except Exception as e:
        logger.error(f"Failed to discover news articles: {e}")
        return []


def html_to_markdown(html_content: str, url: str) -> tuple:
    """Convert HTML content to markdown format."""
    soup = BeautifulSoup(html_content, 'html.parser')

    # Remove script, style, and nav elements
    for element in soup(['script', 'style', 'nav', 'header', 'footer']):
        element.decompose()

    # Extract title
    title = ""
    title_elem = soup.find('h1') or soup.find('title')
    if title_elem:
        title = title_elem.get_text(strip=True)
        # Clean up title - remove " | Anthropic" suffix
        if ' | Anthropic' in title:
            title = title.replace(' | Anthropic', '')
        if ' - Anthropic' in title:
            title = title.replace(' - Anthropic', '')

    # Extract date
    date = ""
    date_meta = soup.find('meta', {'property': 'article:published_time'}) or \
                soup.find('meta', {'name': 'date'})
    if date_meta:
        date = date_meta.get('content', '')

    if not date:
        # Try to find date in common patterns
        date_pattern = r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}'
        date_match = re.search(date_pattern, soup.get_text())
        if date_match:
            date = date_match.group(0)

    # Extract summary/abstract if available
    summary = ""
    summary_meta = soup.find('meta', {'name': 'description'}) or \
                   soup.find('meta', {'property': 'og:description'})
    if summary_meta:
        summary = summary_meta.get('content', '')

    # Convert content
    markdown_lines = []
    article = soup.find('article') or soup.find('main') or soup.find(class_=re.compile(r'(article|content|post)', re.I))
    content_elem = article if article else soup

    for elem in content_elem.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6', 'p', 'ul', 'ol', 'pre', 'blockquote', 'img']):
        if elem.name.startswith('h'):
            level = int(elem.name[1])
            text = elem.get_text(strip=True)
            if text:
                markdown_lines.append(f"{'#' * level} {text}\n")

        elif elem.name == 'p':
            text = elem.get_text(strip=True)
            if text:
                for link in elem.find_all('a'):
                    href = link.get('href', '')
                    link_text = link.get_text(strip=True)
                    if href and link_text:
                        text = text.replace(link_text, f"[{link_text}]({href})")
                markdown_lines.append(f"{text}\n")

        elif elem.name in ['ul', 'ol']:
            for li in elem.find_all('li', recursive=False):
                text = li.get_text(strip=True)
                if text:
                    markdown_lines.append(f"- {text}\n")
            markdown_lines.append("\n")

        elif elem.name == 'pre':
            code = elem.get_text()
            markdown_lines.append(f"```\n{code}\n```\n")

        elif elem.name == 'blockquote':
            text = elem.get_text(strip=True)
            if text:
                markdown_lines.append(f"> {text}\n")

        elif elem.name == 'img':
            src = elem.get('src', '')
            alt = elem.get('alt', 'image')
            if src:
                markdown_lines.append(f"![{alt}]({src})\n")

    content = '\n'.join(markdown_lines)
    content = re.sub(r'\n{3,}', '\n\n', content)

    # Categorize the news article
    categories = categorize_news(title, content)

    # Build output
    output = []
    output.append(f"# {title}\n" if title else "")
    if date:
        output.append(f"*{date}*\n")
    output.append("---\n")
    if summary:
        output.append(f"**Summary:** {summary}\n\n")
    output.append(content)
    output.append("\n---\n")
    output.append(f"**Source:** {url}\n")
    output.append("*This is a mirror of an Anthropic news article for local access and AI-assisted development.*\n")

    return ''.join(output), title, date, summary, categories


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

    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/anthropic-news/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["source_site"] = "anthropic.com/news"
    manifest["last_updated"] = datetime.now().isoformat()

    manifest_path.write_text(json.dumps(manifest, indent=2))


async def fetch_page(
    session: aiohttp.ClientSession,
    page: Dict,
    old_entry: Dict,
    force: bool,
    semaphore: asyncio.Semaphore
) -> Dict:
    """Fetch a single news article with conditional request support."""
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
                            'categories': old_entry.get('categories', []),
                        }

                    if response.status == 200:
                        html_content = await response.text()

                        markdown, title, date, summary, categories = html_to_markdown(html_content, page['url'])
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
                            'categories': categories,
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
                    "title": result.get('title', ''),
                    "date": result.get('date', ''),
                    "summary": result.get('summary', ''),
                    "categories": result.get('categories', []),
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
        description='Fetch Anthropic news articles efficiently'
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
    logger.info("Starting Anthropic news articles fetch")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'FORCE' if args.force else 'INCREMENTAL'}")
    logger.info(f"Concurrency: {args.concurrency}")
    logger.info("=" * 60)

    OUTPUT_DIR.mkdir(exist_ok=True)

    old_manifest = load_manifest()
    cached_count = sum(1 for f in old_manifest.get("files", {}).values() if f.get('etag') or f.get('last_modified'))
    logger.info(f"Existing manifest: {len(old_manifest.get('files', {}))} files ({cached_count} with cache headers)")

    try:
        pages = discover_news_urls_sync()
    except Exception as e:
        logger.error(f"Failed to discover pages: {e}")
        sys.exit(1)

    if not pages:
        logger.error("No news articles discovered!")
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
        "total_articles_discovered": len(pages),
        "articles_fetched_successfully": stats['successful'],
        "articles_failed": stats['failed'],
        "articles_unchanged": stats['unchanged'],
        "articles_updated": stats['updated'],
        "articles_new": stats['new'],
        "articles_skipped_304": stats['skipped_304'],
        "failed_articles": failed_pages,
        "source_sitemap": SITEMAP_URL,
        "fetch_tool_version": "5.0",
        "fetch_mode": "force" if args.force else "incremental"
    }

    save_manifest(new_manifest)

    duration = datetime.now() - start_time
    logger.info("\n" + "=" * 60)
    logger.info(f"Fetch completed in {duration}")
    logger.info(f"Total articles discovered: {len(pages)}")
    logger.info(f"Successful: {stats['successful']}")
    logger.info(f"  - Skipped (304): {stats['skipped_304']}")
    logger.info(f"  - New: {stats['new']}")
    logger.info(f"  - Updated: {stats['updated']}")
    logger.info(f"  - Unchanged: {stats['unchanged']}")
    logger.info(f"Failed: {stats['failed']}")

    if failed_pages:
        logger.warning("\nFailed articles:")
        for page in failed_pages[:10]:
            logger.warning(f"  - {page}")

    # Auto-regenerate indexes (unless skipped for parallel fetching)
    if not args.skip_indexes:
        logger.info("\n" + "=" * 60)
        try:
            import subprocess
            scripts_dir = Path(__file__).parent

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
        except Exception as e:
            logger.warning(f"Failed to regenerate indexes: {e}")
    else:
        logger.info("Skipping index regeneration (--skip-indexes)")

    if stats['successful'] == 0:
        logger.error("No articles were fetched successfully!")
        sys.exit(1)

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
