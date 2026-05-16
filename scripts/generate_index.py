#!/usr/bin/env python3
"""
Generate a comprehensive index of all Claude documentation
"""

import re
from pathlib import Path
from typing import Dict, List, Tuple
import logging

logging.basicConfig(level=logging.INFO, format='%(message)s')

BASE_DIR = Path.home() / '.claude-code-docs'
DOCS_DEV = BASE_DIR / 'docs'
DOCS_SUPPORT = BASE_DIR / 'docs-support'
DOCS_BLOG = BASE_DIR / 'engineering-blog'

# Platform keywords for categorization
PLATFORM_KEYWORDS = {
    'Claude Web': ['claude.ai', 'web interface', 'claude web', 'browser'],
    'Claude Desktop': ['claude desktop', 'desktop app', 'macos', 'windows'],
    'Claude Mobile': ['mobile', 'ios', 'android', 'iphone', 'ipad'],
    'Claude Code': ['claude code', 'cli', 'command line', 'terminal'],
    'Claude for Chrome': ['chrome', 'browser extension'],
    'Claude for Excel': ['excel', 'spreadsheet'],
    'Claude Console': ['console', 'workbench', 'api console'],
    'Claude API': ['api', 'rest api', 'api endpoint', 'api key'],
    'Claude Agent SDK': ['agent sdk', 'sdk', 'typescript', 'python sdk'],
}

def extract_metadata(filepath: Path) -> Tuple[str, str, str]:
    """Extract title and first paragraph as description from markdown file."""
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract title (first H1)
        title_match = re.search(r'^#\s+(.+)$', content, re.MULTILINE)
        title = title_match.group(1).strip() if title_match else filepath.stem.replace('-', ' ').replace('__', ': ').title()

        # Extract first meaningful paragraph (skip metadata, skip short lines)
        lines = content.split('\n')
        description = ""
        in_metadata = False
        in_code = False

        for i, line in enumerate(lines):
            # Skip YAML frontmatter
            if i == 0 and line.strip() == '---':
                in_metadata = True
                continue
            if in_metadata:
                if line.strip() == '---':
                    in_metadata = False
                continue

            # Skip code blocks
            if line.strip().startswith('```'):
                in_code = not in_code
                continue
            if in_code:
                continue

            # Skip headings, links, empty lines
            if line.startswith('#') or line.strip() == '' or line.strip().startswith('['):
                continue

            # Skip markdown metadata like *Published*
            if line.strip().startswith('*') and line.strip().endswith('*') and len(line.strip()) < 50:
                continue

            # Skip horizontal rules
            if line.strip() in ['---', '***', '___']:
                continue

            # Get first substantial paragraph
            if len(line.strip()) > 40:
                # Clean up markdown
                desc = line.strip()
                desc = re.sub(r'\[([^\]]+)\]\([^\)]+\)', r'\1', desc)  # Remove links
                desc = re.sub(r'\*\*([^\*]+)\*\*', r'\1', desc)  # Remove bold
                desc = re.sub(r'\*([^\*]+)\*', r'\1', desc)  # Remove italic
                desc = re.sub(r'`([^`]+)`', r'\1', desc)  # Remove code

                # Get first 2 sentences
                sentences = re.split(r'(?<=[.!?])\s+', desc)
                description = ' '.join(sentences[:2])
                if len(description) > 200:
                    description = description[:197] + '...'
                break

        if not description:
            description = "Documentation for " + title

        # Determine platform(s)
        content_lower = content.lower()
        platforms = []
        for platform, keywords in PLATFORM_KEYWORDS.items():
            for keyword in keywords:
                if keyword.lower() in content_lower or keyword.lower() in filepath.name:
                    platforms.append(platform)
                    break

        # Default categorization based on source
        if not platforms:
            if filepath.parent.name == 'docs':
                platforms = ['Claude API']  # Developer docs default to API
            elif filepath.parent.name == 'engineering-blog':
                platforms = ['Engineering']
            else:
                platforms = ['General']

        return title, description, ', '.join(platforms)

    except Exception as e:
        logging.error(f"Error processing {filepath}: {e}")
        return filepath.stem.replace('-', ' ').title(), "Documentation file", "General"

