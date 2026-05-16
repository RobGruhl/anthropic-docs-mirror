#!/usr/bin/env python3
"""
Generate documentation indexes from manifest files.
Creates both content-type indexes (source of truth) and topic indexes (references).
"""

import json
from pathlib import Path
from datetime import datetime
from typing import Dict, List, Set
from collections import defaultdict

# Configuration
MAX_TOPIC_INDEX_SIZE = 50  # Max documents per topic before splitting
INDEXES_DIR_NAME = 'indexes'
TOPICS_DIR_NAME = 'topics'

# Important topics to detect from filenames and paths
# Maps filename/path patterns to topic names
# Note: These patterns match within filenames/paths, so be specific to avoid false positives
TOPIC_PATTERNS = {
    # MCP-related (be specific to avoid matching unrelated "connectors")
    'mcp': 'mcp',
    'model-context-protocol': 'mcp',
    'remote-mcp': 'mcp',
    'mcp-connector': 'mcp',
    'mcp-server': 'mcp',
    'connectors-directory': 'mcp',  # More specific than just 'connectors'
    'web-connectors': 'mcp',
    'custom-connectors': 'mcp',
    # Skills (unified topic for "Agent Skills" feature - includes API, SDK, and user docs)
    # All skills-related content goes to single 'skills' topic
    'agent-skills': 'skills',
    'agent_skills': 'skills',
    # Agent SDK
    'agent-sdk': 'agent-sdk',
    # Tools
    'tool-use': 'tool-use',
    'bash-tool': 'tool-use',
    'text-editor-tool': 'tool-use',
    'code-execution-tool': 'tool-use',
    'computer-tool': 'tool-use',
    # Claude Code
    'claude-code': 'claude-code',
    # Agents
    'agents-and-tools': 'agents',
    # Prompt engineering
    'prompt-engineering': 'prompt-engineering',
    # Models - be specific
    'about-claude__models': 'models',
    # API - handled by manifest categories
}

# Filename patterns that indicate specific topics (for platform-docs and code-claude-docs)
FILENAME_TOPIC_MAPPINGS = {
    # Files containing these patterns get added to these topics
    # Platform docs - Skills API (beta__skills* files)
    'beta__skills': ['skills', 'api'],
    # Platform docs - Agent SDK
    'agent-sdk__': ['agent-sdk'],
    'agent-sdk__mcp': ['agent-sdk', 'mcp'],
    'agent-sdk__skills': ['agent-sdk', 'skills'],
    # Platform docs - Agents and tools (agent-skills docs → unified 'skills' topic)
    'agents-and-tools__agent-skills': ['skills', 'agents'],
    'agents-and-tools__mcp': ['mcp', 'agents'],
    'agents-and-tools__remote-mcp': ['mcp', 'agents'],
    'agents-and-tools__tool-use': ['tool-use', 'agents'],
    # Claude Code docs
    'skills.md': ['skills', 'claude-code'],  # code-claude-docs/skills.md
    'plugins': ['plugins', 'claude-code'],
    'mcp.md': ['mcp'],
}


