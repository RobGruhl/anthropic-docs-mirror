# Share and unshare chats

*Updated over 2 months ago*

---

Learn how to create shareable links to your chats with Claude. While chats are always private by default, you can easily create snapshots of your conversations to share via direct link. This guide walks you through the process of sharing and unsharing chats.

 

## Share chats

To share a chat:

1. Click the "Share" button in the upper right corner of your chat.
2. Click the "Share" button in the pop out to create a shareable link.

Once a chat has been shared, anyone with the link can view the chat snapshot. The chat snapshot includes all messages that were sent prior to sharing the chat, including any artifacts. All messages sent after sharing a chat will remain private by default. However, if you unshare the chat and share it again, the snapshot will be updated to include any new messages.

 

### Share chats with files or MCP integrations

When sharing chats that include uploaded files or MCP (Model Context Protocol) integrations, it's important to understand what information is included in the shared snapshot.

 

**Attached files:** If you share a chat that contains an attached file, the file itself is not included in the shared snapshot and remains private. Only the conversation and Claude's responses will be visible to anyone with the link.

 

**MCP tool calls:** When sharing chats that use MCP integrations, the raw data retrieved from MCP tool calls remains hidden in the shared snapshot. Only the final chat output and conversation will be visible to viewers. The underlying tool call data stays private.

 

This ensures that sensitive information from your files and connected tools is protected, even when you share a chat snapshot.

 

## Unshare chats

To unshare a chat:

1. Navigate to the "Share" menu.
2. Click the visibility dropdown.
3. Change the chat from "Public" to "Private" to disable the direct link.

 

## Manage shared chats

Users on free, Pro, or Max plans can review a log of shared chats by navigating to **[Settings > Privacy](https://claude.ai/settings/data-privacy-controls)**. Find the **Privacy settings** section and click “Manage” next to **Shared chats:**

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1921669913/7cc7be48cfc7a18f9f469d6cd83c/CleanShot+2026-01-08+at+10_20_43%402x.png?expires=1788115500&signature=a6b4e69eb1425204b30a6f6032a26b3c9a8bc5e89b89f11b6ad779428d549ab4&req=dSklF894lIheWvMW1HO4zWn5HzscY0Buc9cNIYuX0GH98RJD2D7n14zYUY5K%0As%2BgKFAamvxJaUEgIFfQ%3D%0A)

 

This will open a **Shared chats** modal listing the title, date shared, and link to each chat, allowing you to easily review and access all your previously-shared content. From here, you also have the option to click “Unshare” next to each listed chat to revoke access to the last snapshot you shared:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243810/e6fe1d262597446c7fe21dff9f10/AD_4nXdW-GhByF8uKV7fCq9lTbkVB91FglSL6TSyXAOUk_MLcTV9YsEMBMkm9rgm1oXqv0k3sJh1JhlzZP6tHVkKbDJJ71pDRRtM3aVNG64MDuKDIzgmknh-XDZdNa7biTsTdwGoPr5GRg?expires=1788115500&signature=d5a9d252a065ed67e0e189b74cd436565123119bc4770a8ad9d2ba5b8ded63dd&req=dSYlEst6noleWfMW1HO4ze44eC9glRc7guvTv9woD7ahm4jy8llGtF%2BIjH2u%0AIttgcCogcaQHaSbh374%3D%0A)

 

If you don’t have any shared chat snapshots, the **Shared chats** modal will show “No shared content found”:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1624243808/b025db8e598f0c88fb16d83d48d5/AD_4nXeUwCKnmFzzrjMHhfr5By4zk5pJlkEn3wbJ8-aNfu13Yl99IjBywpqPx9G07QRzpH1EwRY7uG7Q9m9fib98Gql1cIV7XwUCTzEgBNu79Ey8tCOS5CEVmwveIcEOxJ4fonBhe3g9MA?expires=1788115500&signature=b7142fee7e78ce0fd3f64fd1085af45959e2ca1734b1d804b0cb2288537d227e&req=dSYlEst6nolfUfMW1HO4zdaFnc11gIy0DeZsm0Gz1Hvj%2BN19eBgV6Z5Bxmdm%0An90KTJCPyrSU81wzMZU%3D%0A)


---

## Related Articles

- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [Manage project visibility and sharing](https://support.claude.com/en/articles/9519189-manage-project-visibility-and-sharing)
- [Publish and share artifacts](https://support.claude.com/en/articles/9547008-publish-and-share-artifacts)
- [Custom visuals in chat and Cowork](https://support.claude.com/en/articles/13979539-custom-visuals-in-chat-and-cowork)
- [Monitor Claude Cowork activity with OpenTelemetry](https://support.claude.com/en/articles/14477985-monitor-claude-cowork-activity-with-opentelemetry)
