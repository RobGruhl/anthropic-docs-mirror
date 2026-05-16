#!/usr/bin/env python3
"""
Fetch API reference documentation from docs.claude.com/en/api/
"""

import requests
import hashlib
import json
import time
import logging
from pathlib import Path
from datetime import datetime
from typing import List, Dict
import xml.etree.ElementTree as ET
from urllib.parse import urlparse

# Configure logging
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)
logger = logging.getLogger(__name__)

# Constants
BASE_DIR = Path(__file__).parent.parent / "api-docs"
SITEMAP_URL = "https://docs.claude.com/sitemap.xml"
HEADERS = {
    'User-Agent': 'Claude-Docs-Fetcher/1.0 (Documentation Mirror Bot)'
}
RATE_LIMIT_DELAY = 0.5  # seconds between requests

def discover_api_pages() -> List[str]:
    """Discover API documentation pages from sitemap."""
    logger.info(f"Fetching sitemap: {SITEMAP_URL}")

    try:
        response = requests.get(SITEMAP_URL, headers=HEADERS, timeout=30)
        response.raise_for_status()

        # Parse XML safely (requires Python 3.8+)
        parser = ET.XMLParser(forbid_dtd=True, forbid_entities=True, forbid_external=True)
        root = ET.fromstring(response.content, parser=parser)

        # Extract URLs
        urls = []
        namespace = {'ns': 'http://www.sitemaps.org/schemas/sitemap/0.9'}

        # Try with namespace
        for url_elem in root.findall('.//ns:url', namespace):
            loc_elem = url_elem.find('ns:loc', namespace)
            if loc_elem is not None and loc_elem.text:
                urls.append(loc_elem.text)

        # Fallback without namespace
        if not urls:
            for loc_elem in root.findall('.//loc'):
                if loc_elem.text:
                    urls.append(loc_elem.text)

        logger.info(f"Found {len(urls)} total URLs in sitemap")

        # Filter for API documentation pages
        api_pages = []
        for url in urls:
            if '/en/api/' in url:
                parsed = urlparse(url)
                path = parsed.path

                # Remove trailing slash
                if path.endswith('/'):
                    path = path[:-1]

                api_pages.append(path)

        # Remove duplicates and sort
        api_pages = sorted(list(set(api_pages)))

        logger.info(f"Discovered {len(api_pages)} API documentation pages")
        return api_pages

    except Exception as e:
        logger.error(f"Failed to discover API pages: {e}")
        logger.info("Using comprehensive fallback list...")

        # Comprehensive fallback list of all known API pages
        return [
            # Core API
            "/en/api/overview",
            "/en/api/messages",
            "/en/api/messages-count-tokens",
            "/en/api/models",
            "/en/api/models-list",
            "/en/api/errors",
            "/en/api/rate-limits",
            "/en/api/versioning",
            "/en/api/client-sdks",
            "/en/api/openai-sdk",
            "/en/api/beta-headers",
            "/en/api/service-tiers",
            "/en/api/supported-regions",
            "/en/api/ip-addresses",
            "/en/api/migrating-from-text-completions-to-messages",
            # Files API
            "/en/api/files-create",
            "/en/api/files-list",
            "/en/api/files-metadata",
            "/en/api/files-content",
            "/en/api/files-delete",
            # Message Batches API
            "/en/api/creating-message-batches",
            "/en/api/listing-message-batches",
            "/en/api/retrieving-message-batches",
            "/en/api/retrieving-message-batch-results",
            "/en/api/canceling-message-batches",
            "/en/api/deleting-message-batches",
            # Prompt Tools API
            "/en/api/prompt-tools-generate",
            "/en/api/prompt-tools-improve",
            "/en/api/prompt-tools-templatize",
            # Skills API
            "/en/api/skills/create-skill",
            "/en/api/skills/list-skills",
            "/en/api/skills/get-skill",
            "/en/api/skills/delete-skill",
            "/en/api/skills/create-skill-version",
            "/en/api/skills/list-skill-versions",
            "/en/api/skills/get-skill-version",
            "/en/api/skills/delete-skill-version",
            # Admin API - Organization
            "/en/api/admin-api/organization/get-me",
            # Admin API - Users
            "/en/api/admin-api/users/list-users",
            "/en/api/admin-api/users/get-user",
            "/en/api/admin-api/users/update-user",
            "/en/api/admin-api/users/remove-user",
            # Admin API - API Keys
            "/en/api/admin-api/apikeys/list-api-keys",
            "/en/api/admin-api/apikeys/get-api-key",
            "/en/api/admin-api/apikeys/update-api-key",
            # Admin API - Invites
            "/en/api/admin-api/invites/create-invite",
            "/en/api/admin-api/invites/list-invites",
            "/en/api/admin-api/invites/get-invite",
            "/en/api/admin-api/invites/delete-invite",
            # Admin API - Workspaces
            "/en/api/admin-api/workspaces/create-workspace",
            "/en/api/admin-api/workspaces/list-workspaces",
            "/en/api/admin-api/workspaces/get-workspace",
            "/en/api/admin-api/workspaces/update-workspace",
            "/en/api/admin-api/workspaces/archive-workspace",
            # Admin API - Workspace Members
            "/en/api/admin-api/workspace_members/create-workspace-member",
            "/en/api/admin-api/workspace_members/list-workspace-members",
            "/en/api/admin-api/workspace_members/get-workspace-member",
            "/en/api/admin-api/workspace_members/update-workspace-member",
            "/en/api/admin-api/workspace_members/delete-workspace-member",
            # Admin API - Usage & Cost
            "/en/api/admin-api/usage-cost/get-cost-report",
            "/en/api/admin-api/usage-cost/get-messages-usage-report",
            "/en/api/admin-api/claude-code/get-claude-code-usage-report",
        ]