def load_manifests(base_dir: Path) -> Dict[str, Dict]:
    """Load all manifest files from the various documentation sources."""
    manifests = {}

    # Load platform docs manifest (NEW - replaces docs/ and api-docs/)
    platform_manifest_path = base_dir / 'platform-docs' / 'platform_manifest.json'
    if platform_manifest_path.exists():
        with open(platform_manifest_path, 'r', encoding='utf-8') as f:
            manifests['platform-docs'] = json.load(f)
            print(f"Loaded platform docs: {len(manifests['platform-docs']['files'])} files")
    else:
        print(f"Note: Platform docs manifest not found: {platform_manifest_path}")
        manifests['platform-docs'] = {"files": {}}

    # Load code.claude.com docs manifest
    code_claude_manifest_path = base_dir / 'code-claude-docs' / 'code_claude_manifest.json'
    if code_claude_manifest_path.exists():
        with open(code_claude_manifest_path, 'r', encoding='utf-8') as f:
            manifests['code-claude-docs'] = json.load(f)
            print(f"Loaded Claude Code docs: {len(manifests['code-claude-docs']['files'])} files")
    else:
        print(f"Warning: Claude Code docs manifest not found: {code_claude_manifest_path}")
        manifests['code-claude-docs'] = {"files": {}}

    # Load engineering blog manifest
    engineering_blog_manifest_path = base_dir / 'engineering-blog' / 'blog_manifest.json'
    if engineering_blog_manifest_path.exists():
        with open(engineering_blog_manifest_path, 'r', encoding='utf-8') as f:
            manifests['engineering-blog'] = json.load(f)
            print(f"Loaded engineering blog: {len(manifests['engineering-blog']['files'])} files")
    else:
        print(f"Warning: Engineering blog manifest not found: {engineering_blog_manifest_path}")
        manifests['engineering-blog'] = {"files": {}}

    # Load claude-blog manifest
    claude_blog_manifest_path = base_dir / 'claude-blog' / 'claude_blog_manifest.json'
    if claude_blog_manifest_path.exists():
        with open(claude_blog_manifest_path, 'r', encoding='utf-8') as f:
            manifests['claude-blog'] = json.load(f)
            print(f"Loaded Claude.com blog: {len(manifests['claude-blog']['files'])} files")
    else:
        print(f"Warning: Claude.com blog manifest not found: {claude_blog_manifest_path}")
        manifests['claude-blog'] = {"files": {}}

    # Load support docs manifest
    support_manifest_path = base_dir / 'docs-support' / 'support_manifest.json'
    if support_manifest_path.exists():
        with open(support_manifest_path, 'r', encoding='utf-8') as f:
            manifests['support'] = json.load(f)
            print(f"Loaded support articles: {len(manifests['support']['files'])} files")
    else:
        print(f"Warning: Support manifest not found: {support_manifest_path}")
        manifests['support'] = {"files": {}}

    # Load anthropic research manifest
    research_manifest_path = base_dir / 'anthropic-research' / 'research_manifest.json'
    if research_manifest_path.exists():
        with open(research_manifest_path, 'r', encoding='utf-8') as f:
            manifests['anthropic-research'] = json.load(f)
            print(f"Loaded Anthropic research: {len(manifests['anthropic-research']['files'])} files")
    else:
        print(f"Note: Anthropic research manifest not found: {research_manifest_path}")
        manifests['anthropic-research'] = {"files": {}}

    # Load anthropic news manifest
    news_manifest_path = base_dir / 'anthropic-news' / 'news_manifest.json'
    if news_manifest_path.exists():
        with open(news_manifest_path, 'r', encoding='utf-8') as f:
            manifests['anthropic-news'] = json.load(f)
            print(f"Loaded Anthropic news: {len(manifests['anthropic-news']['files'])} files")
    else:
        print(f"Note: Anthropic news manifest not found: {news_manifest_path}")
        manifests['anthropic-news'] = {"files": {}}

    # Load MCP docs manifest
    mcp_docs_manifest_path = base_dir / 'mcp-docs' / 'mcp_docs_manifest.json'
    if mcp_docs_manifest_path.exists():
        with open(mcp_docs_manifest_path, 'r', encoding='utf-8') as f:
            manifests['mcp-docs'] = json.load(f)
            print(f"Loaded MCP docs: {len(manifests['mcp-docs']['files'])} files")
    else:
        print(f"Note: MCP docs manifest not found: {mcp_docs_manifest_path}")
        manifests['mcp-docs'] = {"files": {}}

    # Load MCP blog manifest
    mcp_blog_manifest_path = base_dir / 'mcp-blog' / 'mcp_blog_manifest.json'
    if mcp_blog_manifest_path.exists():
        with open(mcp_blog_manifest_path, 'r', encoding='utf-8') as f:
            manifests['mcp-blog'] = json.load(f)
            print(f"Loaded MCP blog: {len(manifests['mcp-blog']['files'])} files")
    else:
        print(f"Note: MCP blog manifest not found: {mcp_blog_manifest_path}")
        manifests['mcp-blog'] = {"files": {}}

    # Load AgentSkills docs manifest
    agentskills_manifest_path = base_dir / 'agentskills-docs' / 'agentskills_manifest.json'
    if agentskills_manifest_path.exists():
        with open(agentskills_manifest_path, 'r', encoding='utf-8') as f:
            manifests['agentskills-docs'] = json.load(f)
            print(f"Loaded AgentSkills docs: {len(manifests['agentskills-docs']['files'])} files")
    else:
        print(f"Note: AgentSkills docs manifest not found: {agentskills_manifest_path}")
        manifests['agentskills-docs'] = {"files": {}}

    # Legacy: Load old docs manifest if it still exists (for migration period)
    docs_manifest_path = base_dir / 'docs' / 'docs_manifest.json'
    if docs_manifest_path.exists() and not manifests['platform-docs'].get('files'):
        with open(docs_manifest_path, 'r', encoding='utf-8') as f:
            manifests['docs'] = json.load(f)
            print(f"Loaded legacy developer docs: {len(manifests['docs']['files'])} files")
    else:
        manifests['docs'] = {"files": {}}

    # Legacy: Load old api-docs manifest if it still exists
    api_manifest_path = base_dir / 'api-docs' / 'api_manifest.json'
    if api_manifest_path.exists() and not manifests['platform-docs'].get('files'):
        with open(api_manifest_path, 'r', encoding='utf-8') as f:
            manifests['api-docs'] = json.load(f)
            print(f"Loaded legacy API reference: {len(manifests['api-docs']['files'])} files")
    else:
        manifests['api-docs'] = {"files": {}}

    return manifests


