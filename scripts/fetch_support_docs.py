#!/usr/bin/env python3
"""
Fetch and convert Claude support documentation from support.claude.com

Features:
- Async concurrent fetching with connection pooling
- Local hash-based change detection (server doesn't support ETags)
- CLI flags: --force, --dry-run, --concurrency, --rediscover
- Automatic article discovery via collection crawling
- Converts Intercom JSON blocks to clean markdown
"""

import argparse
import asyncio
import aiohttp
import hashlib
import json
import html
import logging
import sys
import os
import re
from bs4 import BeautifulSoup
from pathlib import Path
from datetime import datetime
from typing import List, Dict, Set, Optional, Any

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)
logger = logging.getLogger(__name__)

# Constants
BASE_URL = "https://support.claude.com"
OUTPUT_DIR = Path(__file__).parent.parent / "docs-support"
MANIFEST_FILE = "support_manifest.json"
CACHE_FILE = "discovered_articles.json"

HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/5.0 (Efficient Documentation Mirror)',
    'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8',
}

# Defaults
DEFAULT_CONCURRENCY = 5
MAX_RETRIES = 3
DISCOVERY_RATE_LIMIT = 1.0


# =============================================================================
# Article Discovery Functions (Synchronous - runs once)
# =============================================================================

def discover_collections_sync() -> List[Dict]:
    """Fetch homepage and extract collection metadata from __NEXT_DATA__."""
    import requests

    url = f"{BASE_URL}/en"
    logger.info(f"Discovering collections from {url}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')
        script = soup.find('script', id='__NEXT_DATA__')

        if not script:
            logger.error("No __NEXT_DATA__ found on homepage")
            return []

        data = json.loads(script.string)
        collections = data.get('props', {}).get('pageProps', {}).get('home', {}).get('collections', [])

        logger.info(f"Found {len(collections)} top-level collections")
        return collections

    except Exception as e:
        logger.error(f"Failed to discover collections: {e}")
        return []


def discover_articles_in_collection_sync(
    collection_url: str,
    visited_collections: set,
    visited_articles: set
) -> List[Dict]:
    """Scrape a collection page for article and sub-collection links (synchronous)."""
    import requests
    import time

    if collection_url in visited_collections:
        return []

    visited_collections.add(collection_url)
    articles = []

    if collection_url.startswith('/'):
        collection_url = f"{BASE_URL}{collection_url}"

    logger.info(f"  Crawling: {collection_url}")

    try:
        response = requests.get(collection_url, headers=HEADERS, timeout=15)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, 'html.parser')

        collection_name = "support"
        title_tag = soup.find('h1')
        if title_tag:
            collection_name = title_tag.get_text(strip=True)

        links = soup.find_all('a', href=True)
        sub_collections = []

        for link in links:
            href = link.get('href', '')
            title = link.get_text(strip=True)

            if not title or len(title) < 3:
                continue

            if '/articles/' in href:
                if href.startswith('/'):
                    full_url = f"{BASE_URL}{href}"
                else:
                    full_url = href

                if full_url not in visited_articles:
                    visited_articles.add(full_url)
                    articles.append({
                        'title': title,
                        'url': full_url,
                        'collection': collection_name
                    })

            elif '/collections/' in href and href not in visited_collections:
                if href.startswith('/'):
                    full_url = f"{BASE_URL}{href}"
                else:
                    full_url = href
                sub_collections.append(full_url)

        logger.info(f"    Found {len(articles)} articles, {len(sub_collections)} sub-collections")

        time.sleep(DISCOVERY_RATE_LIMIT)

        for sub_url in sub_collections:
            sub_articles = discover_articles_in_collection_sync(sub_url, visited_collections, visited_articles)
            articles.extend(sub_articles)

        return articles

    except Exception as e:
        logger.error(f"  Failed to crawl {collection_url}: {e}")
        return articles