def url_to_filename(path: str) -> str:
    """Convert URL path to safe filename."""
    # Remove /en/api/ prefix
    if path.startswith('/en/api/'):
        path = path[8:]  # Remove '/en/api/'

    # Remove leading/trailing slashes
    path = path.strip('/')

    # Replace remaining slashes with double underscores
    filename = path.replace('/', '__')

    # If empty, use index
    if not filename:
        filename = "index"

    return f"{filename}.md"

def fetch_api_page(path: str) -> str:
    """Fetch API documentation page as markdown."""
    url = f"https://docs.claude.com{path}.md"
    logger.info(f"Fetching: {url}")

    try:
        response = requests.get(url, headers=HEADERS, timeout=30)
        response.raise_for_status()

        content = response.text

        # Add source footer
        footer = f"\n\n---\n📖 **Source:** https://docs.claude.com{path}\n*This is a mirror of the Claude API documentation for local access and AI-assisted development.*\n"

        return content + footer

    except Exception as e:
        logger.error(f"Failed to fetch {path}: {e}")
        return None

def calculate_hash(content: str) -> str:
    """Calculate SHA256 hash of content."""
    return hashlib.sha256(content.encode('utf-8')).hexdigest()

def main():
    """Main fetcher function."""
    logger.info("Starting API documentation fetch...")

    # Create output directory
    BASE_DIR.mkdir(exist_ok=True)

    # Discover API pages
    api_pages = discover_api_pages()

    if not api_pages:
        logger.error("No API pages discovered!")
        return 1

    # Fetch each page
    successful = 0
    failed = 0
    files_data = {}

    for path in api_pages:
        filename = url_to_filename(path)
        filepath = BASE_DIR / filename

        # Fetch content
        content = fetch_api_page(path)

        if content:
            # Write to file
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)

            # Store metadata
            files_data[filename] = {
                "original_url": f"https://docs.claude.com{path}",
                "hash": calculate_hash(content),
                "last_updated": datetime.now().isoformat(),
                "path": path
            }

            successful += 1
            logger.info(f"✓ Saved: {filename}")
        else:
            failed += 1
            logger.warning(f"✗ Failed: {path}")

        # Rate limiting
        time.sleep(RATE_LIMIT_DELAY)

    # Create manifest
    manifest = {
        "files": files_data,
        "fetch_metadata": {
            "last_fetch_completed": datetime.now().isoformat(),
            "total_pages_discovered": len(api_pages),
            "pages_fetched_successfully": successful,
            "pages_failed": failed,
            "source": "docs.claude.com/en/api"
        }
    }

    manifest_path = BASE_DIR / "api_manifest.json"
    with open(manifest_path, 'w', encoding='utf-8') as f:
        f.write(json.dumps(manifest, indent=2))

    logger.info(f"\n✓ Fetch complete!")
    logger.info(f"  Successful: {successful}")
    logger.info(f"  Failed: {failed}")
    logger.info(f"  Manifest: {manifest_path}")

    return 0 if failed == 0 else 1

if __name__ == "__main__":
    exit(main())
