# Set up the Microsoft 365 connector

*Updated this week*

---

This article walks admins through enabling the Microsoft 365 connector for their organization in Claude—including granting Microsoft Entra consent, restricting access, and managing permissions. Once setup is complete, people in your tenant can connect Microsoft 365 to their own Claude accounts to search across SharePoint, OneDrive, Outlook, and Teams from Claude. You can also enable write tools, which let Claude send email, manage calendar events, and create and update files on a member's behalf.

For end-user instructions on connecting and using Microsoft 365 once setup is complete, see **[Connect Claude to Microsoft 365](https://support.claude.com/en/articles/15183774)**.

 

---

 

## Setup overview

Two things need to happen before anyone in your organization can connect Microsoft 365, plus an optional third step if you want to enable write tools:

1. **On Team and Enterprise plans:** A Claude organization owner enables the Microsoft 365 connector for the organization.
2. **In every tenant:** A Microsoft Entra Global Administrator grants a one-time consent that authorizes the integration for your tenant.
3. **To enable write tools:** A Microsoft Entra administrator consents to the updated permission set, and you enable write tools for your organization. See **[Enable write tools](#h_a51d877afd)** below.

After completing these steps, members can connect Microsoft 365 to their own Claude accounts following the steps in **[Connect Claude to Microsoft 365](https://support.claude.com/en/articles/15183774)**.

 

## Enable the connector for your organization

This step applies to Team and Enterprise plans only. On Free, Pro, and Max plans, skip to the next section.

1. Sign in to Claude.
2. Navigate to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.
3. Click “+ Add” at the top of the page, then “All available.”
4. Find **Microsoft 365** and click “Add to your team.”

 

## Grant Microsoft Entra admin consent

A Microsoft Entra Global Administrator in your tenant needs to authorize the integration before anyone can connect. There are two ways to do this.

 

### Option 1: Consent through Claude

If your Microsoft Entra Global Administrator has a Claude account, they can grant consent during the standard connection flow:

1. Navigate to **[Customize > Connectors](https://claude.ai/customize/connectors)**.
2. Find **Microsoft 365** and click “Connect.”
3. Authenticate with Microsoft 365 credentials.
4. Review and accept the requested permissions, checking the box to grant access on behalf of the whole organization.

After this, other people in the same Entra tenant can connect by following the standard end-user steps. They won't see the consent prompt—they'll just authenticate and start using the integration.

 

### Option 2: Manual setup in Microsoft Entra ID

Use this path if your Microsoft Entra Global Administrator doesn't have a Claude account, or if you need to troubleshoot the app install and permissions setup. You can add the connector apps and grant admin consent directly in Microsoft Entra ID.

This process adds two service principals to your tenant. Each principal establishes a service-level identity for one of the two M365 MCP for Claude app registrations, allowing them to access and interact with your organization's data and resources via the Microsoft Graph API.

 

**1. Add the service principals**

Using Microsoft Graph Explorer, add both required service principals:

 

M365 MCP Client for Claude:

```
POST https://graph.microsoft.com/v1.0/servicePrincipals
{"appId":"08ad6f98-a4f8-4635-bb8d-f1a3044760f0"}
```

M365 MCP Server for Claude:

```
POST https://graph.microsoft.com/v1.0/servicePrincipals
{"appId":"07c030f6-5743-41b7-ba00-0a6e85f37c17"}
```

 

**2. Grant admin consent**

Construct and visit the following URLs in your browser, replacing {your-tenant-id} with your organization's tenant ID.

 

M365 MCP Client for Claude:

```
https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=08ad6f98-a4f8-4635-bb8d-f1a3044760f0
```

 

M365 MCP Server for Claude:

```
https://login.microsoftonline.com/{your-tenant-id}/adminconsent?client_id=07c030f6-5743-41b7-ba00-0a6e85f37c17
```

When you visit each URL, you'll be prompted to consent to the delegated permissions required by the integration on behalf of your organization.

 

**3. Finish setup**

- **Team and Enterprise plans:** A Claude organization Owner needs to enable the connector in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**. Then members can connect individually.
- **Free, Pro, and Max plans:** Members can connect by navigating to **[Customize > Connectors](https://claude.ai/customize/connectors)**, finding **Microsoft 365**, and clicking “Connect.”
-  

### Restrict who can use the connector

To limit which people in your tenant can authenticate to Microsoft 365 through Claude:

1. Go to the Microsoft Entra admin center at entra.microsoft.com.
2. Navigate to the **M365 MCP Server for Claude** enterprise application.
3. Go to **Properties** and set **Assignment required?** to “Yes.”
4. Under **Users and groups**, add the specific users or groups who should have access.
5. Repeat the same steps for the **M365 MCP Client for Claude** enterprise application.

Both components need to be restricted to the same set of authorized people.

 

### Restrict which permissions the connector can use

To limit which types of resources the integration can access, selectively revoke permissions from the default set of authorized scopes. This requires Microsoft Entra admin access.

1. As a Microsoft Entra admin, go to entra.admin.com.
2. Select “Enterprise Applications.”
3. Next to the search box, remove the application type filter.
4. Search for and click “M365 MCP Server for Claude.”
5. Go to **Permissions**.
6. Under the **Admin consent** tab and in the Microsoft Graph list of permissions, select the permission you would like to revoke and click the “**…**” button.
7. Select “Revoke permission” and confirm with “Yes, revoke.”

Once revoked, attempts to access a resource with that permission will return a "Failed to call tool" error.

 

Members can also individually turn off specific tools in their own Microsoft 365 settings to prevent Claude from trying to access a tool for which the permission has been revoked.

 

To restore a revoked permission, follow the steps to grant admin consent described in **Option 2: Manual setup in Microsoft Entra ID**. This will revert the permissions to the default state.

 

---

 

## Enable write tools

Write tools let Claude send email, manage drafts and calendar events, update mailbox settings, and create and update files in OneDrive and SharePoint. Read and search tools work the same whether or not write tools are enabled.

 

**1. Re-consent to the updated permissions**

The connector's permission set now includes additional Microsoft Graph scopes to support write tools. If your tenant consented before write tools launched, a Microsoft Entra Global Administrator needs to review and approve the updated permission set before write tools activate. Review and approve the updated permissions for the connector in your tenant's **Enterprise Applications** consent flow. This is a one-time action per tenant.

 

**2. Enable write tools for your organization**

If your organization was using the connector before write tools launched, they will be blocked by default. Enable them for everyone by going to **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**, finding “Microsoft 365,” and setting the appropriate permissions. Enterprise plans can enable them for a subset of users through **[custom roles](https://support.claude.com/en/articles/13930452-manage-custom-roles-on-enterprise-plans#h_979e558d00)**.

 

**3. Verify**

Once enabled, ask Claude to perform a low-risk write action, such as "Draft an email to myself, but don't send it," to confirm write tools are active.

 

---

 

## Permissions reference

The Microsoft 365 connector uses **delegated permissions**, meaning Claude acts on behalf of each individual user and can only access data that user already has permission to view in Microsoft 365. Permissions are read-only—Claude can't modify, delete, or create content in your tenant.

 

During authentication, the integration requests the following permissions:

 

**Basic access**

- <code>User.Read</code>: Sign in and read user profile
- <code>openid</code>: Sign in with organizational account
- <code>offline_access</code>: Maintain access to data
- <code>email</code>: View email address
- <code>profile</code>: View basic profile information

**Email (Outlook)**

- <code>Mail.Read</code>: Read email messages
- <code>Mail.ReadBasic</code>: Read email metadata (sender, subject, date)
- <code>Mail.Read.Shared</code>: Read emails in mailboxes the user has access to
- - **Note:** Shared mailbox access is included through the <code>Mail.Read.Shared</code> permission. Users can search shared mailboxes they have delegate access to in Microsoft 365, including full access and folder-level delegation. No setup is needed beyond standard admin consent and the delegate permissions already configured in Microsoft 365.
- <code>MailboxFolder.Read</code>: Read mailbox folder structure
- <code>MailboxItem.Read</code>: Read items in mailbox
- <code>MailboxSettings.Read</code>: Read mailbox settings, like the user's timezone

 

**Calendar**

- <code>Calendars.Read</code>: Read calendar events
- <code>Calendars.Read.Shared</code>: Read calendars shared with the user

**Teams chat**

- <code>Chat.Read</code>: Read Teams chat messages
- <code>Chat.ReadBasic</code>: Read Teams chat metadata
- <code>ChatMember.Read</code>: Read information about chat participants
- <code>ChatMessage.Read</code>: Read Teams chat messages

**Teams channels**

- <code>Channel.ReadBasic.All</code>: Read channel names and descriptions
- <code>ChannelMessage.Read.All</code>: Read channel messages

**Meetings**

- <code>OnlineMeetings.Read</code>: Read online meetings
- <code>OnlineMeetingTranscript.Read.All</code>: Read meeting transcripts
- <code>OnlineMeetingAiInsight.Read</code>: Read AI-generated meeting insights
- <code>OnlineMeetingArtifact.Read.All</code>: Read meeting recordings and artifacts
- <code>OnlineMeetingRecording.Read.All</code>: Read meeting recordings

**Files (OneDrive and SharePoint)**

- <code>Files.Read</code>: Read user files
- <code>Files.Read.All</code>: Read all files the user can access
- <code>Sites.Read.All</code>: Read items in SharePoint sites

**Write permissions**

The following permissions support write tools and are included in the updated consent set:

- <code>Mail.Send</code>: Send and forward email
- <code>Mail.ReadWrite</code>: Create, update, and delete drafts; move and label messages
- <code>Calendars.ReadWrite</code>: Create, update, delete, and respond to calendar events
- <code>Files.ReadWrite.All</code>: Create and update files in OneDrive and SharePoint
- <code>MailboxSettings.ReadWrite</code>: Manage categories, inbox rules, and automatic replies 

**User directory**

- <code>User.ReadBasic.All</code>: Read basic profile information for all users in the organization (used for finding meeting availability)

The Microsoft 365 connector searches SharePoint across the entire tenant using the permissions of the user. Site-specific search restriction isn't supported.

 

## Privacy and security

- **Permission inheritance:** Claude mirrors each user's existing Microsoft 365 permissions. Members can't access anything through Claude that they couldn't already see directly in Microsoft 365.
- **On-demand access:** Claude only accesses data when a user explicitly asks a question that requires it.
- **Revocable access:** Members can disconnect their own integration through **[Customize > Connectors](https://claude.ai/customize/connectors)**. Team and Enterprise plan Owners can also remove the connector for the entire organization in **[Organization settings > Connectors](https://claude.ai/admin-settings/connectors)**.

For more detail, see the **[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-)**.

 

---

 

## Troubleshooting

### A member can't authenticate

1. Confirm their account is tied to a Microsoft Entra tenant, not a personal Microsoft account.
2. Confirm their Microsoft 365 license is active.
3. Confirm admin consent has been granted using Option 1 or Option 2 above.
4. Check whether a Conditional Access policy in your tenant is blocking the connection. See below: **[Conditional Access is blocking the connection](#h_c7635fb6e2)**.
4.  

### Members are seeing "Failed to call tool" errors

A permission may have been selectively revoked in Microsoft Entra. Members can turn off the corresponding tool in their Microsoft 365 settings to suppress the error, or you can restore the permission by repeating the admin consent steps in **[Option 2: Manual setup in Microsoft Entra ID](#h_c5f095c9cf)**.

 

### Write tools aren't appearing for members

1. Confirm a Microsoft Entra administrator has consented to the updated permission set that includes write scopes.
2. Confirm write tools are enabled in the Microsoft 365 connector configuration, or that the member is covered by a role-based access policy that grants them.
3. Have the member disconnect and reconnect Microsoft 365 in **[Customize > Connectors](https://claude.ai/customize/connectors)**.
3.  

### Conditional Access is blocking the connection

A Conditional Access block shows up in one of three ways:

- A user sees "Authorization with the MCP server failed" and a reference code starting with <code>ofid_</code> when they try to connect. Our Support team can look up that code.
- A member who is already connected gets an error when Claude uses a Microsoft 365 tool. The error includes an <code>AADSTS</code> code, a note that the request was blocked by a Conditional Access policy, and the Trace ID and Correlation ID you can search for in Entra.
- Members are asked to reconnect Microsoft 365 on a regular cycle, much more often than the normal 90-day expiry. This usually means a sign-in frequency policy.

Connecting Microsoft 365 involves more than the sign-in the member sees. After the member signs in to Microsoft in their browser, Claude's servers exchange that sign-in for access tokens, and later exchange those tokens for Microsoft 365 access on the member's behalf. In our testing, Entra evaluates your Conditional Access policies against these server-side requests as coming from Anthropic's IP range, <code>160.79.104.0/21</code>. They identify the member and carry the device recorded when the member connected, not the member's current device or network. So a policy can pass the member's own sign-in and still block the connection a moment later, or block it days later. Learn more about **[Anthropic's IP addresses](https://platform.claude.com/docs/en/api/ip-addresses)**.

 

**Find the policy that's blocking the connection**

1. In the Microsoft Entra admin center, go to **Sign-in logs** and open the **User sign-ins (non-interactive)** tab. The member's own sign-in appears on the interactive tab and usually shows as successful, so the block is rarely there.
2. Filter by the affected member. The blocked requests can appear under either **M365 MCP Server for Claude** or **M365 MCP Client for Claude**, so filtering by member is more reliable than filtering by application. Don't filter by resource, which hides some of the rows.
3. Open the failed entry and select the **Conditional Access** tab. It names the policy that blocked the request.

The error code tells you what kind of policy it is:

- <code>AADSTS70043</code>: a sign-in frequency policy. See the next section.
- <code>AADSTS53003</code>: a policy set to block access. The Conditional Access tab tells you which one. If it's based on location, see the next section.
- <code>AADSTS50076</code>: a policy required multi-factor authentication on a server-side request. Disconnecting and reconnecting Microsoft 365 clears it. If it keeps happening, see the **[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)**.
- <code>AADSTS53000</code>: a policy requires a compliant device. The similar code <code>AADSTS530003</code> means a policy requires a managed device. In both cases the member needs to reconnect from a device that meets the policy. Learn more in the **[Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)**.

**Exclude Anthropic's IP range from sign-in frequency and location policies**

Because the server-side requests come from Anthropic's IP range, a policy that limits sign-ins to your own network, or that enforces a sign-in frequency, blocks them for every member. Excluding the two Claude applications from the policy isn't enough on its own. We recommend excluding Anthropic's IP range from the policy as well.

If the policy that blocked the request is a sign-in frequency or location policy:

1. In the Microsoft Entra admin center, go to **Conditional Access > Named locations** and create an IP range location containing <code>160.79.104.0/21</code>. Leave **Mark as trusted location** unchecked so the exclusion doesn't affect other policies that use trusted locations.
2. Open the policy that blocked the request and go to **Conditions > Locations > Exclude**.
3. Add the named location you created. Keep any existing exclusions for the Claude applications in place.
4. Save the policy and wait a few minutes for the change to apply.
5. Have an affected member disconnect and reconnect Microsoft 365 in **Customize > Connectors**.

 

---

 

## Frequently asked questions

### What happens if a member tries to connect before consent is granted?

They'll see an error message indicating that an administrator must grant app permissions before they can use the integration. The connection will fail until a Microsoft Entra Global Administrator approves the necessary permissions.

 

### Can the Microsoft 365 connector be used with enterprise search?

Yes. When enterprise search is enabled, it can query Microsoft 365 alongside other connected services for unified search across Slack, Google Workspace, Microsoft 365, and more.

 

### What file types can the connector read?

Claude reads Word, Excel, PowerPoint (including older .doc, .xls, and .ppt files), PDF, and plain-text formats such as .txt, .md, and .csv from SharePoint and OneDrive. Other formats, including OneNote, can't be read. For the full list, see **[Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365#h_ddeb82923f)**.

 

### Can the integration modify Microsoft 365 data?

Only after an Entra admin grants write scopes. With write tools on, Claude can send email, manage drafts and calendar events, update mailbox settings, and create and update files in OneDrive and SharePoint, always within each member's existing Microsoft 365 permissions. Without them, the integration is read-only. Claude can't post Teams messages or change Teams settings or permissions in either case, since there are no tools allowing this.


---

## Related Articles

- [Use connectors to extend Claude's capabilities](https://support.claude.com/en/articles/11176164-use-connectors-to-extend-claude-s-capabilities)
- [Microsoft 365 connector security guide](https://support.claude.com/en/articles/12684923-microsoft-365-connector-security-guide)
- [Set up role-based permissions on Enterprise plans](https://support.claude.com/en/articles/13930458-set-up-role-based-permissions-on-enterprise-plans)
- [MCP connectors](https://support.claude.com/en/articles/14503689-mcp-connectors)
- [Connect to Microsoft 365](https://support.claude.com/en/articles/15183774-connect-to-microsoft-365)
