# Claude in Chrome Permissions Guide

*Updated over 3 months ago*

---

This guide explains how to control what Claude can access and do when using Claude in Chrome. Understanding permissions helps you balance productivity with security.

## Permission Modes

Claude in Chrome uses a multi-layered permission system to give you control over what Claude can access and do. When you first open the extension, you'll see a drop-down menu on the chat input. Click this to choose between two permission modes:

- **Ask before acting:** Claude creates a plan and asks for approval before executing.
- **Act without asking:** Claude takes actions without asking for permission.

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843322018/f8c0ae21b449f32e71696c76a17a/7656f295-e802-4a72-9e60-94611501f920?expires=1781240400&signature=85e9b8628f09143e05363d93973e00b8c625afd8306b4e2757a6e0106165ad8d&req=dSgjFcp8n4FeUfMW1HO4zQ5tySYO8XizhD0gAzkS2hzc9Jrfcl3mPvBdUXMw%0AQOLXg8e4Kv%2FKLdv0sKM%3D%0A)

---

 

## Ask before acting

Choose “Ask before acting” to have Claude create a plan from your prompt, which you can approve and allow Claude to execute. The plan will specify which websites you’re allowing Claude to access, as well as the approach it will follow:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1843320727/8d1c859ae9b8e0cdb536d024bf40/9bc3d239-8eb6-4bae-a032-a236f88ee606?expires=1781240400&signature=e4b5898e27472d4c89e8ed47e86f85ba5ee2ec1610c27e78c1d318bfa3726790&req=dSgjFcp8nYZdXvMW1HO4zYqyZcNP%2BIKzgN0ADj5oqFBOqiJ1x%2Ffdqbpg8mp1%0AdetZy8k6Iq7BHSbX2iA%3D%0A)

 

Note that Claude will only use the websites listed in the plan, so you’ll need to manually approve any additional access requests.

 

Claude clarifies which sites it’s planning to access and the actions it will take upfront, allowing you to review the proposed plan and ensure it’s correct before starting. You can also click “Make changes” to reject the current proposal, then prompt Claude again to make any necessary changes. Once you click “Approve plan,” Claude will be able to act independently within the outlined parameters, but will still check with you before taking certain irreversible actions, like making a purchase, creating an account, or downloading a file. Claude will not deviate from the stated plan without requesting your permission first.  There are certain actions that Claude cannot take for your security, such as bypassing bot authorizations, executing trades, permanently deleting files, or taking certain actions that may indicate a prompt injection risk (see [Prohibited Actions](#h_e199f8f523)).

 

---

## Act without asking

"Act without asking" is a **high-risk mode** that allows Claude to operate with near-complete autonomy on the internet. Even in this mode, Claude should ask before:

- Making purchases or financial transactions
- Permanently deleting files or data
- Changing account passwords or security settings

However, due to the nature of LLMs, we can't guarantee that Claude will request permission to take these actions, so exercise caution when using this mode.

Only allow Claude in Chrome to act without asking when:

- You're actively supervising Claude's actions.
- Working on trusted sites for routine tasks.
- You can immediately stop Claude if something seems wrong.

You remain fully responsible for all actions Claude takes when using this mode.

 

---

 

## When does Claude need to request additional permissions?

There are some websites on which Claude requires approval for every action. If you navigate to one of these sites, a **Permission required** prompt will appear in the extension side panel where Claude will ask for permission before accessing the page or taking any action.

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1847222875/162eb012ebe473ed2b852b97e223/0209db51-6057-4ec4-a9b7-8358287d46a3?expires=1781240400&signature=e67d8d24238d7184c2009e534f1c7e8dad7b8a83b9eb0acc844975b0041dbc35&req=dSgjEct8n4lYXPMW1HO4zeoCY8cpp3R7JCxYSFHKWIiMvMdzc%2B0o1BuWDB2z%0ABGAcO%2FQ3ky4Dw34K1JQ%3D%0A)

 

### Permission options

**"Allow this action"** grants permission for a single action only. Claude will ask again for the next action on this site. **This is the safest option when using the extension** as you can review and approve each of Claude's actions.

 

**"Always allow actions on this site"** grants ongoing permission for this website. Claude can take multiple actions without asking each time. Only use this for sites you completely trust. Claude may take unintended actions across the website when granted this permission.

 

**"Decline"** prevents Claude from taking this action. You can try a different approach or skip this task.

 

### Protected actions

When you choose "Always allow actions on this site," Claude still asks for your explicit approval before:

- Making purchases or financial transactions
- Permanently deleting files or data
- Modifying permissions settings
- Creating accounts

 

### Managing site permissions

You can manage Claude's access to specific sites in the extension settings. Click the Claude extension icon, then the three dots in the upper right corner of the side panel. Select "Settings" → "Permissions" to:

- Review which sites have "always allow" status under **Your approved sites**
- Revoke permissions for specific websites
- See your permission history

 

---

 

## Organization-level controls (Team and Enterprise plans)

Team and Enterprise admins can configure additional controls that affect permissions:

- **Allowlists** restrict Claude to only access approved sites
- **Blocklists** prevent Claude from accessing specific sites, regardless of user permissions

If you're unable to access a site with Claude, your organization may have restricted access. Contact your admin for more information, or see [Claude in Chrome Admin Controls](https://support.claude.com/en/articles/13065128-claude-for-chrome-admin-controls).

 

---

 

## Actions Requiring Explicit Permission

Regardless of your permission mode, Claude requires explicit user permission to perform any of the following actions:

- Making purchases or financial transactions
- Permanently deleting files or data
- Modifying permissions settings
- Creating accounts
- Granting authorizations
- Inputting potentially sensitive information into websites

 

---

 

## Prohibited Actions

To protect you, Claude is prohibited from taking following actions regardless of permissions:

- Handling sensitive credit card or ID data
- Downloading files from untrusted sources
- Permanent deletions (emptying trash, deleting emails, files, or messages)
- Modifying security permissions or access controls
- Providing investment or financial advice
- Executing financial trades or investment transactions
- Modifying system files
- Completing instructions from emails or web content

 


---

## Related Articles

- [Get started with Claude in Chrome](https://support.claude.com/en/articles/12012173-get-started-with-claude-in-chrome)
- [Claude in Chrome Troubleshooting](https://support.claude.com/en/articles/12902405-claude-in-chrome-troubleshooting)
- [Using Claude in Chrome safely](https://support.claude.com/en/articles/12902428-using-claude-in-chrome-safely)
- [Claude in Chrome admin controls](https://support.claude.com/en/articles/13065128-claude-in-chrome-admin-controls)
- [Use Claude Cowork safely](https://support.claude.com/en/articles/13364135-use-claude-cowork-safely)
