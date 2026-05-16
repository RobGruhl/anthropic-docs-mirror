#!/usr/bin/env python3
"""
Generate manifest file for support articles.
Scans support docs and extracts metadata to create support_manifest.json.

Uses discovered_articles.json as the source of truth for article URLs.
"""

import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Optional


def load_discovered_articles(support_dir: Path) -> Dict[str, Dict]:
    """
    Load discovered articles cache and build a lookup by slug.
    Returns dict mapping slug -> {url, title, collection}
    """
    cache_file = support_dir / 'discovered_articles.json'
    url_lookup = {}

    if cache_file.exists():
        try:
            with open(cache_file, 'r', encoding='utf-8') as f:
                data = json.load(f)

            for article in data.get('articles', []):
                url = article.get('url', '')
                # Extract slug from URL: /articles/{id}-{slug}
                if '/articles/' in url:
                    parts = url.split('/articles/')[-1].split('?')[0].rstrip('/')
                    # Get slug part (after the ID)
                    if '-' in parts:
                        slug = parts.split('-', 1)[1]
                    else:
                        slug = parts

                    # Clean slug to match filename format
                    slug_clean = re.sub(r'[^\w\-]', '_', slug)
                    slug_clean = re.sub(r'_+', '_', slug_clean).strip('_')

                    url_lookup[slug_clean] = {
                        'url': url,
                        'title': article.get('title', ''),
                        'collection': article.get('collection', 'support')
                    }

            print(f"Loaded {len(url_lookup)} URLs from discovered_articles.json")
        except Exception as e:
            print(f"Warning: Failed to load discovered articles: {e}")

    return url_lookup


def extract_article_id_from_url(url: str) -> str:
    """Extract article ID from support URL."""
    match = re.search(r'/articles/(\d+)-', url)
    return match.group(1) if match else ""


def categorize_article(filename: str, content: str, title: str) -> List[str]:
    """
    Categorize article based on filename, title, and content.
    Only looks at the main content, NOT the Related Articles section.
    """
    categories = []

    filename_lower = filename.lower()
    title_lower = title.lower()

    # Find where Related Articles section starts to exclude it from content analysis
    content_lines = content.split('\n')
    main_content_end = len(content_lines)
    for i, line in enumerate(content_lines):
        if line.strip().startswith('## Related Articles') or line.strip() == '---' and i > len(content_lines) * 0.7:
            main_content_end = i
            break

    # Only analyze main content (first ~1500 chars or before Related Articles)
    main_content = '\n'.join(content_lines[:main_content_end])[:2000].lower()

    # Platform/product categories - check filename and title primarily
    if 'claude-code' in filename_lower or 'claude code' in title_lower:
        categories.append('claude-code')
    if 'desktop' in filename_lower or 'desktop' in title_lower:
        categories.append('desktop')
    if any(x in filename_lower for x in ['mobile', 'ios', 'android']) or any(x in title_lower for x in ['mobile', 'ios', 'android']):
        categories.append('mobile')
    if 'chrome' in filename_lower or 'chrome' in title_lower:
        categories.append('chrome-extension')
    if 'excel' in filename_lower or 'sheets' in filename_lower:
        categories.append('sheets')

    # MCP - must be in filename or title, OR prominently in main content header
    if 'mcp' in filename_lower or 'mcp' in title_lower:
        categories.append('mcp')
    elif 'model context protocol' in main_content[:500]:
        categories.append('mcp')
    elif 'connector' in filename_lower and ('remote' in filename_lower or 'mcp' in main_content[:500]):
        categories.append('mcp')

    # Skills (Agent Skills) - check filename and title
    if 'skill' in filename_lower or 'skill' in title_lower:
        categories.append('skills')

    # API - be specific
    if 'api' in filename_lower or 'api key' in title_lower or 'api' in title_lower.split():
        categories.append('api')

    # Account management
    if any(x in filename_lower for x in ['account', 'login', 'password', 'email', 'phone']):
        categories.append('account')

    # Billing
    if any(x in filename_lower for x in ['billing', 'subscription', 'payment', 'invoice']):
        categories.append('billing')

    # Plans - be careful not to over-match
    if any(x in filename_lower for x in ['plan', 'pricing']):
        categories.append('plans')
    elif 'pro plan' in title_lower or 'max plan' in title_lower or 'team plan' in title_lower or 'enterprise' in title_lower:
        categories.append('plans')

    # Usage
    if any(x in filename_lower for x in ['usage', 'limits', 'rate-limit']):
        categories.append('usage')

    # Security
    if any(x in filename_lower for x in ['security', 'compliance', 'privacy', 'hipaa', 'soc2']):
        categories.append('security')

    # Integrations
    if any(x in filename_lower for x in ['integration', 'slack', 'google-workspace']):
        categories.append('integrations')

    # Artifacts
    if 'artifact' in filename_lower or 'artifact' in title_lower:
        categories.append('artifacts')

    # Projects
    if 'project' in filename_lower and 'projection' not in filename_lower:
        categories.append('projects')

    # FAQ
    if 'faq' in filename_lower:
        categories.append('faq')

    # Troubleshooting
    if any(x in filename_lower for x in ['troubleshoot', 'error', 'issue', 'fix', 'problem']):
        categories.append('troubleshooting')

    # Getting started
    if 'getting-started' in filename_lower or 'how-to-get-started' in filename_lower:
        categories.append('getting-started')

    # Default category
    if not categories:
        categories.append('support')

    return list(set(categories))


