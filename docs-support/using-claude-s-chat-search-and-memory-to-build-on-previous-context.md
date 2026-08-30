# Use Claude’s chat search and memory to build on previous context

*Updated this week*

---

You can prompt Claude to search through your previous conversations to find and reference relevant information in new chats. Claude can also remember context from your chats and carry it into new conversations and Cowork tasks. This article explains how chat search and memory work, what Claude does and doesn't remember, how to review and edit what's saved, and how to turn these features on or off.

 

---

 

## Search past chats with Claude

You can prompt Claude to search through your previous conversations to find relevant information across sessions and reference specific details when needed. Simply ask Claude to find what you discussed before, and it will pull together the appropriate context to keep your conversation flowing. These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations.

 

## What Claude can search

You can prompt Claude to search conversations within these boundaries:

- All chats outside of projects.
- Individual project conversations (searches are limited to within each specific project).

 

## Search and reference past chats

Once the ability to search past chats is rolled out to your account, it will be enabled by default. Just ask Claude about your previous conversations naturally to use it, such as:

- "What did we discuss about [topic]?"
- "Can you find our conversation about [subject]?"
- "Let's continue where we left off with [project]."

When Claude searches your previous chats, you will see this reflected in your current chat as a tool call.

 

## Can I prevent Claude from searching my past chats?

