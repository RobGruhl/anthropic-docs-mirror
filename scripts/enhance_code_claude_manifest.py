#!/usr/bin/env python3
"""
Enhance code.claude.com manifest with categories and keywords metadata.
Reads existing code_claude_manifest.json and adds category/keyword information.
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

    # Core Claude Code topics
    if 'plugin' in url_lower or 'plugin' in filename_lower:
        categories.append('plugins')
    if 'hook' in url_lower or 'hook' in filename_lower:
        categories.append('hooks')
    if 'mcp' in url_lower:
        categories.append('mcp')
    if 'sub-agent' in url_lower or 'subagent' in url_lower:
        categories.append('sub-agents')
    if 'skill' in url_lower:
        categories.append('skills')
    if 'slash-command' in url_lower or 'command' in url_lower:
        categories.append('slash-commands')
    if 'settings' in url_lower or 'config' in url_lower:
        categories.append('configuration')
    if 'setup' in url_lower or 'install' in url_lower:
        categories.append('setup')
    if 'quickstart' in url_lower or 'getting-started' in url_lower:
        categories.append('getting-started')
    if 'overview' in url_lower:
        categories.append('overview')

    # Integrations
    if 'vs-code' in url_lower or 'vscode' in url_lower:
        categories.append('vs-code')
    if 'jetbrains' in url_lower:
        categories.append('jetbrains')
    if 'devcontainer' in url_lower:
        categories.append('devcontainer')

    # CI/CD
    if 'github-action' in url_lower:
        categories.append('ci-cd')
        categories.append('github-actions')
    if 'gitlab' in url_lower:
        categories.append('ci-cd')
        categories.append('gitlab')
    if 'headless' in url_lower:
        categories.append('ci-cd')
        categories.append('headless')

    # Cloud platforms
    if 'bedrock' in url_lower or 'amazon' in url_lower or 'aws' in url_lower:
        categories.append('cloud-platforms')
        categories.append('amazon-bedrock')
    if 'vertex' in url_lower or 'google' in url_lower or 'gcp' in url_lower:
        categories.append('cloud-platforms')
        categories.append('google-vertex-ai')
    if 'microsoft' in url_lower or 'azure' in url_lower or 'foundry' in url_lower:
        categories.append('cloud-platforms')
        categories.append('microsoft-foundry')

    # Administration
    if 'iam' in url_lower:
        categories.append('administration')
        categories.append('security')
    if 'security' in url_lower:
        categories.append('administration')
        categories.append('security')
    if 'monitor' in url_lower or 'usage' in url_lower or 'analytic' in url_lower:
        categories.append('administration')
        categories.append('monitoring')
    if 'cost' in url_lower:
        categories.append('administration')
        categories.append('costs')
    if 'data-usage' in url_lower:
        categories.append('administration')
        categories.append('data-privacy')

    # Configuration
    if 'network' in url_lower:
        categories.append('configuration')
        categories.append('networking')
    if 'model' in url_lower:
        categories.append('configuration')
        categories.append('model-config')
    if 'terminal' in url_lower:
        categories.append('configuration')
        categories.append('terminal')
    if 'output-style' in url_lower:
        categories.append('configuration')
        categories.append('output-styles')
    if 'statusline' in url_lower:
        categories.append('configuration')
        categories.append('statusline')
    if 'sandbox' in url_lower:
        categories.append('configuration')
        categories.append('sandboxing')

    # Features
    if 'memory' in url_lower:
        categories.append('features')
        categories.append('memory')
    if 'checkpoint' in url_lower:
        categories.append('features')
        categories.append('checkpointing')
    if 'interactive' in url_lower:
        categories.append('features')
        categories.append('interactive-mode')

    # Deployment
    if 'third-party' in url_lower or 'gateway' in url_lower:
        categories.append('deployment')
        categories.append('integrations')

    # Reference
    if 'cli-reference' in url_lower or 'reference' in url_lower:
        categories.append('reference')
    if 'workflow' in url_lower:
        categories.append('workflows')
    if 'legal' in url_lower or 'compliance' in url_lower:
        categories.append('legal')
    if 'troubleshoot' in url_lower:
        categories.append('troubleshooting')

    # Web version
    if 'web' in url_lower and 'claude-code' in url_lower:
        categories.append('web-version')

    # SDK
    if 'sdk' in url_lower or 'migration' in url_lower:
        categories.append('sdk')
        categories.append('agent-sdk')

    # Extract keywords from filename parts
    # Split by double underscore (our convention)
    parts = filename.replace('.md', '').split('__')
    for part in parts:
        # Split by dash and take meaningful words
        words = part.split('-')
        for word in words:
            if len(word) > 3 and word not in {'about', 'with', 'from', 'that', 'this', 'your', 'docs'}:
                keywords.append(word.lower())

    # Default category
    if not categories:
        categories.append('claude-code')

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


def enhance_code_claude_manifest():
    """Add categories and keywords to existing code.claude.com manifest."""
    docs_dir = Path(__file__).parent.parent / 'code-claude-docs'
    manifest_file = docs_dir / 'code_claude_manifest.json'

    if not manifest_file.exists():
        print(f"Error: Manifest file not found: {manifest_file}")
        return

    # Load existing manifest
    with open(manifest_file, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    print(f"Enhancing code.claude.com manifest with {len(manifest['files'])} files")

    # Add source field to manifest metadata
    if 'source' not in manifest:
        manifest['source'] = 'code-claude-documentation'
        manifest['description'] = 'Official Claude Code documentation from code.claude.com'

    # Process each file
    enhanced_count = 0
    for filename, file_info in manifest['files'].items():
        original_url = file_info.get('original_url', '')

        # Get categories and keywords
        categories, keywords = categorize_from_url(original_url, filename)

        # Get title
        title = get_title_from_filename(filename)

        # Add new fields
        file_info['source'] = 'code-claude-docs'
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
    enhance_code_claude_manifest()