def discover_all_articles_sync() -> List[Dict]:
    """Main discovery: crawl all collections recursively (synchronous)."""
    import time

    logger.info("=" * 60)
    logger.info("Starting article discovery...")
    logger.info("=" * 60)

    collections = discover_collections_sync()

    if not collections:
        logger.error("No collections found!")
        return []

    visited_collections = set()
    visited_articles = set()
    all_articles = []

    for i, collection in enumerate(collections, 1):
        coll_id = collection.get('id', '')
        coll_name = collection.get('name', 'Unknown')

        slug = coll_name.lower().replace(' ', '-').replace('(', '').replace(')', '')
        slug = re.sub(r'[^a-z0-9-]', '', slug)
        collection_url = f"{BASE_URL}/en/collections/{coll_id}-{slug}"

        logger.info(f"\n[{i}/{len(collections)}] Collection: {coll_name}")

        articles = discover_articles_in_collection_sync(collection_url, visited_collections, visited_articles)
        all_articles.extend(articles)

        if i < len(collections):
            time.sleep(DISCOVERY_RATE_LIMIT)

    # Deduplicate
    seen_urls = set()
    unique_articles = []
    for article in all_articles:
        if article['url'] not in seen_urls:
            seen_urls.add(article['url'])
            unique_articles.append(article)

    logger.info(f"\n{'=' * 60}")
    logger.info(f"Discovery complete!")
    logger.info(f"Total unique articles: {len(unique_articles)}")
    logger.info(f"Collections crawled: {len(visited_collections)}")
    logger.info("=" * 60)

    return unique_articles


def load_cached_articles(cache_file: Path) -> Optional[List[Dict]]:
    """Load articles from JSON cache if it exists."""
    if cache_file.exists():
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)
            articles = data.get('articles', [])
            discovered_at = data.get('discovered_at', 'unknown')
            logger.info(f"Loaded {len(articles)} articles from cache (discovered: {discovered_at})")
            return articles
        except Exception as e:
            logger.warning(f"Failed to load cache: {e}")
    return None


def save_articles_cache(articles: List[Dict], cache_file: Path):
    """Save discovered articles to JSON cache."""
    try:
        data = {
            'discovered_at': datetime.now().isoformat(),
            'count': len(articles),
            'articles': articles
        }
        with open(cache_file, 'w', encoding='utf-8') as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
        logger.info(f"Saved {len(articles)} articles to cache: {cache_file}")
    except Exception as e:
        logger.error(f"Failed to save cache: {e}")


# =============================================================================
# Markdown Conversion Functions
# =============================================================================

def convert_html_links(text: str) -> str:
    """Convert HTML anchor tags to markdown links."""
    pattern = r'<a\s+(?:[^>]*?\s+)?href=["\']([^"\']*)["\'][^>]*>(.*?)</a>'

    def replace_link(match):
        url = match.group(1)
        link_text = match.group(2)
        link_text = re.sub(r'<[^>]+>', '', link_text)
        return f"[{link_text}]({url})"

    result = re.sub(pattern, replace_link, text, flags=re.IGNORECASE)
    result = re.sub(r'<b>(.*?)</b>', r'**\1**', result)
    result = re.sub(r'<strong>(.*?)</strong>', r'**\1**', result)
    result = re.sub(r'<i>(.*?)</i>', r'*\1*', result)
    result = re.sub(r'<em>(.*?)</em>', r'*\1*', result)

    return result


