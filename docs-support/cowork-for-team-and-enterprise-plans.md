# Cowork for Team and Enterprise plans

*Updated today*

---

This article explains important limitations and considerations for Team and Enterprise organizations using Cowork during the research preview period.

 

## Availability

Cowork is available as a research preview for paid plans (Pro, Max, Team, Enterprise) on:

- **Claude Desktop for macOS**
- - **[Click here](https://claude.ai/api/desktop/darwin/universal/dmg/latest/redirect)** to download
- **Claude Desktop for Windows** (x64 only)

**Windows users:** Cowork requires the latest version of Claude for Windows. Download or update at **[claude.com/download](https://claude.com/download)**.

 

Windows arm64 is not supported.

 

---

 

## Admin controls

Cowork will be on by default when the research preview launches, but organization owners can manually disable it.

 

**How to enable or disable Cowork:**

1. Log in to your Team or Enterprise organization as an Owner or Primary Owner.
2. Navigate to **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)**.
3. Locate the **Cowork** toggle.
4. Toggle off to disable Cowork for all users in your organization.

 

### Plugins

Plugins are included with Cowork and controlled by the same admin toggle—there's no separate setting to manage plugin access within Cowork.

 

When Cowork is enabled, users can:

- Access pre-installed knowledge work plugins (e.g., sales, legal, data analysis, finance, productivity)
- Install additional plugins from Anthropic's public repository
- Customize existing plugins or create new ones locally on their machines

 

---

 

## Compliance and monitoring limitations

Cowork currently lacks several enterprise monitoring and compliance capabilities. These limitations are important to understand before enabling Cowork for your organization.

 

### No audit logging or data exports

Cowork activity is **not captured** in:

- Audit Logs
- Compliance API
- Data Exports

Security teams will have no visibility into Cowork usage through standard enterprise monitoring tools. If your organization requires audit trails for compliance purposes, do not enable Cowork for regulated workloads.

 

### Local conversation storage

Cowork stores conversation history locally on users' computers. This data is not subject to Anthropic's standard **[data retention policies](https://privacy.claude.com/en/articles/7996866-how-long-do-you-store-my-organization-s-data)** and cannot be centrally managed or exported by admins.

 

### No role-based access controls

Cowork access cannot be selectively limited by user, role, or team within your organization. The admin toggle is organization-wide only—either all users have access or none do.

 

If you need to selectively enable Cowork for specific users or teams, contact your account representative.

 

---

 

## Security considerations

### Prompt injection risks

Cowork has unique risks due to its agentic nature and internet access. While we've implemented safety measures including model training and content classifiers, the risk of prompt injection attacks is non-zero.

 

Users should:

- Avoid granting access to files with sensitive information
- Monitor Claude for suspicious actions
- Limit browser and web access to trusted sources
- Report suspicious behavior immediately

For detailed guidance, see **[Using Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)**.

 

### Network access

Cowork respects your organization's current network egress permissions. Review your network access settings in **[Organization settings > Capabilities](https://claude.ai/admin-settings/capabilities)** under **Code execution** before enabling Cowork.


---

## Related Articles

- [Installing Claude Desktop](https://support.claude.com/en/articles/10065433-installing-claude-desktop)
- [Use Claude Code with your Team or Enterprise plan](https://support.claude.com/en/articles/11845131-use-claude-code-with-your-team-or-enterprise-plan)
- [Getting started with Cowork](https://support.claude.com/en/articles/13345190-getting-started-with-cowork)
- [Using Cowork safely](https://support.claude.com/en/articles/13364135-using-cowork-safely)
- [Purchase and manage seats on Enterprise plans](https://support.claude.com/en/articles/13393991-purchase-and-manage-seats-on-enterprise-plans)