Yes, navigate to **[Settings > Memory](https://claude.ai/new#settings/customize-memory)** and switch the toggle next to "Search and reference chats" off:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2533482439/4dee2d7b267f865205feefc8f4f3/cb60c334-d1e2-4828-a01d-dfb36bbaa7eb?expires=1788115500&signature=825f341a634e7bc896948ef535b0b796e7d570309e248da798dd9eed52ba49df&req=diUkFc12n4VcUPMW1HO4zY9IRAJtVNRyYNcz5nFaZkHYaPrU3E9qkZy9J8ZY%0AlU8VcZlwMQE3GvbXAhg%3D%0A)

 

 

## Can I exclude a specific past chat from searches?

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen. 

 

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

 

---

 

## What is Claude's memory?

Claude can generate memory based on your chats. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

## How does Claude’s memory work?

In addition to searching past chats, enabling Claude's memory feature adds several capabilities.

 

### How Claude stores memory 

Claude saves memory as a set of individual topics as you chat, rather than summarizing conversations after they end. Mention that a deadline moved, and your next conversation already knows. Claude saves on its own, and you can also tell Claude to "remember this" to save something directly.

 

### Project memory and summary

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

 

### One memory across chat and Claude Cowork

What Claude remembers from your chats is available when you hand it a task in Cowork in the cloud, and what comes up in a Cowork task carries back to chat. For example, ask Cowork to draft an update for your manager, and it already knows who that is and how they like updates written.

## Turn memory on or off

You can toggle Claude’s memory on by navigating to **[Settings > Memory](https://claude.ai/new#settings/customize-memory)** and turning on **Generate memory from chats**:

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2533482441/b5c806a8e3f68bf34c4a70724d38/d30be013-d099-4c93-99d1-23d404792f08?expires=1788115500&signature=810ef26843ce1a09583b6f881e4f9e52c533d74874e26ad16538ea038b1d543c&req=diUkFc12n4VbWPMW1HO4zRlYrpNs41UpNshWSMEMw9ey2DdqMXGSTtCQT8Jz%0AMq7R8RHToYidpIMX2f0%3D%0A)

 

If you want to disable Claude’s memory, click the toggle and you'll see two options:

- **Pause memory:** Claude keeps its existing memory, including sensitive topics if you have it turned on, but won't use memory or make new memories. Conversations while memory is paused won't be added to memory if you turn it back on.  If you unpause memory, both your memory and sensitive topics memory will be on.
- **Reset memory:** Permanently deletes all memories including project memories. Once you select this option and click "Reset memory," this cannot be undone. Upon re-enabling the feature, you’ll start from scratch and Claude will not have its previous memory.

 

## What Claude remembers

Claude remembers the everyday context that helps it work with you, such as:

- Your role, projects, and professional context
- The people and places in your work and life
- Communication preferences and working style
- Technical preferences and coding style
- Project details and ongoing work

​We apply safeguards and conduct evaluations to memory to help keep users safe.

 

### Sensitive topics in memory

By default, Claude does not store topics related to personal or sensitive subject matter, like your health, race, ethnicity, religious beliefs, politics, gender identity, and other similar areas.

 

If these are topics you'd rather not keep re-explaining, you can choose to include them. Turn on **Include sensitive topics in memory** in **[Settings > Memory](https://claude.ai/new#settings/customize-memory)**. You can also turn it on from the one-time notice Claude shows in chat the first time it declines to save a memory because it referenced a sensitive topic.

 

Once the setting is on:

- Claude saves sensitive topics going forward. Anything from before you turned it on isn't saved retroactively.
- Each time Claude saves something on one of these topics, a notice appears above the message box so you can review it or update your settings.
- - If you’re using Claude for iOS or Android, this notice will only appear if you’re on the latest version of the mobile app. If you’re using an older version or the mobile app, you will not see this notice, and Claude won't save the sensitive topic to its memory.

If you decline the notice, or turn the setting off later, Claude removes any sensitive items already saved to memory.

## What Claude doesn't remember

### Incognito chats

When starting a chat with Claude outside of a project, you will see a ghost icon in the upper right corner of your screen; clicking this enables incognito chats. When this mode is switched on, Claude won’t remember your chats, so they won’t be saved to Claude’s memory or your chat history. Close your current incognito chat when you’re ready for Claude to start remembering your conversations again.

 

---

 

## Data retention and privacy

All memory will be retained in accordance with existing chat data retention policies.

- Claude’s memory reflects changes to your conversations as they happen. 
- When a conversation expires or is deleted, related memory entries generated from it won’t be removed, but you can delete individual memories at any time.
- All memory data is included in data exports.
- Enterprise data retention policies apply to all memory-related data, including incognito chats.<br>​

---

 

## User controls and visibility

You have several mechanisms for managing and overseeing Claude's memory.

 

### View and manage your memory 

See exactly what Claude remembers about you in **[Settings > Memory](https://claude.ai/new#settings/customize-memory)**. Everything Claude remembers is listed under **Topics**. Select any topic to read it, then use the edit icon to change it or select "Delete" to remove it. Fix something in one topic and the change applies to every conversation from then on.

 

You can also update memory directly from a chat. Tell Claude what you'd like it to remember, change, or forget, and the update applies to your next conversation.

 

### Past chat citations

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

 

### Toggle search past chats and memory on/off

You maintain control over Claude’s ability to search past chats and use memory–you can always disable these features and enable them again when needed in **[Settings > Memory](https://claude.ai/new#settings/customize-memory).**

 

### Importing your memory from other AI tools

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

---

## Controls for Team and Enterprise plan owners

Memory and sensitive topics are two separate controls for your organization, and both are off by default.

 

### Organization-level memory controls

Owners and Primary Owners can turn memory on for the organization in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**. Once enabled, individual users manage their own memory settings. Enabling memory doesn't enable sensitive topics, and even if you allow sensitive topics for your organization, nothing in those categories is saved until each user opts in themselves. Once a user has opted in, they control their own sensitive memories: they can view and delete individual entries, or turn sensitive topics off to stop saving new ones. Owners can't view or edit a user’s individual memories.

 

When an owner turns memory off for the organization, all existing memory entries for all users are deleted immediately, and users can't access the memory setting.

Memory isn't available to organizations with HIPAA, public-sector, or custom data retention agreements.

 

### Data handling and compliance

- **Memory entries** are stored with encryption at rest. When a conversation expires or is deleted, related memory entries aren't removed, but members can delete individual memories at any time.
- **Incognito chats** don't contribute to memory and aren't visible in members' chat histories, but they remain available to owners through data export and are subject to your data retention policies (retained for at least 30 days for safety purposes).
-  

### Audit logging and data exports

- **Audit logging:** The system logs when owners turn org-level memory controls on or off. Standard conversation access logging applies to memory entries. Individual member memory edits aren't logged.
- **Data exports:** Memory entries are included in standard conversation history exports. Incognito chats are included in organizational data exports.

 

---

 

## Information for legacy memory users

### Search past chats with Claude

You can prompt Claude to search through your previous conversations to find relevant information across sessions and reference specific details when needed. Simply ask Claude to find what you discussed before, and it will pull together the appropriate context to keep your conversation flowing. These searches use Retrieval-Augmented Generation (RAG) and will appear as tool calls during your conversations.

 

### What Claude can search

You can prompt Claude to search conversations within these boundaries:

- All chats outside of projects.
- Individual project conversations (searches are limited to within each specific project).
-  

### Search and reference past chats

Once the ability to search past chats is rolled out to your account, it will be enabled by default. Just ask Claude about your previous conversations naturally to use it, such as:

- "What did we discuss about [topic]?"
- "Can you find our conversation about [subject]?"
- "Let's continue where we left off with [project]."

When Claude searches your previous chats, you will see this reflected in your current chat as a tool call.

 

### Can I prevent Claude from searching my past chats?

Yes, navigate to **[Settings > Capabilities](https://claude.ai/settings/capabilities)** and find the **Preferences** section. Switch the toggle next to “Search and reference chats” off:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730889/3fafbf5ecaa0ae31d7d84a66229b/c25536c1-7433-4b94-a5e9-cd5acf97a4fd?expires=1788115500&signature=d1bc52a4bf2992e946f21e5a977d423f4d46f85fc2a5c3119255746052125e42&req=dScmH859nYlXUPMW1HO4zRzXH1cxIjTHJG68qZhl782%2FSiB9HaVuWUuq3ojF%0A3DE%2Bh8q%2BiPnbRfo3iwE%3D%0A)

 

### Can I exclude a specific past chat from searches?

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730893/9549b21954e0070ceb6b85231fd5/88e59234-6fc2-4229-84fe-733b33efff26?expires=1788115500&signature=ab0f4a62fc1645bbc591c8e8d226f5e0a454ef91c095b1bfe5e02e8b6ffd5655&req=dScmH859nYlWWvMW1HO4za54sKttPYO%2BXDpzhlKsgjPMd%2F0Ekv7Wd%2BPbCTPb%0ABOfgMFIVp67mF6sFMJo%3D%0A)

 

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

 

---

 

### What is Claude's memory?

Claude can now generate memory based on your chat history. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

 

### How does Claude’s memory work?

In addition to searching past chats, enabling Claude’s memory feature adds several capabilities.

 

**Memory summary**

Claude will automatically summarize your conversations and create a synthesis of key insights across your chat history (not including chats in projects). This synthesis is updated every 24 hours and provides context for every new standalone conversation.

 

**Project memory and summary**

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

 

### Enable Claude’s memory

You can toggle Claude’s memory on by navigating to **[Settings > Capabilities](https://claude.ai/settings/capabilities)**:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730892/62f9f2b68d675a8e33393f06024f/89198978-192f-4c52-915d-5294b16f3fe1?expires=1788115500&signature=2d524fa16c2203bc99dc2041940e8ba30fed49926f17af4b9d3392e9b52c35ef&req=dScmH859nYlWW%2FMW1HO4zTD5MMnnduFABq9N9dRTKYeYdxtrnyB76tsl7xLH%0AqFYoEYIJSQILwBSWJ74%3D%0A)

 

If you want to disable Claude’s memory, click the toggle to see two options:

- **Pause memory:** Claude keeps its existing memory but won’t use memory or make new memories. Conversations with Claude while memory is paused will not be summarized into its memory should you turn the feature back on.
- **Reset memory:** Permanently deletes all memories including project memories. Once you select this option and click “Reset memory,” this cannot be undone. Upon re-enabling the feature, you’ll start from scratch and Claude will not have its previous memory.

 

### What does Claude remember?

Claude focuses on work-related context that helps improve collaboration. You will see this information reflected in your memory or project summary:

- Your role, projects, and professional context
- Communication preferences and working style
- Technical preferences and coding style
- Project details and ongoing work
-  

### What Claude doesn't remember

**Incognito chats**

When starting a chat with Claude outside of a project, you will see a ghost icon in the upper right corner of your screen; clicking this enables incognito chats. When this mode is switched on, Claude won’t remember your chats, so they won’t be saved to Claude’s memory or your chat history. Close your current incognito chat when you’re ready for Claude to start remembering your conversations again.

 

---

 

### Data retention and privacy

All memory will be retained in accordance with existing chat data retention policies.

- Deleted conversations are removed from memory synthesis.
- Claude’s memory is updated within 24 hours when conversations are created, modified, or deleted.
- All memory data is included in data exports.
- Enterprise data retention policies apply to all memory-related data, including incognito chats.
-  

---

 

### User controls and visibility

You have several mechanisms for managing and overseeing Claude's memory.

 

**View and manage your memory summary**

See exactly what Claude remembers about you by navigating to **[Settings > Capabilities](https://claude.ai/settings/capabilities)** and clicking “View and edit memory.” The **Manage memory** modal displays everything Claude remembers about you. In addition to asking Claude to edit the existing summary, you can also tell Claude what you want it to remember. To add custom instructions to Claude’s memory, click the pencil icon in the lower left corner of the summary.

 

You can also update your memory summary directly from your chats. Simply tell Claude what you'd like it to remember, and it will update your memory summary without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation, so you don’t need to wait for the daily synthesis to run.

 

**Past chat citations**

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

 

**Toggle search past chats and memory on/off**

You maintain control over Claude’s ability to search past chats and use memory – you can always disable these features and enable them again when needed in **[Settings > Capabilities](https://claude.ai/settings/capabilities)**.

 

**Importing your memory from other AI tools**

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

 

---

 

### Controls for Enterprise plan owners

Enterprise plan Owners and Primary Owners have specific controls for managing memory features across their organization.

 

**Organization-level memory controls**

The organization-wide **Generate memory from chat history** toggle is enabled by default. When enabled, individual users can manage their own memory settings. Owners can disable the memory summary feature for their entire organization by navigating to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**. When disabled by an Owner, it immediately deletes all existing memory synthesis data for all users, and individual users cannot modify or access the memory synthesis setting.

**Data handling and compliance**

- **Chat summaries** are stored alongside conversation data and follow your organization's existing data retention policies. When a conversation is deleted, its summary is also deleted.
- **Memory synthesis** is stored with encryption at rest and is tied to underlying conversations. As conversations expire or are deleted according to your retention settings, the synthesis updates accordingly.
- **Incognito chats** don't contribute to memory and aren't visible in users' chat histories, but they remain available to Owners through data export features and are subject to your existing data retention policies (retained for at least 30 days for safety purposes).
-  

**Audit logging and data exports**

- **Audit logging:** The system logs when org-level memory toggles are enabled or disabled by Owners. Standard conversation access logging applies to memory synthesis. Individual user memory edits are not logged.
- **Data exports:** Memory synthesis and chat summaries are included in standard conversation history exports. Incognito chats are included in organizational data exports. All exported chat summaries remain tied to their source conversations.

 

**Team plan limitations**

Team plans do not have organization-level controls for memory features. Individual Team plan members manage their own memory settings directly.


---

## Related Articles

- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- [Get started with Claude Cowork](https://support.claude.com/en/articles/13345190-get-started-with-claude-cowork)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
- [Use analytics chat to ask Claude about usage](https://support.claude.com/en/articles/14729354-use-analytics-chat-to-ask-claude-about-usage)