def convert_blocks_to_markdown(blocks: List[Dict[str, Any]]) -> str:
    """Convert Intercom JSON blocks to markdown format."""
    markdown_lines = []

    for block in blocks:
        block_type = block.get('type', 'unknown')

        if block_type == 'paragraph':
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            markdown_lines.append(text)
            markdown_lines.append('')

        elif block_type == 'heading':
            level = block.get('level', 2)
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            markdown_lines.append(f"{'#' * level} {text}")
            markdown_lines.append('')

        elif block_type == 'subheading':
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            markdown_lines.append(f"## {text}")
            markdown_lines.append('')

        elif block_type == 'subheading3':
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            markdown_lines.append(f"### {text}")
            markdown_lines.append('')

        elif block_type == 'subheading4':
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            markdown_lines.append(f"#### {text}")
            markdown_lines.append('')

        elif block_type == 'list':
            for item in block.get('items', []):
                text = html.unescape(item.get('text', ''))
                text = convert_html_links(text)
                markdown_lines.append(f"- {text}")
            markdown_lines.append('')

        elif block_type == 'unorderedNestedList':
            for item in block.get('items', []):
                for content_block in item.get('content', []):
                    text = html.unescape(content_block.get('text', ''))
                    text = convert_html_links(text)
                    markdown_lines.append(f"- {text}")
            markdown_lines.append('')

        elif block_type == 'orderedList':
            for i, item in enumerate(block.get('items', []), 1):
                text = html.unescape(item.get('text', ''))
                text = convert_html_links(text)
                markdown_lines.append(f"{i}. {text}")
            markdown_lines.append('')

        elif block_type == 'orderedNestedList':
            for i, item in enumerate(block.get('items', []), 1):
                for content_block in item.get('content', []):
                    text = html.unescape(content_block.get('text', ''))
                    text = convert_html_links(text)
                    markdown_lines.append(f"{i}. {text}")
            markdown_lines.append('')

        elif block_type == 'image':
            url = block.get('url', '')
            alt = block.get('alt', 'image')
            markdown_lines.append(f"![{alt}]({url})")
            markdown_lines.append('')

        elif block_type == 'code':
            code = block.get('text', block.get('code', ''))
            code = code.replace('<br>', '\n')
            code = html.unescape(code)
            language = block.get('language', '')
            markdown_lines.append(f"```{language}")
            markdown_lines.append(code)
            markdown_lines.append("```")
            markdown_lines.append('')

        elif block_type in ['callout', 'warning', 'note']:
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            if text.strip():
                markdown_lines.append(f"> **Note**: {text}")
                markdown_lines.append('')

        elif block_type == 'quote':
            text = html.unescape(block.get('text', ''))
            text = convert_html_links(text)
            markdown_lines.append(f"> {text}")
            markdown_lines.append('')

        elif block_type in ('divider', 'horizontalRule'):
            markdown_lines.append('---')
            markdown_lines.append('')

        elif block_type == 'table':
            rows = block.get('rows', [])
            for row_idx, row in enumerate(rows):
                cells = row.get('cells', [])
                cell_texts = []
                for cell in cells:
                    parts = []
                    for content_block in cell.get('content', []):
                        text = content_block.get('text', '')
                        text = html.unescape(text)
                        text = convert_html_links(text)
                        # Convert <code> tags to backticks
                        text = re.sub(r'<code>(.*?)</code>', r'`\1`', text)
                        # Strip any remaining HTML tags
                        text = re.sub(r'<[^>]+>', '', text)
                        parts.append(text.strip())
                    cell_texts.append(' '.join(parts))
                markdown_lines.append('| ' + ' | '.join(cell_texts) + ' |')
                if row_idx == 0:
                    markdown_lines.append('| ' + ' | '.join(['---'] * len(cell_texts)) + ' |')
            markdown_lines.append('')

        else:
            logger.warning(f"Unknown block type: {block_type}")

    return '\n'.join(markdown_lines)


def article_to_markdown(article_content: Dict[str, Any]) -> tuple[str, str]:
    """Convert article content to markdown.

    Returns:
        tuple: (content_for_hash, full_markdown)
            - content_for_hash: Stable content without volatile metadata (for change detection)
            - full_markdown: Complete markdown including lastUpdated (for file output)
    """
    title = article_content.get('title', 'Untitled')
    last_updated = article_content.get('lastUpdated', '')
    blocks = article_content.get('blocks', [])

    # Build stable content (title + body) for hashing
    body = convert_blocks_to_markdown(blocks)

    related_articles = article_content.get('relatedArticles', [])
    related_section = ""
    if related_articles:
        related_section = "\n\n---\n\n## Related Articles\n\n"
        for related in related_articles:
            rel_title = related.get('title', 'Unknown')
            rel_url = related.get('url', '#')
            related_section += f"- [{rel_title}]({rel_url})\n"

    content_for_hash = f"# {title}\n\n---\n\n{body}{related_section}"

    # Build full markdown with volatile metadata for file output
    full_markdown = f"# {title}\n\n"
    if last_updated:
        full_markdown += f"*{last_updated}*\n\n"
    full_markdown += f"---\n\n{body}{related_section}"

    return content_for_hash, full_markdown


def url_to_filename(url: str) -> str:
    """Convert article URL to a safe filename."""
    parts = url.split('/articles/')
    if len(parts) < 2:
        return "unknown.md"

    article_part = parts[1].split('?')[0].rstrip('/')

    if '-' in article_part:
        slug_parts = article_part.split('-', 1)
        if len(slug_parts) > 1:
            filename = slug_parts[1]
        else:
            filename = article_part
    else:
        filename = article_part

    filename = re.sub(r'[^\w\-]', '_', filename)
    filename = re.sub(r'_+', '_', filename)
    filename = filename.strip('_')

    return f"{filename}.md"


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

    manifest["base_url"] = f"https://raw.githubusercontent.com/{github_repo}/{github_ref}/docs-support/"
    manifest["github_repository"] = github_repo
    manifest["github_ref"] = github_ref
    manifest["source_site"] = "support.claude.com"
    manifest["last_updated"] = datetime.now().isoformat()

    manifest_path.write_text(json.dumps(manifest, indent=2))


