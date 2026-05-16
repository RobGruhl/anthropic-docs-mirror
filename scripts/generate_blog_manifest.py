#!/usr/bin/env python3
"""
Generate manifest file for engineering blog posts.
Scans blog files and extracts metadata to create blog_manifest.json.
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

    # Extract date (look for *date* pattern or Published: pattern)
    for line in lines[:20]:  # Check first 20 lines
        if line.startswith('*') and ('202' in line or '201' in line):
            # Extract date from *Month Day, Year* format
            date = line.strip('*').strip()
            break
        if 'Published' in line:
            date = line.split('Published')[-1].strip(':').strip()
            break

    # Extract summary (look for **Summary:** pattern)
    for i, line in enumerate(lines):
        if '**Summary:**' in line:
            summary = line.split('**Summary:**')[-1].strip()
            # If summary is empty, get next line
            if not summary and i + 1 < len(lines):
                summary = lines[i + 1].strip()
            break

    # Extract source URL (look for 📖 **Source:** pattern at end)
    source_url = ""
    for line in reversed(lines[-50:]):
        if '**Source:**' in line or 'Source:' in line:
            # Extract URL from markdown link format
            url_match = re.search(r'https://[^\s\)]+', line)
            if url_match:
                source_url = url_match.group(0)
            break

    # If no source URL found, construct from filename
    if not source_url:
        slug = filename.replace('.md', '')
        source_url = f"https://www.anthropic.com/engineering/{slug}"

    # Infer categories from content and filename
    categories = []
    keywords = []

    # Analyze filename and content for categories
    filename_lower = filename.lower()
    content_lower = content.lower()

    if 'claude-code' in filename_lower or 'claude code' in content_lower[:1000]:
        categories.append('claude-code')
    if 'agent' in filename_lower or 'agent' in content_lower[:1000]:
        categories.append('agents')
    if 'mcp' in filename_lower or 'model context protocol' in content_lower[:1000]:
        categories.append('mcp')
    if 'tool' in filename_lower or 'tools' in content_lower[:1000]:
        categories.append('tools')
    if 'skill' in filename_lower or 'skills' in content_lower[:1000]:
        categories.append('agent-skills')
    if 'sdk' in filename_lower or 'sdk' in content_lower[:1000]:
        categories.append('agent-sdk')
    if 'prompt' in filename_lower or 'prompting' in content_lower[:1000]:
        categories.append('prompt-engineering')
    if 'desktop' in filename_lower:
        categories.append('desktop')
    if 'retrieval' in filename_lower or 'contextual' in filename_lower:
        categories.append('rag')
        categories.append('retrieval')
    if 'sandbox' in filename_lower:
        categories.append('security')
    if 'postmortem' in filename_lower:
        categories.append('reliability')
    if 'swe-bench' in filename_lower or 'benchmark' in content_lower[:1000]:
        categories.append('benchmarks')

    # Default category
    if not categories:
        categories.append('engineering')

    # Extract keywords from title
    if title:
        # Remove common words
        common_words = {'the', 'a', 'an', 'and', 'or', 'but', 'with', 'for', 'to', 'in', 'on', 'at'}
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


def generate_blog_manifest():
    """Generate manifest for all blog posts."""
    blog_dir = Path(__file__).parent.parent / 'engineering-blog'

    if not blog_dir.exists():
        print(f"Error: Blog directory not found: {blog_dir}")
        return

    manifest = {
        "files": {},
        "source": "anthropic-engineering-blog",
        "base_url": "https://www.anthropic.com/engineering/",
        "last_updated": datetime.now().isoformat(),
        "description": "Anthropic Engineering Blog posts - technical articles about Claude, agents, and AI development"
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
            "source": "engineering-blog",
            "categories": metadata["categories"],
            "keywords": metadata["keywords"],
            "date_published": metadata["date"],
            "summary": metadata["summary"]
        }

        print(f"  Title: {metadata['title']}")
        print(f"  Categories: {', '.join(metadata['categories'])}")
        print(f"  Date: {metadata['date']}")

    # Write manifest
    manifest_file = blog_dir / 'blog_manifest.json'
    manifest_file.write_text(json.dumps(manifest, indent=2), encoding='utf-8')
    print(f"\nManifest written to: {manifest_file}")
    print(f"Total blog posts: {len(manifest['files'])}")


if __name__ == '__main__':
    generate_blog_manifest()