def generate_content_type_index(manifest: Dict, content_type: str, dir_prefix: str, base_dir: Path) -> str:
    """Generate a content-type index (source of truth) with full details."""
    lines = []

    # Header
    type_labels = {
        'platform-docs': 'Platform Documentation (platform.claude.com)',
        'docs': 'Developer Documentation',
        'code-claude-docs': 'Claude Code Documentation',
        'api-docs': 'API Reference',
        'engineering-blog': 'Engineering Blog Posts',
        'claude-blog': 'Claude.com Blog Posts',
        'support': 'Support Articles',
        'anthropic-research': 'Anthropic Research Papers',
        'anthropic-news': 'Anthropic News & Announcements',
        'mcp-docs': 'MCP Documentation (modelcontextprotocol.io)',
        'mcp-blog': 'MCP Blog Posts',
        'agentskills-docs': 'AgentSkills Documentation (agentskills.io)'
    }
    title = type_labels.get(content_type, content_type.title())
    lines.append(f"# {title} Index\n")
    lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    lines.append(f"Total documents: {len(manifest['files'])}\n")
    lines.append("---\n")

    # Group files by primary category
    categorized = defaultdict(list)
    for filename, file_info in sorted(manifest['files'].items()):
        categories = file_info.get('categories', ['uncategorized'])
        primary_category = categories[0] if categories else 'uncategorized'
        categorized[primary_category].append((filename, file_info))

    # Generate sections by category
    for category in sorted(categorized.keys()):
        files = categorized[category]
        lines.append(f"## {category.replace('-', ' ').title()} ({len(files)} documents)\n")

        for filename, file_info in sorted(files, key=lambda x: x[1].get('title', x[0])):
            title = file_info.get('title', filename.replace('.md', ''))
            original_url = file_info.get('original_url', '')
            last_updated = file_info.get('last_updated', 'Unknown')
            categories_list = file_info.get('categories', [])
            keywords_list = file_info.get('keywords', [])
            summary = file_info.get('summary', '')

            # Format last updated date
            if 'T' in last_updated:
                try:
                    dt = datetime.fromisoformat(last_updated.replace('Z', '+00:00'))
                    last_updated = dt.strftime('%Y-%m-%d')
                except:
                    pass

            lines.append(f"### {title}\n")
            lines.append(f"**File:** `/{dir_prefix}/{filename}`  \n")
            lines.append(f"**Source:** {original_url}  \n")
            lines.append(f"**Updated:** {last_updated}  \n")

            if categories_list:
                lines.append(f"**Categories:** {', '.join(categories_list)}  \n")

            if keywords_list:
                keywords_str = ', '.join(keywords_list[:10])  # Limit to 10
                lines.append(f"**Keywords:** {keywords_str}  \n")

            if summary:
                # Truncate very long summaries
                if len(summary) > 250:
                    summary = summary[:247] + '...'
                lines.append(f"\n{summary}\n")

            lines.append("\n")

    return ''.join(lines)


