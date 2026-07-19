# Use Claude’s chat search and memory to build on previous context

*Updated this week*

---

You can now prompt Claude to search through your previous conversations to find and reference relevant information in new chats. Additionally, Claude can remember context from previous chats, creating continuity across your conversations. This article introduces Claude’s chat search and memory capabilities and explains how they work, what Claude can and can’t remember, and how you can toggle the features on/off.

 

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

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2533482439/4dee2d7b267f865205feefc8f4f3/cb60c334-d1e2-4828-a01d-dfb36bbaa7eb?expires=1784458800&signature=d9a4b27cb76a88c9aafb2cada9689ac1c95ab162792dfdea218fc0071ec41237&req=diUkFc12n4VcUPMW1HO4zY9IRA5oUNl%2FYNcz5nFaZkFOLb6WapOT7HPziLDk%0AVWzOvpgYrU61dFja%2BM8%3D%0A)

 

 

## Can I exclude a specific past chat from searches?

 

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen. 

 

Clicking the ghost icon will open an incognito chat, creating a temporary conversation that isn’t saved to your chat history. Claude won’t pull information from incognito chats when searching previous conversations.

 

 

---

 

## What is Claude's memory?

Claude can now generate memory based on your chats. With the addition of memory, Claude transforms from a stateless chat interface into a knowledgeable collaborator that builds understanding over time.

 

## How does Claude’s memory work?

In addition to searching past chats, enabling Claude's memory feature adds several capabilities.

 

### How Claude stores memory 

Claude builds memory as a set of individual entries that are organized into categories. Claude reads, writes and updates these entries in real time as you chat rather than on a fixed daily schedule.

 

We apply safeguards and conduct evaluations to memory to help keep users safe.

 

### Project memory and summary

Each project has its own separate memory space and dedicated project summary, so the context within each of your projects is focused, relevant, and separate from other projects or non-project chats.

 

## Enable Claude’s memory

 