def extract_keywords_from_title(title: str) -> List[str]:
    """Extract meaningful keywords from article title."""
    common_words = {
        'the', 'a', 'an', 'and', 'or', 'but', 'with', 'for', 'to', 'in', 'on',
        'at', 'how', 'what', 'why', 'when', 'can', 'does', 'is', 'are', 'do',
        'my', 'your', 'you', 'i', 'we', 'it', 'this', 'that', 'of', 'from'
    }
    words = [w.lower() for w in re.findall(r'\w+', title)
             if w.lower() not in common_words and len(w) > 2]
    return words[:7]


def extract_summary(content: str) -> str:
    """Extract first substantial paragraph as summary."""
    lines = content.split('\n')
    in_content = False

    for line in lines[:50]:
        line = line.strip()
        if line.startswith('#'):
            in_content = True
            continue
        # Skip metadata lines and short lines
        if in_content and line and not line.startswith('*') and not line.startswith('-') and len(line) > 50:
            # Truncate if needed
            if len(line) > 200:
                return line[:197] + '...'
            return line

    return ""


def generate_support_manifest():
    """Generate manifest for all support articles."""
    support_dir = Path(__file__).parent.parent / 'docs-support'

    if not support_dir.exists():
        print(f"Error: Support directory not found: {support_dir}")
        return

    # Load discovered articles for URL lookup
    url_lookup = load_discovered_articles(support_dir)

    manifest = {
        "files": {},
        "source": "claude-support",
        "base_url": "https://support.claude.com/en/articles/",
        "last_updated": datetime.now().isoformat(),
        "description": "Claude Support articles - help documentation and FAQs"
    }

    support_files = sorted(support_dir.glob('*.md'))
    print(f"Found {len(support_files)} support articles")

    # Track statistics
    category_counts = {}
    urls_from_cache = 0
    urls_constructed = 0

    for i, support_file in enumerate(support_files, 1):
        filename = support_file.name
        slug = filename.replace('.md', '')

        if i <= 5 or i % 50 == 0 or i == len(support_files):
            print(f"Processing [{i}/{len(support_files)}]: {filename}")

        # Read content
        try:
            content = support_file.read_text(encoding='utf-8')
        except Exception as e:
            print(f"  Error reading {filename}: {e}")
            continue

        # Extract title from content
        title = ""
        for line in content.split('\n'):
            if line.startswith('# '):
                title = line[2:].strip()
                break

        if not title:
            title = slug.replace('-', ' ').title()

        # Get URL from discovered articles cache (preferred) or construct it
        if slug in url_lookup:
            source_url = url_lookup[slug]['url']
            article_id = extract_article_id_from_url(source_url)
            urls_from_cache += 1
        else:
            # Construct URL from filename (fallback)
            source_url = f"https://support.claude.com/en/articles/{slug}"
            article_id = ""
            urls_constructed += 1

        # Calculate content hash
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

        # Extract metadata
        categories = categorize_article(filename, content, title)
        keywords = extract_keywords_from_title(title)
        summary = extract_summary(content)

        # Get file modification time
        file_last_updated = datetime.fromtimestamp(support_file.stat().st_mtime).isoformat()

        # Build manifest entry
        manifest["files"][filename] = {
            "title": title,
            "original_url": source_url,
            "hash": content_hash,
            "last_updated": file_last_updated,
            "source": "support",
            "categories": categories,
            "keywords": keywords,
            "article_id": article_id,
            "summary": summary
        }

        # Count categories
        for cat in categories:
            category_counts[cat] = category_counts.get(cat, 0) + 1

    # Write manifest
    manifest_file = support_dir / 'support_manifest.json'
    manifest_file.write_text(json.dumps(manifest, indent=2), encoding='utf-8')

    print(f"\nManifest written to: {manifest_file}")
    print(f"Total support articles: {len(manifest['files'])}")
    print(f"URLs from cache: {urls_from_cache}")
    print(f"URLs constructed: {urls_constructed}")
    print(f"\nCategory distribution:")
    for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:20]:
        print(f"  {cat}: {count} articles")


if __name__ == '__main__':
    generate_support_manifest()