def generate_topic_index(topic: str, documents: List[tuple], base_dir: Path) -> str:
    """Generate a topic index (lightweight references)."""
    lines = []

    # Header
    topic_title = topic.replace('-', ' ').title()
    lines.append(f"# {topic_title} Topic Index\n")
    lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    lines.append(f"\nDocuments related to {topic_title} across all sources ({len(documents)} documents)\n")
    lines.append("---\n")

    # Group by source
    by_source = defaultdict(list)
    for filename, file_info, source_type, dir_prefix in documents:
        by_source[source_type].append((filename, file_info, dir_prefix))

    # Source labels and order
    source_order = ['platform-docs', 'code-claude-docs', 'mcp-docs', 'agentskills-docs', 'docs', 'api-docs', 'anthropic-research', 'anthropic-news', 'mcp-blog', 'engineering-blog', 'claude-blog', 'support']
    source_labels = {
        'platform-docs': 'Platform Documentation (platform.claude.com)',
        'code-claude-docs': 'Claude Code Documentation',
        'mcp-docs': 'MCP Documentation (modelcontextprotocol.io)',
        'agentskills-docs': 'AgentSkills Documentation (agentskills.io)',
        'docs': 'Developer Documentation (legacy)',
        'api-docs': 'API Reference (legacy)',
        'anthropic-research': 'Anthropic Research Papers',
        'anthropic-news': 'Anthropic News & Announcements',
        'mcp-blog': 'MCP Blog Posts',
        'engineering-blog': 'Engineering Blog Posts',
        'claude-blog': 'Claude.com Blog Posts',
        'support': 'Support Articles'
    }

    for source_type in source_order:
        if source_type not in by_source:
            continue

        files = by_source[source_type]
        lines.append(f"## {source_labels[source_type]} ({len(files)})\n")

        for filename, file_info, dir_prefix in sorted(files, key=lambda x: x[1].get('title', x[0])):
            title = file_info.get('title', filename.replace('.md', ''))
            summary = file_info.get('summary', '')

            # Create a one-line description
            if summary:
                # Take first sentence or first 80 chars
                desc = summary.split('.')[0].split('\n')[0]
                if len(desc) > 80:
                    desc = desc[:77] + '...'
            else:
                desc = ""

            # Format as bullet point with link
            lines.append(f"- [{title}](/{dir_prefix}/{filename})")
            if desc:
                lines.append(f" - {desc}")
            lines.append("\n")

        lines.append("\n")

    return ''.join(lines)


def derive_topics_from_filename(filename: str, file_info: Dict, source_type: str = '') -> Set[str]:
    """
    Derive topic categories from filename patterns and URL paths.
    This helps include documents in topic indexes even when they don't have
    explicit category tags in the manifest.
    """
    topics = set()

    # Normalize filename for matching (lowercase, without .md)
    normalized = filename.lower().replace('.md', '')

    # Check explicit filename mappings first (most specific)
    for pattern, topic_list in FILENAME_TOPIC_MAPPINGS.items():
        if pattern in normalized:
            topics.update(topic_list)

    # Check general topic patterns in filename
    for pattern, topic in TOPIC_PATTERNS.items():
        if pattern in normalized:
            topics.add(topic)

    # Also check the URL path if available
    url_path = file_info.get('path', '') or file_info.get('original_url', '')
    if url_path:
        url_lower = url_path.lower()
        for pattern, topic in TOPIC_PATTERNS.items():
            if pattern in url_lower:
                topics.add(topic)

    # Check title for topic keywords
    title = file_info.get('title', '').lower()
    for pattern, topic in TOPIC_PATTERNS.items():
        if pattern in title:
            topics.add(topic)

    # Source-based topic assignment
    # All code-claude-docs should be in the claude-code topic
    if source_type == 'code-claude-docs':
        topics.add('claude-code')

    # All mcp-docs and mcp-blog should be in the mcp topic
    if source_type in ('mcp-docs', 'mcp-blog'):
        topics.add('mcp')

    # All agentskills-docs should be in the skills topic
    if source_type == 'agentskills-docs':
        topics.add('skills')

    return topics


