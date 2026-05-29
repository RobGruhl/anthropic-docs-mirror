# Enabling and using the desktop extension allowlist

*Updated over 2 months ago*

---

This article introduces a desktop extension allowlist that Team and Enterprise plan Owners can use to manage their organization’s access to extensions.

 

## How to enable the allowlist

The desktop extension allowlist is disabled by default, so an organization Owner will need to switch it on manually. Note that **users will be able to access all desktop extensions in the registry until you enable the allowlist. **To prevent this, ensure you activate the allowlist to block all desktop extensions by default, then add only the extensions your team needs access to.

 

**To turn on the allowlist:**

1. Open Claude Desktop
2. Click your initials or name in the lower left corner
3. Navigate to Organization settings > Connectors
4. Switch to the "Desktop" tab:
4.  
4. 
4.  
5. Toggle **Allowlist** on:
5.  
5. 

 

## What happens after enabling the allowlist?

Once the allowlist is enabled:

- Any existing desktop extension installations will be force-deleted from Claude Desktop clients.
- Users will no longer be able to install new desktop extensions that are not included within the allowlist.
- Users can only download extensions from the sanctioned in-app registry; they can no longer drag or click to install MCPBs. 

Note that the allowlist does not guard against individuals tampering with local MCP file contents after installation.

 

Consider completing the allowlist setup during off-hours to minimize disruption to existing users. If a user's installed extension is deleted while the allowlist is being configured, they will need to manually re-install the extension.

 

## Managing allowed extensions

After enabling the allowlist, you can choose which extensions to allow:

1. Navigate to Organization settings > Connectors and select the “Desktop” tab.
2. Click “Browse extensions” to view the list of available extensions.
3. Select the extension you want to add.
4. Click the “Add to your team” button.
5. The extension will appear in your allowlist.

If you want to remove an extension from the allowlist, click the “...” button and “Remove from allowlist.”

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1781751250/6558c0f59aea7976bd44b0213d76/e750f02b-cd0d-437e-a83f-9ac362cdf456?expires=1780061400&signature=c0616812ca3b8dc2306fed9837f4c0d92139003f78b66e69f0d8bf90bffe37c9&req=dScvF857nINaWfMW1HO4zTrxBagp%2BVaRqXridZhfx1LQK2CVo%2Bmp0c47GmO9%0ApoSsY2g7zeMkdqSfpI0%3D%0A)

 

## Uploading custom extensions

You can also upload custom extensions to deploy across your organization via Organization settings > Connectors > Desktop.

1. Click “Add custom extension”
2. This will open a filepicker; select the .mcpb file.
3. The extension will appear under **Custom team extensions**.
4. Click "...” then “Add to team” to add it to your allowlist and enable it for your team.

When you allowlist a custom extension, it's scoped to your specific organization and can't be used across other organizations. For more in-depth information about creating custom extensions with MCP Bundles (.mcpb), please refer to our **[desktop extension developer documentation](https://github.com/anthropics/mcpb)**.

 

## Updating custom extensions

We’ve also introduced the ability to update previously-installed custom extensions to new versions without having to remove and reinstall them.

 

You can update a new MCPB version by making changes to manifest.json, ensuring the version field for the update candidate is incremented from the current uploaded version, and that you leave the name value unchanged. Changing the name will create a new custom desktop extension rather than uploading a new version. Then navigate to the custom upload pane, select "Upload new version" via the kebab menu, and upload the new file.


---

## Related Articles

- [Install Claude Desktop](https://support.claude.com/en/articles/10065433-install-claude-desktop)
- [Getting Started with Local MCP Servers on Claude Desktop](https://support.claude.com/en/articles/10949351-getting-started-with-local-mcp-servers-on-claude-desktop)
- [Deploy Claude Desktop for macOS](https://support.claude.com/en/articles/12611117-deploy-claude-desktop-for-macos)
- [Enterprise configuration for Claude Desktop](https://support.claude.com/en/articles/12622667-enterprise-configuration-for-claude-desktop)
- [Deploying enterprise-grade MCP servers with desktop extensions](https://support.claude.com/en/articles/12702546-deploying-enterprise-grade-mcp-servers-with-desktop-extensions)
