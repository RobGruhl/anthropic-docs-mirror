#!/usr/bin/env python3
"""
Enhance docs manifest with categories and keywords metadata.
Reads existing docs_manifest.json and adds category/keyword information.
"""

import json
import re
from pathlib import Path
from typing import List, Dict

def categorize_from_url(url: str, filename: str) -> tuple[List[str], List[str]]:
    """Determine categories and keywords from URL path and filename."""
    categories = []
    keywords = []

    # Parse URL path
    url_lower = url.lower()
    filename_lower = filename.lower()

    # Main sections from URL
    if '/agent-sdk/' in url_lower:
        categories.append('agent-sdk')
    if '/agents-and-tools/' in url_lower:
        categories.append('agents-and-tools')
    if '/about-claude/' in url_lower:
        categories.append('about-claude')
    if '/build-with-claude/' in url_lower:
        categories.append('build-with-claude')
    if '/test-and-evaluate/' in url_lower:
        categories.append('test-and-evaluate')
    if '/get-started' in url_lower:
        categories.append('getting-started')

    # Specific topics
    if 'tool-use' in url_lower or 'tool' in filename_lower:
        categories.append('tool-use')
    if 'agent-skills' in url_lower or 'agent-skill' in url_lower:
        categories.append('agent-skills')
    if 'mcp' in url_lower:
        categories.append('mcp')
    if 'prompt' in url_lower:
        categories.append('prompt-engineering')
    if 'model' in url_lower and 'models' in url_lower:
        categories.append('models')
    if 'api' in url_lower or 'messages' in url_lower or 'streaming' in url_lower:
        categories.append('api')
    if 'batch' in url_lower:
        categories.append('batch-processing')
    if 'embed' in url_lower:
        categories.append('embeddings')
    if 'cach' in url_lower:
        categories.append('caching')
    if 'pricing' in url_lower or 'cost' in url_lower:
        categories.append('pricing')
    if 'secur' in url_lower:
        categories.append('security')
    if 'guardrail' in url_lower or 'moderation' in url_lower:
        categories.append('guardrails')
    if 'citation' in url_lower:
        categories.append('citations')
    if 'thinking' in url_lower or 'think' in url_lower:
        categories.append('extended-thinking')
    if 'context' in url_lower:
        categories.append('context')
    if 'file' in url_lower or 'pdf' in url_lower:
        categories.append('files')
    if 'structured-output' in url_lower:
        categories.append('structured-outputs')
    if 'changelog' in filename_lower:
        categories.append('changelog')
        categories.append('release-notes')

    # Cloud providers
    if 'bedrock' in url_lower or 'amazon' in url_lower:
        categories.append('amazon-bedrock')
    if 'vertex' in url_lower or 'google' in url_lower:
        categories.append('google-vertex-ai')

    # Code/development
    if 'code' in url_lower or 'bash' in url_lower or 'execution' in url_lower:
        categories.append('code-execution')
    if 'computer-use' in url_lower:
        categories.append('computer-use')

    # Evaluation
    if 'eval' in url_lower or 'test' in url_lower:
        categories.append('evaluation')

    # Extract keywords from filename parts
    # Split by double underscore (our convention)
    parts = filename.replace('.md', '').split('__')
    for part in parts:
        # Split by dash and take meaningful words
        words = part.split('-')
        for word in words:
            if len(word) > 3 and word not in {'about', 'with', 'from', 'that', 'this', 'your'}:
                keywords.append(word.lower())

    # Default category
    if not categories:
        categories.append('documentation')

    # Deduplicate
    categories = list(set(categories))
    keywords = list(set(keywords))[:10]  # Limit to 10 keywords

    return categories, keywords


def get_title_from_filename(filename: str) -> str:
    """Generate a readable title from filename."""
    # Remove .md extension
    name = filename.replace('.md', '')

    # Split by double underscore to get path parts
    parts = name.split('__')

    # Take the last part as the main title
    title_part = parts[-1] if parts else name

    # Replace dashes with spaces and title case
    title = title_part.replace('-', ' ').title()

    return title


def enhance_docs_manifest():
    """Add categories and keywords to existing docs manifest."""
    docs_dir = Path(__file__).parent.parent / 'docs'
    manifest_file = docs_dir / 'docs_manifest.json'

    if not manifest_file.exists():
        print(f"Error: Manifest file not found: {manifest_file}")
        return

    # Load existing manifest
    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    print(f"Enhancing manifest with {len(manifest['files'])} files")

    # Add source field to manifest metadata
    if 'source' not in manifest:
        manifest['source'] = 'developer-documentation'
        manifest['description'] = 'Official Claude developer documentation from docs.claude.com'

    # Process each file
    enhanced_count = 0
    for filename, file_info in manifest['files'].items():
        original_url = file_info.get('original_url', '')

        # Get categories and keywords
        categories, keywords = categorize_from_url(original_url, filename)

        # Get title
        title = get_title_from_filename(filename)

        # Add new fields
        file_info['source'] = 'developer-docs'
        file_info['categories'] = categories
        file_info['keywords'] = keywords
        file_info['title'] = title

        enhanced_count += 1

        if enhanced_count <= 5 or enhanced_count % 20 == 0:
            print(f"  [{enhanced_count}] {filename}")
            print(f"      Title: {title}")
            print(f"      Categories: {', '.join(categories[:5])}")

    # Write enhanced manifest
    with open(manifest_file, 'w', encoding='utf-8') as f:
        f.write(json.dumps(manifest, indent=2))

    print(f"\nEnhanced manifest written to: {manifest_file}")
    print(f"Total files enhanced: {enhanced_count}")

    # Show category distribution
    category_counts = {}
    for file_info in manifest['files'].values():
        for cat in file_info.get('categories', []):
            category_counts[cat] = category_counts.get(cat, 0) + 1

    print(f"\nCategory distribution (top 15):")
    for cat, count in sorted(category_counts.items(), key=lambda x: x[1], reverse=True)[:15]:
        print(f"  {cat}: {count} files")


if __name__ == '__main__':
    enhance_docs_manifest()