def collect_all_topics(manifests: Dict) -> Dict[str, List[tuple]]:
    """Collect all documents organized by topic."""
    topics = defaultdict(list)

    # Directory prefixes for each source
    # For platform-docs and mcp-docs, we include the category subdirectory
    dir_prefixes = {
        'platform-docs': 'platform-docs',  # Will be adjusted per file based on category
        'docs': 'docs',
        'code-claude-docs': 'code-claude-docs',
        'api-docs': 'api-docs',
        'engineering-blog': 'engineering-blog',
        'claude-blog': 'claude-blog',
        'support': 'docs-support',
        'anthropic-research': 'anthropic-research',
        'anthropic-news': 'anthropic-news',
        'mcp-docs': 'mcp-docs',  # Will be adjusted per file based on category
        'mcp-blog': 'mcp-blog',
        'agentskills-docs': 'agentskills-docs'
    }

    # Process each manifest
    for source_type, manifest in manifests.items():
        base_prefix = dir_prefixes.get(source_type, source_type)

        for filename, file_info in manifest.get('files', {}).items():
            # Get explicit categories from manifest
            categories = set(file_info.get('categories', []))

            # Derive additional topics from filename/path patterns
            derived_topics = derive_topics_from_filename(filename, file_info, source_type)

            # Combine both sources
            all_categories = categories | derived_topics

            # Normalize category names (unify synonyms and merge redundant topics)
            # This mapping consolidates related topics into canonical names
            CATEGORY_NORMALIZATION = {
                # Skills unification
                'agent-skills': 'skills',
                # Batch unification
                'batch-processing': 'batch',
                # Evaluation unification
                'test-and-evaluate': 'evaluation',
                # Tools unification - merge tool-use into tools
                'tool-use': 'tools',
                # Agents unification - agents-and-tools is a URL path, not a topic
                'agents-and-tools': 'agents',
                # Pricing unification
                'costs': 'pricing',
                'rate-limits': 'pricing',
                # computer-use and code-execution are specific tools
                'computer-use': 'tools',
                'code-execution': 'tools',
                # Guardrails is part of evaluation
                'guardrails': 'evaluation',
                # About-claude is too generic - use models or remove
                'about-claude': 'models',
                # build-with-claude is a URL path, not a semantic topic
                'build-with-claude': None,  # Skip - content goes to specific topics
            }

            normalized_categories = set()
            for cat in all_categories:
                normalized = CATEGORY_NORMALIZATION.get(cat, cat)
                if normalized is not None:  # Skip if mapped to None
                    normalized_categories.add(normalized)

            # For platform-docs and mcp-docs, adjust path to include category subdirectory
            if source_type == 'platform-docs':
                category_subdir = file_info.get('category', 'developer-guide')
                dir_prefix = f"{base_prefix}/{category_subdir}"
            elif source_type == 'mcp-docs':
                category_subdir = file_info.get('category', 'docs')
                dir_prefix = f"{base_prefix}/{category_subdir}"
            else:
                dir_prefix = base_prefix

            # Add this document to each of its category topics
            for category in normalized_categories:
                topics[category].append((filename, file_info, source_type, dir_prefix))

    return topics


