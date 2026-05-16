#!/usr/bin/env python3
"""
Generate manifest file for Claude.com blog posts.
Scans blog files and extracts metadata to create claude_blog_manifest.json.
"""

import json
import hashlib
import re
from pathlib import Path
from datetime import datetime
from typing import Dict, List

def extract_metadata_from_blog(content: str, filename: str) -> Dict:
    """Extract title, date, and keywords from blog post content."""
    lines = content.split('\n')

    title = ""
    date = ""
    summary = ""

    # Extract title (first # heading)
    for line in lines:
        if line.startswith('# '):
            title = line[2:].strip()
            break

    # Extract date (look for *date* pattern)
    for line in lines[:20]:
        if line.startswith('*') and ('202' in line or '201' in line):
            date = line.strip('*').strip()
            break

    # Extract first substantial paragraph as summary
    in_content = False
    for line in lines[:100]:
        line = line.strip()
        if line.startswith('#'):
            in_content = True
            continue
        if in_content and line and not line.startswith('*') and not line.startswith('---') and len(line) > 50:
            summary = line[:200] + ('...' if len(line) > 200 else '')
            break

    # Extract source URL from footer
    source_url = ""
    for line in reversed(lines[-20:]):
        if 'Source:**' in line:
            url_match = re.search(r'https://[^\s\)]+', line)
            if url_match:
                source_url = url_match.group(0)
            break

    # If no source URL, construct from filename
    if not source_url:
        slug = filename.replace('.md', '')
        source_url = f"https://www.claude.com/blog/{slug}"

    # Infer categories from content and filename
    categories = []
    keywords = []

    filename_lower = filename.lower()
    content_lower = content.lower()

    # Categorize by topic
    if 'claude-code' in filename_lower or 'claude code' in content_lower[:1500]:
        categories.append('claude-code')
    if 'api' in filename_lower or 'api' in content_lower[:1500]:
        categories.append('api')
    if 'agent' in filename_lower or 'agentic' in filename_lower or 'agent' in content_lower[:1500]:
        categories.append('agents')
    if 'mcp' in filename_lower or 'model context protocol' in content_lower[:1500]:
        categories.append('mcp')
    if 'tool' in filename_lower or 'tools' in content_lower[:1500]:
        categories.append('tools')
    if 'skill' in filename_lower or 'skills' in content_lower[:1500]:
        categories.append('agent-skills')
    if 'prompt' in filename_lower or 'prompting' in content_lower[:1500]:
        categories.append('prompt-engineering')
    if 'citation' in filename_lower:
        categories.append('citations')
    if 'cach' in filename_lower:
        categories.append('caching')
    if 'batch' in filename_lower:
        categories.append('batch-processing')
    if 'structured-output' in filename_lower:
        categories.append('structured-outputs')
    if 'console' in filename_lower:
        categories.append('console')
    if 'bedrock' in filename_lower:
        categories.append('amazon-bedrock')
    if 'vertex' in filename_lower or 'google' in filename_lower:
        categories.append('google-vertex-ai')
    if 'slack' in filename_lower:
        categories.append('integrations')
    if 'chrome' in filename_lower:
        categories.append('chrome-extension')
    if 'artifact' in filename_lower:
        categories.append('artifacts')
    if 'search' in filename_lower:
        categories.append('search')
    if 'security' in filename_lower:
        categories.append('security')
    if 'plugin' in filename_lower:
        categories.append('plugins')
    if 'connector' in filename_lower:
        categories.append('connectors')
    if 'enterprise' in filename_lower or 'business' in filename_lower:
        categories.append('enterprise')

    # Default category
    if not categories:
        categories.append('product')

    # Extract keywords from title
    if title:
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'with', 'for', 'to', 'in', 'on', 'at', 'how', 'what', 'introducing'}
        title_words = [w.lower() for w in re.findall(r'\w+', title) if w.lower() not in common_words]
        keywords.extend(title_words[:5])

    return {
        "title": title or filename.replace('.md', '').replace('-', ' ').title(),
        "date": date,
        "summary": summary,
        "original_url": source_url,
        "categories": list(set(categories)),
        "keywords": list(set(keywords))
    }


def generate_claude_blog_manifest():
    """Generate manifest for all Claude.com blog posts."""
    blog_dir = Path(__file__).parent.parent / 'claude-blog'

    if not blog_dir.exists():
        print(f"Error: Blog directory not found: {blog_dir}")
        return

    manifest = {
        "files": {},
        "source": "claude-blog",
        "base_url": "https://www.claude.com/blog/",
        "last_updated": datetime.now().isoformat(),
        "description": "Claude.com blog posts - product announcements, feature launches, and developer guides"
    }

    blog_files = sorted(blog_dir.glob('*.md'))
    print(f"Found {len(blog_files)} blog posts")

    for blog_file in blog_files:
        filename = blog_file.name
        print(f"Processing: {filename}")

        # Read content
        content = blog_file.read_text(encoding='utf-8')

        # Calculate hash
        content_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()

        # Extract metadata
        metadata = extract_metadata_from_blog(content, filename)

        # Get file modification time
        last_updated = datetime.fromtimestamp(blog_file.stat().st_mtime).isoformat()

        # Build manifest entry
        manifest["files"][filename] = {
            "title": metadata["title"],
            "original_url": metadata["original_url"],
            "hash": content_hash,
            "last_updated": last_updated,
            "source": "claude-blog",
            "categories": metadata["categories"],
            "keywords": metadata["keywords"],
            "date_published": metadata["date"],
            "summary": metadata["summary"]
        }

        print(f"  Title: {metadata['title']}")
        print(f"  Categories: {', '.join(metadata['categories'])}")
        print(f"  Date: {metadata['date']}")

    # Write manifest
    manifest_file = blog_dir / 'claude_blog_manifest.json'
    manifest_file.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f"\nManifest written to: {manifest_file}")
    print(f"Total blog posts: {len(manifest['files'])}")


if __name__ == '__main__':
    generate_claude_blog_manifest()
