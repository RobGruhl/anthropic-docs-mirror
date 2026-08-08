# Set up single sign-on (SSO)

*Updated yesterday*

---

This guide covers the steps to configure SSO for Team and Enterprise plans, and Claude Console organizations.

 

## Step 1: Review prerequisites and important considerations

Before proceeding with SSO setup, complete the following:

 

**Review the considerations guide:** Read **[Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)** to understand parent organizations, determine your setup path, and complete any prerequisite steps such as merging organizations.

 

**Confirm you have the required role:**

- For Team or Enterprise plans: You must be an Owner or Primary Owner
- For Claude Console: You must be an Admin

**Confirm you have access to the following:**

- DNS settings for your company's email address domain
- Your company's SSO Identity Provider (IdP) used to log in to third-party applications (e.g., Okta, Google Workspace, etc.)

Please contact your organization's IT Administrator if you do not have permissions to manage Claude or company DNS settings.

 

---

 

## Step 2: Verify your domain(s)

Domain verification proves that you own your company's domain. Once verified, you can configure SSO for accounts with your company's domain.

 

You can verify multiple domains for a single organization, but all domains must be managed through a single IdP. We don't support verifying domains from separate IdPs within the same organization.

1. Navigate to your **Organization and access** settings in Claude (**[claude.ai/admin-settings/organization](https://claude.ai/admin-settings/organization)**) or your **Identity and access** settings in Console (**[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)**) – note this page will only appear on Console if you've worked with Sales to enable SSO or completed a merge proposal.
2. In the **Domains** section, click “Add or edit domains.”
3. Enter the domain(s) you want to verify in the **Update organization email domains **modal and click the “+” button:
3.  
3. 
3.  
4. Click “Save” when you’re finished adding domains.
5. The domain(s) you added will now appear in the **Domains** section; click “Verify” to the right of the domain(s) to begin the verification process.
6. Enter your domain in the text box and click “Continue”:
6.  
6. 
6.  
7. The setup screen displays a TXT record. **Copy the full Value using the copy button**—it begins with <code>anthropic-domain-verification-</code> and is longer than what's visible in the box. In your DNS provider, add a TXT record with **Host/Name** set to <code>@</code> (the root of your domain) and **Value** set to the copied string. Add it alongside any existing TXT records; don't replace them. The value is case-sensitive, so paste it exactly.
7. 1. **Important:** Save the TXT value before leaving the setup screen. Once the domain shows as Pending, the admin console doesn't display the value again. If you lose it, you'll need to remove and re-add the domain, which generates a new value.
8. Wait 10 minutes for your DNS change to propagate.
8. - **Note:*** DNS changes can take 24-48 hours to propagate globally.*
9. When you see the green "Verified" badge, you can close the instructions page.
10. If your domain shows as "Pending," use the "Refresh" button.
10.  

### If your domain stays Pending

Clicking "Refresh" re-checks your DNS; it won't show Verified until the published TXT record exactly matches the expected value. If it stays Pending after DNS has propagated, check the following:

- **The record exists at the root.** Look up your domain's TXT records with a tool such as **[DNSChecker](https://dnschecker.org/#TXT)** and confirm a record beginning with <code>anthropic-domain-verification-</code> appears for <code>yourdomain.com</code> (not <code>www.yourdomain.com</code> or another subdomain). If it doesn't appear, the record may have been added at the wrong host or hasn't propagated yet.
- **The value matches exactly.** The check is case-sensitive and requires the full string including the <code>anthropic-domain-verification-…=</code> prefix. A single character difference will keep it Pending.
- **You haven't removed and re-added the domain.** Each re-add generates a new verification value. If you re-added the domain after publishing the TXT record, the published value no longer matches—you'll need to update the DNS record with the new value.

If the record is correct and propagated but the status still shows Pending, contact Support.

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2047044496/b8df54a0331784cc9ae8f00112aa/bf9609c1-dc93-4665-a066-4cae2fe4b002?expires=1786225500&signature=cf15b124313df1c1175e332a1a82f02d57c0f47dfe55be70cee28fdd2417b4aa&req=diAjEcl6mYVWX%2FMW1HO4zVjmWS8CbXG8PM2D8Zcdgrg9Vum7H7gJPzjtTO3V%0ATzmpodgVR5%2B%2F0gr7lMc%3D%0A)

 

---

 

## Step 3: Set up SSO with your Identity Provider

1. Navigate to your **Organization and access** settings in Claude (**[claude.ai/admin-settings/organization](https://claude.ai/admin-settings/organization)**) or your **Identity and access** settings in Console (**[platform.claude.com/settings/identity](https://platform.claude.com/settings/identity)**).
2. In the **Authentication **section, click “Setup SSO” (or “Manage SSO”).
3. Follow the setup guide provided for your Identity Provider (see below for additional guides).
4. At the end of these steps, you’ll be prompted to Test Single Sign-on to confirm there are no errors and the configuration is successful.
5. Once complete, navigate back to the **Organization and access** settings page for further configuration options.

 

For IdP-specific setup instructions, see:

- **[Okta SAML](https://workos.com/docs/integrations/okta-saml)**
- **[Entra ID SAML (formerly Azure AD)](https://workos.com/docs/integrations/entra-id-saml)**
- **[Google SAML](https://workos.com/docs/integrations/google-saml)**
- **[OneLogin SAML](https://workos.com/docs/integrations/onelogin-saml)**
- **[JumpCloud SAML](https://workos.com/docs/integrations/jumpcloud-saml)**
- **[Duo SAML](https://workos.com/docs/integrations/duo-saml/4-enter-duo-saml-settings-in-your-workos-dashboard)**
-  

---

 

## Step 4: Choose to require SSO

You can now choose to toggle on **Require SSO for Console** and/or **Require SSO for Claude,** on the **Organization and access** page, under the **Authentication** section:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2312690200/bd2403586d4f6651ccd79e2a45af/b9f8d7ce-0def-49d9-bfb2-3a14352d7214?expires=1786225500&signature=c5c37436923bea583f3cba926ffe123a85f103b05fc0f784e7ce427714afcde1&req=diMmFM93nYNfWfMW1HO4zdAICwmjAHkPItXtKivx6ZEVlGPyHTL7RH5Xs7kX%0AP4LpmLWYDHq7O2hxY14%3D%0A)

 

When SSO is required, users must use the “Continue with SSO” option to log in to their Claude/Console accounts. When SSO is not required, they will have the option to choose “Continue with SSO” or “Continue with email.”

 

Before you decide, review **[What happens to existing users when SSO is enabled](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning#h_644f467167)**.

 

---

 

## Step 5: Choose your provisioning approach

Once SSO is enabled, you need to decide how users will be added to your organization by choosing an option within the **User provisioning **section of your **Organization and access** settings.

 

**Invite only** is the default. Users are added and removed directly in your Claude or Console settings. Please see **[Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-managing-members-on-team-and-enterprise-plans)**.

 

**Just-in-Time (JIT) provisioning** can be enabled to automatically provision users when they first log in. By default, users assigned to your Anthropic IdP app first login, they will receive the User role. This is the simplest automated option and requires no additional configuration beyond selecting "Just-in-Time (JIT)" as your provisioning mode.

 

### Enable group mappings - when to configure additional provisioning features

For more control over provisioning, see **[Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-setting-up-jit-or-scim-provisioning)**. You'll want to review this guide if you need to:

- Automatically assign roles or seat tiers based on IdP group membership.
- Use SCIM directory sync for automatic provisioning and deprovisioning.
- Manage access across multiple organizations (e.g., if you have both a Team/Enterprise organization and a Console organization linked to the same parent and need to control which users are provisioned to each).

 

---

 

## Updating your SSO certificate

When your Identity Provider's X.509 signing certificate expires or is rotated, you'll need to update it in Claude or Console to maintain SSO functionality.

1. Navigate to your settings:
1. - For Team and Enterprise plans: **[claude.ai/admin-settings/organization](https://claude.ai/admin-settings/organization)**
- For Claude Console: **[platform.claude.com/settings/identity](https://platform.claude.com/settings/organization)**
2. In the **Authentication **section, click “Manage SSO.”
3. Find the **Metadata configuration** section and click “Edit.”
4. Update your certificate information and save your changes.
5. Click "Test sign-in" on the same page to confirm everything is working.
5.  

---

 

## Turning off SSO

You can toggle **Require SSO for Claude **or **Require SSO for Console** off at any time. This will make SSO optional for all users.

 

To fully disconnect SSO, click “Manage SSO” then “Reset connection.” This will end all users’ sessions and require them to sign back in via email login link.


---

## Related Articles

- [Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Okta SSO setup](https://support.claude.com/en/articles/13917894-okta-sso-setup)
- [SSO login](https://support.claude.com/en/articles/14503613-sso-login)
- [Set up SCIM in Claude for Government](https://support.claude.com/en/articles/14503643-set-up-scim-in-claude-for-government)
