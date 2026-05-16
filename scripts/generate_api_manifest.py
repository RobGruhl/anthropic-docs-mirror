#!/usr/bin/env python3
"""
Generate enhanced manifest for API documentation with categories and keywords.
"""

import json
import hashlib
from pathlib import Path
from typing import Dict, List
import re

BASE_DIR = Path(__file__).parent.parent / "api-docs"
MANIFEST_FILE = BASE_DIR / "api_manifest.json"

def extract_title(content: str, filename: str) -> str:
    """Extract title from markdown content."""
    lines = content.split('\n')
    for line in lines[:20]:
        if line.startswith('# '):
            return line[2:].strip()

    # Fallback to filename
    return filename.replace('__', ' / ').replace('.md', '').replace('-', ' ').title()

def infer_categories(filename: str, content: str) -> List[str]:
    """Infer categories from filename and content."""
    categories = ["api"]

    # Category keywords
    category_map = {
        "messages": ["messages", "message"],
        "batch": ["batch", "batches"],
        "files": ["files", "file-"],
        "models": ["models", "model"],
        "client-sdks": ["sdk", "client"],
        "rate-limits": ["rate", "limits"],
        "errors": ["errors", "error"],
        "versioning": ["version"],
        "authentication": ["auth", "api-key"],
        "streaming": ["stream"],
    }

    filename_lower = filename.lower()
    content_lower = content.lower()

    for category, keywords in category_map.items():
        if any(kw in filename_lower for kw in keywords):
            categories.append(category)

    return list(set(categories))

def extract_keywords(content: str, filename: str) -> List[str]:
    """Extract keywords from content."""
    keywords = []

    # Extract from filename
    name_parts = filename.replace('.md', '').replace('__', '-').split('-')
    keywords.extend(name_parts)

    # Common API terms
    api_terms = [
        'endpoint', 'request', 'response', 'parameter', 'authentication',
        'rate limit', 'batch', 'streaming', 'token', 'model', 'message',
        'file', 'sdk', 'client', 'error', 'version', 'header', 'status'
    ]

    content_lower = content.lower()
    for term in api_terms:
        if term in content_lower:
            keywords.append(term)

    # Remove duplicates and common words
    keywords = [k for k in set(keywords) if k not in ['the', 'a', 'an', 'and', 'or', 'but']]
    return keywords[:10]  # Limit to 10 keywords

def generate_manifest():
    """Generate enhanced manifest with metadata."""
    if not MANIFEST_FILE.exists():
        print(f"Error: Manifest file not found: {MANIFEST_FILE}")
        return 1

    # Load existing manifest
    with open(MANIFEST_FILE, 'r', encoding='utf-8') as f:
        manifest = json.load(f)

    # Enhance each file entry
    for filename, metadata in manifest['files'].items():
        filepath = BASE_DIR / filename

        if not filepath.exists():
            print(f"Warning: File not found: {filepath}")
            continue

        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Extract metadata
        metadata['title'] = extract_title(content, filename)
        metadata['categories'] = infer_categories(filename, content)
        metadata['keywords'] = extract_keywords(content, filename)

        # Verify hash
        current_hash = hashlib.sha256(content.encode('utf-8')).hexdigest()
        if metadata['hash'] != current_hash:
            print(f"Warning: Hash mismatch for {filename}")
            metadata['hash'] = current_hash

    # Write updated manifest
    with open(MANIFEST_FILE, 'w', encoding='utf-8') as f:
        f.write(json.dumps(manifest, indent=2))

    print(f"✓ Enhanced manifest written to {MANIFEST_FILE}")
    print(f"  Total files: {len(manifest['files'])}")

    return 0

if __name__ == "__main__":
    exit(generate_manifest())