# =============================================================================
# Async Fetching Functions
# =============================================================================

async def fetch_article(
    session: aiohttp.ClientSession,
    article: Dict,
    old_entry: Dict,
    force: bool,
    semaphore: asyncio.Semaphore
) -> Dict:
    """Fetch a single article and extract content."""
    async with semaphore:
        for attempt in range(MAX_RETRIES):
            try:
                async with session.get(
                    article['url'],
                    headers=HEADERS,
                    timeout=aiohttp.ClientTimeout(total=30)
                ) as response:

                    if response.status == 200:
                        html_content = await response.text()

                        soup = BeautifulSoup(html_content, 'html.parser')
                        scripts = soup.find_all('script', id='__NEXT_DATA__')

                        if not scripts:
                            return {'status': -1, 'error': 'No __NEXT_DATA__ found'}

                        data = json.loads(scripts[0].string)
                        page_props = data.get('props', {}).get('pageProps', {})
                        article_content = page_props.get('articleContent', {})

                        if not article_content:
                            return {'status': -1, 'error': 'No articleContent found'}

                        content_for_hash, full_markdown = article_to_markdown(article_content)
                        content_hash = hashlib.sha256(content_for_hash.encode('utf-8')).hexdigest()

                        return {
                            'status': 200,
                            'content': full_markdown,
                            'hash': content_hash,
                            'title': article_content.get('title', article['title']),
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
            except json.JSONDecodeError as e:
                return {'status': -1, 'error': f'JSON parse error: {e}'}

    return {'status': -1, 'error': 'Max retries exceeded'}


async def fetch_all_articles(
    articles: List[Dict],
    old_manifest: Dict,
    force: bool,
    concurrency: int,
    dry_run: bool
) -> Dict:
    """Fetch all articles concurrently."""

    semaphore = asyncio.Semaphore(concurrency)
    connector = aiohttp.TCPConnector(limit=concurrency, limit_per_host=concurrency)

    stats = {
        'successful': 0, 'failed': 0, 'unchanged': 0,
        'updated': 0, 'new': 0
    }
    failed_articles = []
    new_manifest = {"files": {}}
    current_files = set()

    if dry_run:
        logger.info("DRY RUN - checking what would be fetched...")
        for article in articles:
            filename = url_to_filename(article['url'])
            old_entry = old_manifest.get("files", {}).get(filename, {})
            if old_entry.get('hash'):
                logger.info(f"  Would check: {filename} (has hash)")
            else:
                logger.info(f"  Would fetch: {filename} (no hash)")
        return stats, failed_articles, old_manifest, set(old_manifest.get("files", {}).keys())

    async with aiohttp.ClientSession(connector=connector) as session:
        tasks = []
        for article in articles:
            filename = url_to_filename(article['url'])
            old_entry = old_manifest.get("files", {}).get(filename, {})
            task = fetch_article(session, article, old_entry, force, semaphore)
            tasks.append((article, filename, old_entry, task))

        total = len(tasks)
        for i, (article, filename, old_entry, task) in enumerate(tasks, 1):
            result = await task

            if i % 50 == 0 or i == total:
                logger.info(f"Progress: {i}/{total} ({stats['unchanged']} unchanged, {stats['updated']} updated)")

            if result['status'] == 200:
                content = result['content']
                old_hash = old_entry.get('hash', '')

                if old_hash == result['hash'] and not force:
                    stats['unchanged'] += 1
                    last_updated = old_entry.get('last_updated', datetime.now().isoformat())
                else:
                    if old_hash:
                        stats['updated'] += 1
                    else:
                        stats['new'] += 1
                    last_updated = datetime.now().isoformat()

                    # Only write if content changed
                    file_path = OUTPUT_DIR / filename
                    file_path.write_text(content, encoding='utf-8')

                new_manifest["files"][filename] = {
                    "original_url": article['url'],
                    "title": result.get('title', article['title']),
                    "collection": article.get('collection', ''),
                    "hash": result['hash'],
                    "last_updated": last_updated
                }

                current_files.add(filename)
                stats['successful'] += 1

            else:
                stats['failed'] += 1
                failed_articles.append(article['title'])
                logger.warning(f"Failed: {filename} - {result.get('error', 'Unknown error')}")

    return stats, failed_articles, new_manifest, current_files


def cleanup_old_files(current_files: Set[str], old_manifest: Dict) -> None:
    """Remove files that no longer exist in the source."""
    old_files = set(old_manifest.get("files", {}).keys())
    files_to_remove = old_files - current_files

    for filename in files_to_remove:
        if filename in [MANIFEST_FILE, CACHE_FILE]:
            continue
        file_path = OUTPUT_DIR / filename
        if file_path.exists():
            logger.info(f"Removing obsolete file: {filename}")
            file_path.unlink()


def main():
    """Main fetcher function."""
    parser = argparse.ArgumentParser(
        description='Fetch Claude support documentation efficiently'
    )
    parser.add_argument(
        '--force', action='store_true',
        help='Force full re-fetch, ignoring hashes'
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
        '--rediscover', action='store_true',
        help='Force fresh article discovery, ignore cache'
    )
    parser.add_argument(
        '--discover-only', action='store_true',
        help='Only discover articles, do not fetch content'
    )
    parser.add_argument(
        '--skip-indexes', action='store_true',
        help='Skip index regeneration (for parallel fetching)'
    )
    args = parser.parse_args()

    start_time = datetime.now()
    logger.info("=" * 60)
    logger.info("Starting support.claude.com documentation fetch")
    logger.info(f"Mode: {'DRY RUN' if args.dry_run else 'FORCE' if args.force else 'INCREMENTAL'}")
    logger.info(f"Concurrency: {args.concurrency}")
    logger.info("=" * 60)

    OUTPUT_DIR.mkdir(exist_ok=True)

    # Discovery phase
    cache_file = OUTPUT_DIR / CACHE_FILE

    if args.rediscover or not cache_file.exists():
        logger.info("Performing fresh article discovery...")
        articles = discover_all_articles_sync()
        if articles:
            save_articles_cache(articles, cache_file)
        else:
            logger.error("Discovery failed - no articles found")
            sys.exit(1)
    else:
        articles = load_cached_articles(cache_file)
        if not articles:
            logger.info("Cache empty or invalid, performing fresh discovery...")
            articles = discover_all_articles_sync()
            if articles:
                save_articles_cache(articles, cache_file)
            else:
                logger.error("Discovery failed - no articles found")
                sys.exit(1)

    logger.info(f"\nTotal articles to process: {len(articles)}")

    if args.discover_only:
        logger.info("Discovery-only mode - skipping content fetch")
        return 0

    # Load manifest
    old_manifest = load_manifest()
    logger.info(f"Existing manifest: {len(old_manifest.get('files', {}))} files")

    # Fetch phase
    stats, failed_articles, new_manifest, current_files = asyncio.run(
        fetch_all_articles(articles, old_manifest, args.force, args.concurrency, args.dry_run)
    )

    if args.dry_run:
        logger.info("\nDry run complete - no files were modified")
        return 0

    cleanup_old_files(current_files, old_manifest)

    new_manifest["fetch_metadata"] = {
        "last_fetch_completed": datetime.now().isoformat(),
        "fetch_duration_seconds": (datetime.now() - start_time).total_seconds(),
        "total_articles_discovered": len(articles),
        "articles_fetched_successfully": stats['successful'],
        "articles_failed": stats['failed'],
        "articles_unchanged": stats['unchanged'],
        "articles_updated": stats['updated'],
        "articles_new": stats['new'],
        "failed_articles": failed_articles[:20],
        "source_url": BASE_URL,
        "fetch_tool_version": "5.0",
        "fetch_mode": "force" if args.force else "incremental"
    }

    save_manifest(new_manifest)

    duration = datetime.now() - start_time
    logger.info("\n" + "=" * 60)
    logger.info(f"Fetch completed in {duration}")
    logger.info(f"Total articles discovered: {len(articles)}")
    logger.info(f"Successful: {stats['successful']}")
    logger.info(f"  - New: {stats['new']}")
    logger.info(f"  - Updated: {stats['updated']}")
    logger.info(f"  - Unchanged: {stats['unchanged']}")
    logger.info(f"Failed: {stats['failed']}")

    if failed_articles:
        logger.warning("\nFailed articles:")
        for title in failed_articles[:10]:
            logger.warning(f"  - {title}")
        if len(failed_articles) > 10:
            logger.warning(f"  ... and {len(failed_articles) - 10} more")

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
        logger.error("No articles were fetched successfully!")
        sys.exit(1)

    return 0 if stats['failed'] == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