def scan_directory(directory: Path, source_name: str) -> List[Dict]:
    """Scan a directory for markdown files and extract metadata."""
    docs = []

    if not directory.exists():
        logging.warning(f"Directory not found: {directory}")
        return docs

    for filepath in sorted(directory.glob('*.md')):
        title, description, platforms = extract_metadata(filepath)

        # Generate deep link
        filename = filepath.stem
        if source_name == 'Developer Documentation':
            base_url = "https://docs.anthropic.com/en/docs/"
            # Convert filename back to URL path
            url_path = filename.replace('__', '/')
            deep_link = f"{base_url}{url_path}"
        elif source_name == 'Support Articles':
            deep_link = f"https://support.claude.com/en/articles/{filename}"
        else:  # Engineering Blog
            deep_link = f"https://www.anthropic.com/engineering/{filename}"

        docs.append({
            'title': title,
            'description': description,
            'filename': filename,
            'deep_link': deep_link,
            'platforms': platforms,
            'source': source_name
        })

    return docs

def generate_index():
    """Generate comprehensive index.md file."""
    logging.info("Scanning documentation...")

    # Scan all directories
    dev_docs = scan_directory(DOCS_DEV, 'Developer Documentation')
    support_docs = scan_directory(DOCS_SUPPORT, 'Support Articles')
    blog_posts = scan_directory(DOCS_BLOG, 'Engineering Blog')

    all_docs = dev_docs + support_docs + blog_posts

    logging.info(f"Found {len(all_docs)} total documents:")
    logging.info(f"  - Developer Documentation: {len(dev_docs)}")
    logging.info(f"  - Support Articles: {len(support_docs)}")
    logging.info(f"  - Engineering Blog: {len(blog_posts)}")

    # Organize by platform
    by_platform = {}
    for doc in all_docs:
        for platform in doc['platforms'].split(', '):
            if platform not in by_platform:
                by_platform[platform] = []
            by_platform[platform].append(doc)

    # Generate index
    output = []
    output.append("# Claude Documentation Index")
    output.append("")
    output.append("**Complete index of Claude documentation across all platforms and sources.**")
    output.append("")
    output.append(f"**Total Documents:** {len(all_docs)} (Developer: {len(dev_docs)}, Support: {len(support_docs)}, Blog: {len(blog_posts)})")
    output.append("")
    output.append("---")
    output.append("")

    # Table of Contents
    output.append("## Table of Contents")
    output.append("")
    for platform in sorted(by_platform.keys()):
        anchor = platform.lower().replace(' ', '-').replace('/', '')
        output.append(f"- [{platform}](#{anchor}) ({len(by_platform[platform])} docs)")
    output.append("")
    output.append("---")
    output.append("")

    # Platform sections
    for platform in sorted(by_platform.keys()):
        output.append(f"## {platform}")
        output.append("")
        output.append(f"**{len(by_platform[platform])} documents**")
        output.append("")

        # Group by source within platform
        by_source = {}
        for doc in by_platform[platform]:
            source = doc['source']
            if source not in by_source:
                by_source[source] = []
            by_source[source].append(doc)

        for source in ['Developer Documentation', 'Support Articles', 'Engineering Blog']:
            if source not in by_source:
                continue

            output.append(f"### {source}")
            output.append("")

            for doc in sorted(by_source[source], key=lambda x: x['title']):
                output.append(f"**[{doc['title']}]({doc['deep_link']})**")
                output.append(f"- {doc['description']}")
                output.append(f"- *Local:* `/docs {doc['filename']}`")
                output.append("")

        output.append("---")
        output.append("")

    # Write index
    index_path = BASE_DIR / 'INDEX.md'
    with open(index_path, 'w', encoding='utf-8') as f:
        f.write('\n'.join(output))

    logging.info(f"✓ Generated index at: {index_path}")
    logging.info(f"  Total platforms: {len(by_platform)}")

if __name__ == '__main__':
    generate_index()