You can toggle Claude’s memory on by navigating to **[Settings > Memory](https://claude.ai/new#settings/customize-memory)** and turning on **Generate memory from chats**:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2533482441/b5c806a8e3f68bf34c4a70724d38/d30be013-d099-4c93-99d1-23d404792f08?expires=1784458800&signature=06ee576ed81d37012c019cd9a978a77fa5f8dbdaea3a29dfb5f949d980628530&req=diUkFc12n4VbWPMW1HO4zRlYrp9p51gkNshWSMEMw9c%2BJlsiaaLjYYsil0d4%0Ahq1Url0mBatuhGaJMuc%3D%0A)

 

If you want to disable Claude’s memory, click the toggle and you'll see two options:

- **Pause memory:** Claude keeps its existing memory but won’t use memory or make new memories. Conversations with Claude while memory is paused will not be summarized into its memory should you turn the feature back on.
- **Reset memory:** Permanently deletes all memories including project memories. Once you select this option and click "Reset memory," this cannot be undone. Upon re-enabling the feature, you’ll start from scratch and Claude will not have its previous memory.

 

## What Claude remembers

Claude focuses on work-related context that helps improve collaboration. You will see this information reflected in your memory or project summary:

- Your role, projects, and professional context
- Communication preferences and working style
- Technical preferences and coding style
- Project details and ongoing work<br>​

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

See exactly what Claude remembers about you by navigating to **[Settings > Memory](https://claude.ai/new#settings/customize-memory).** The Memory panel lists everything Claude remembers, grouped by category. Select any entry to see its summary and details.

 

To change an entry, use the "Tell Claude what to change or remove" box. To remove an entry entirely, select "Delete." You can also update your memory directly from your chats. Simply tell Claude what you'd like it to remember, and it will update Claude’s  memory of you without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation.

 

### Past chat citations

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

 

### Toggle search past chats and memory on/off

You maintain control over Claude’s ability to search past chats and use memory–you can always disable these features and enable them again when needed in **[Settings > Memory](https://claude.ai/new#settings/customize-memory).**

 

### Importing your memory from other AI tools

You can now transfer your memory between Claude and other AI services. This feature lets you import memories from other AI assistants or export your Claude memory for backup or migration. This feature is experimental and still in active development, but for best practices, see this article: **[Importing and exporting your memory from Claude](https://support.claude.com/en/articles/12123587-importing-and-exporting-your-memory-from-claude)**.

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

Yes, navigate to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and find the **Preferences** section. Switch the toggle next to “Search and reference chats” off:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730889/3fafbf5ecaa0ae31d7d84a66229b/c25536c1-7433-4b94-a5e9-cd5acf97a4fd?expires=1784458800&signature=c48ad374b97753a5f82e89d08447a5c267adea053e6d0d7f6213933b40fd3bd3&req=dScmH859nYlXUPMW1HO4zRzXH1s0JjnKJG68qZhl7813vlOeL%2BQtpLlC1U3C%0AIb7S2b9Smc019TMnuUo%3D%0A)

 

### Can I exclude a specific past chat from searches?

When starting a new chat with Claude outside of a project, you'll see a ghost icon in the upper right corner of your screen:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730893/9549b21954e0070ceb6b85231fd5/88e59234-6fc2-4229-84fe-733b33efff26?expires=1784458800&signature=98ab0cdbae9134dc1ccace0485465cb0ec952ecba03498253787bf2874a05847&req=dScmH859nYlWWvMW1HO4za54sKdoOY6zXDpzhlKsgjPmRhlUQYdK9emKn3tu%0ALP%2F9QNc%2BJMQKxP9JejE%3D%0A)

 

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

You can toggle Claude’s memory on by navigating to **[Settings > Capabilities](http://claude.ai/settings/capabilities)**:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1719730892/62f9f2b68d675a8e33393f06024f/89198978-192f-4c52-915d-5294b16f3fe1?expires=1784458800&signature=089ed60d035166bb5f597c5386c4b7773346193b5519bbed6e6ad5c4b929d169&req=dScmH859nYlWW%2FMW1HO4zTD5MMXicuxNBq9N9dRTKYeY0fljEKfQ0MciT38f%0AiGLpxrA10u6OIlxMmKk%3D%0A)

 

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

See exactly what Claude remembers about you by navigating to **[Settings > Capabilities](http://claude.ai/settings/capabilities)** and clicking “View and edit memory.” The **Manage memory** modal displays everything Claude remembers about you. In addition to asking Claude to edit the existing summary, you can also tell Claude what you want it to remember. To add custom instructions to Claude’s memory, click the pencil icon in the lower left corner of the summary.

 

You can also update your memory summary directly from your chats. Simply tell Claude what you'd like it to remember, and it will update your memory summary without needing to leave the conversation. Any edits made in this way will immediately apply to your next conversation, so you don’t need to wait for the daily synthesis to run.

 

**Past chat citations**

When Claude references previous conversations, you'll see citations linking back to the original chats, along with the option to delete specific conversations.

 

**Toggle search past chats and memory on/off**

You maintain control over Claude’s ability to search past chats and use memory – you can always disable these features and enable them again when needed in **[Settings > Capabilities](http://claude.ai/settings/capabilities)**.

 

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

- [How large is the context window on paid Claude plans?](https://support.claude.com/en/articles/8606394-how-large-is-the-context-window-on-paid-claude-plans)
- [Import and export your memory from Claude](https://support.claude.com/en/articles/12123587-import-and-export-your-memory-from-claude)
- [Use incognito chats](https://support.claude.com/en/articles/12260368-use-incognito-chats)
- [Use Claude Cowork on Team and Enterprise plans](https://support.claude.com/en/articles/13455879-use-claude-cowork-on-team-and-enterprise-plans)
- [Organize your tasks with projects in Claude Cowork](https://support.claude.com/en/articles/14116274-organize-your-tasks-with-projects-in-claude-cowork)