def generate_master_readme(manifests: Dict, all_topics: Dict[str, List], base_dir: Path) -> str:
    """Generate the master README index."""
    lines = []

    # Header
    lines.append("# Claude Documentation Index\n")
    lines.append(f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*\n")
    lines.append("\n")

    # Quick stats
    total_docs = sum(len(m.get('files', {})) for m in manifests.values())
    platform_count = len(manifests.get('platform-docs', {}).get('files', {}))
    code_claude_count = len(manifests.get('code-claude-docs', {}).get('files', {}))
    mcp_docs_count = len(manifests.get('mcp-docs', {}).get('files', {}))
    mcp_blog_count = len(manifests.get('mcp-blog', {}).get('files', {}))
    agentskills_count = len(manifests.get('agentskills-docs', {}).get('files', {}))

    research_count = len(manifests.get('anthropic-research', {}).get('files', {}))
    news_count = len(manifests.get('anthropic-news', {}).get('files', {}))

    lines.append("## Quick Stats\n")
    lines.append(f"- **Total Documents:** {total_docs}\n")
    lines.append(f"- **Platform Docs:** {platform_count}\n")
    lines.append(f"- **Claude Code Docs:** {code_claude_count}\n")
    lines.append(f"- **MCP Docs:** {mcp_docs_count}\n")
    lines.append(f"- **AgentSkills Docs:** {agentskills_count}\n")
    lines.append(f"- **Anthropic Research:** {research_count}\n")
    lines.append(f"- **Anthropic News:** {news_count}\n")
    lines.append(f"- **MCP Blog:** {mcp_blog_count}\n")
    lines.append(f"- **Engineering Blog:** {len(manifests.get('engineering-blog', {}).get('files', {}))}\n")
    lines.append(f"- **Claude.com Blog:** {len(manifests.get('claude-blog', {}).get('files', {}))}\n")
    lines.append(f"- **Support Articles:** {len(manifests.get('support', {}).get('files', {}))}\n")
    lines.append(f"- **Topics:** {len(all_topics)}\n")
    lines.append("\n")

    # Quick navigation
    lines.append("## Quick Navigation\n")
    lines.append("\n")

    lines.append("### By Content Type\n")
    lines.append(f"- [Platform Documentation](platform-docs.md) - {platform_count} docs from platform.claude.com\n")
    lines.append(f"- [Claude Code Documentation](code-claude-docs.md) - {code_claude_count} docs from code.claude.com\n")
    lines.append(f"- [MCP Documentation](mcp-docs.md) - {mcp_docs_count} docs from modelcontextprotocol.io\n")
    lines.append(f"- [AgentSkills Documentation](agentskills-docs.md) - {agentskills_count} docs from agentskills.io\n")
    lines.append(f"- [Anthropic Research](anthropic-research.md) - {research_count} research papers from anthropic.com/research\n")
    lines.append(f"- [Anthropic News](anthropic-news.md) - {news_count} news articles from anthropic.com/news\n")
    lines.append(f"- [MCP Blog](mcp-blog.md) - {mcp_blog_count} posts from blog.modelcontextprotocol.io\n")
    lines.append(f"- [Engineering Blog](engineering-blog.md) - {len(manifests.get('engineering-blog', {}).get('files', {}))} technical posts from anthropic.com/engineering\n")
    lines.append(f"- [Claude.com Blog](claude-blog.md) - {len(manifests.get('claude-blog', {}).get('files', {}))} product/API posts from claude.com/blog\n")
    lines.append(f"- [Support Articles](support-articles.md) - {len(manifests.get('support', {}).get('files', {}))} help articles from support.claude.com\n")
    lines.append("\n")

    lines.append("### By Topic\n")
    # List top topics by document count
    top_topics = sorted(all_topics.items(), key=lambda x: len(x[1]), reverse=True)[:20]
    for topic, docs in top_topics:
        topic_title = topic.replace('-', ' ').title()
        lines.append(f"- [{topic_title}]({TOPICS_DIR_NAME}/{topic}.md) - {len(docs)} documents\n")

    if len(all_topics) > 20:
        lines.append(f"- [View all {len(all_topics)} topics]({TOPICS_DIR_NAME}/)\n")

    lines.append("\n")

    # Usage guide
    lines.append("## How to Use This Index\n")
    lines.append("\n")
    lines.append("### Finding Documentation\n")
    lines.append("\n")
    lines.append("1. **Browse by content type** - Start with [Developer Documentation](developer-docs.md), [Engineering Blog](engineering-blog.md), or [Support Articles](support-articles.md) for comprehensive listings\n")
    lines.append("2. **Browse by topic** - Use topic indexes like [Agent SDK](topics/agent-sdk.md) or [Claude Code](topics/claude-code.md) to find related content across all sources\n")
    lines.append("3. **Search with grep** - Use command-line search across all indexes:\n")
    lines.append("   ```bash\n")
    lines.append("   # Search for a keyword\n")
    lines.append("   grep -r \"authentication\" indexes/\n")
    lines.append("   \n")
    lines.append("   # Search in a specific topic\n")
    lines.append("   grep -i \"custom tools\" indexes/topics/agent-sdk.md\n")
    lines.append("   ```\n")
    lines.append("\n")

    lines.append("### Understanding the Structure\n")
    lines.append("\n")
    lines.append("- **Content-type indexes** (developer-docs.md, etc.) - Full document details, source of truth\n")
    lines.append("- **Topic indexes** (topics/*.md) - Lightweight references linking to related documents\n")
    lines.append("- Each document appears fully in ONE content-type index\n")
    lines.append("- Documents may appear as references in MULTIPLE topic indexes\n")
    lines.append("\n")

    lines.append("## Auto-Updates\n")
    lines.append("\n")
    lines.append("This index system is automatically regenerated:\n")
    lines.append("- Developer docs update every 3 hours via GitHub Actions\n")
    lines.append("- Blog and support content fetched periodically\n")
    lines.append("- Indexes regenerated after each content update\n")
    lines.append("\n")

    lines.append("## Need Help?\n")
    lines.append("\n")
    lines.append("- Use the `/docs` command in Claude Code to search documentation\n")
    lines.append("- Check [Support Articles](support-articles.md) for FAQs and troubleshooting\n")
    lines.append("- See [Getting Started](topics/getting-started.md) for introductory content\n")

    return ''.join(lines)


def main():
    """Main function to generate all indexes."""
    base_dir = Path(__file__).parent.parent
    indexes_dir = base_dir / INDEXES_DIR_NAME
    topics_dir = indexes_dir / TOPICS_DIR_NAME

    print("=" * 60)
    print("Generating Claude Documentation Indexes")
    print("=" * 60)
    print()

    # Create directories
    indexes_dir.mkdir(exist_ok=True)
    topics_dir.mkdir(exist_ok=True)
    print(f"Indexes directory: {indexes_dir}")
    print()

    # Load manifests
    print("Loading manifests...")
    manifests = load_manifests(base_dir)
    print()

    # Generate content-type indexes
    print("Generating content-type indexes...")

    # Platform docs (NEW - primary source)
    if manifests.get('platform-docs', {}).get('files'):
        print("  - platform-docs.md")
        platform_index = generate_content_type_index(manifests['platform-docs'], 'platform-docs', 'platform-docs', base_dir)
        (indexes_dir / 'platform-docs.md').write_text(platform_index, encoding='utf-8')

    if manifests.get('code-claude-docs', {}).get('files'):
        print("  - code-claude-docs.md")
        code_claude_index = generate_content_type_index(manifests['code-claude-docs'], 'code-claude-docs', 'code-claude-docs', base_dir)
        (indexes_dir / 'code-claude-docs.md').write_text(code_claude_index, encoding='utf-8')

    # Legacy: Only generate if platform-docs doesn't exist yet
    if manifests.get('docs', {}).get('files') and not manifests.get('platform-docs', {}).get('files'):
        print("  - developer-docs.md (legacy)")
        dev_index = generate_content_type_index(manifests['docs'], 'docs', 'docs', base_dir)
        (indexes_dir / 'developer-docs.md').write_text(dev_index, encoding='utf-8')

    if manifests.get('api-docs', {}).get('files') and not manifests.get('platform-docs', {}).get('files'):
        print("  - api-docs.md (legacy)")
        api_index = generate_content_type_index(manifests['api-docs'], 'api-docs', 'api-docs', base_dir)
        (indexes_dir / 'api-docs.md').write_text(api_index, encoding='utf-8')

    if manifests.get('engineering-blog', {}).get('files'):
        print("  - engineering-blog.md")
        eng_blog_index = generate_content_type_index(manifests['engineering-blog'], 'engineering-blog', 'engineering-blog', base_dir)
        (indexes_dir / 'engineering-blog.md').write_text(eng_blog_index, encoding='utf-8')

    if manifests.get('claude-blog', {}).get('files'):
        print("  - claude-blog.md")
        claude_blog_index = generate_content_type_index(manifests['claude-blog'], 'claude-blog', 'claude-blog', base_dir)
        (indexes_dir / 'claude-blog.md').write_text(claude_blog_index, encoding='utf-8')

    if manifests.get('support', {}).get('files'):
        print("  - support-articles.md")
        support_index = generate_content_type_index(manifests['support'], 'support', 'docs-support', base_dir)
        (indexes_dir / 'support-articles.md').write_text(support_index, encoding='utf-8')

    if manifests.get('anthropic-research', {}).get('files'):
        print("  - anthropic-research.md")
        research_index = generate_content_type_index(manifests['anthropic-research'], 'anthropic-research', 'anthropic-research', base_dir)
        (indexes_dir / 'anthropic-research.md').write_text(research_index, encoding='utf-8')

    if manifests.get('anthropic-news', {}).get('files'):
        print("  - anthropic-news.md")
        news_index = generate_content_type_index(manifests['anthropic-news'], 'anthropic-news', 'anthropic-news', base_dir)
        (indexes_dir / 'anthropic-news.md').write_text(news_index, encoding='utf-8')

    if manifests.get('mcp-docs', {}).get('files'):
        print("  - mcp-docs.md")
        mcp_docs_index = generate_content_type_index(manifests['mcp-docs'], 'mcp-docs', 'mcp-docs', base_dir)
        (indexes_dir / 'mcp-docs.md').write_text(mcp_docs_index, encoding='utf-8')

    if manifests.get('mcp-blog', {}).get('files'):
        print("  - mcp-blog.md")
        mcp_blog_index = generate_content_type_index(manifests['mcp-blog'], 'mcp-blog', 'mcp-blog', base_dir)
        (indexes_dir / 'mcp-blog.md').write_text(mcp_blog_index, encoding='utf-8')

    if manifests.get('agentskills-docs', {}).get('files'):
        print("  - agentskills-docs.md")
        agentskills_index = generate_content_type_index(manifests['agentskills-docs'], 'agentskills-docs', 'agentskills-docs', base_dir)
        (indexes_dir / 'agentskills-docs.md').write_text(agentskills_index, encoding='utf-8')

    print()

    # Collect all topics
    print("Collecting topics...")
    all_topics = collect_all_topics(manifests)
    print(f"Found {len(all_topics)} unique topics")
    print()

    # Generate topic indexes
    print("Generating topic indexes...")
    for topic, documents in sorted(all_topics.items()):
        if len(documents) > 0:  # Only create index if there are documents
            topic_filename = f"{topic}.md"
            print(f"  - {TOPICS_DIR_NAME}/{topic_filename} ({len(documents)} docs)")
            topic_index = generate_topic_index(topic, documents, base_dir)
            (topics_dir / topic_filename).write_text(topic_index, encoding='utf-8')

    print()

    # Generate master README
    print("Generating master README...")
    master_readme = generate_master_readme(manifests, all_topics, base_dir)
    (indexes_dir / 'README.md').write_text(master_readme, encoding='utf-8')
    print("  - README.md")
    print()

    # Summary
    print("=" * 60)
    print("Index Generation Complete!")
    print("=" * 60)
    print(f"Content-type indexes: 3 files")
    print(f"Topic indexes: {len(all_topics)} files")
    print(f"Total documents indexed: {sum(len(m.get('files', {})) for m in manifests.values())}")
    print(f"\nIndexes location: {indexes_dir}")
    print(f"View master index: {indexes_dir / 'README.md'}")


if __name__ == '__main__':
    main()
