# Configuring session security settings

*Updated over a week ago*

---

Session duration controls allow Enterprise and Console Admins to set a maximum session length for all users in their organization. When enabled, users will need to sign in again after the specified period, even if they've been actively using Claude. This helps protect your organization by limiting how long a compromised session could remain valid.

 

## Enabling session length settings

### For Enterprise Admins

1. Log in to your Enterprise organization as an Admin or above.
2. Navigate to **[Organization settings > Organization and access](https://claude.ai/admin-settings/organization)**.
3. Locate the **Session security** section.
4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 7 days, 14 days, or 28 days.
5. Confirm your selection by clicking “Enable.”

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469436/1725e63ea1a2615948faecf4ec73/9bd276a1-7329-414d-87a1-d04dac93fff7?expires=1779066000&signature=e86cb417749c1461407b85e75d971b0aced16b37debcc9f052fde241f92d01fa&req=dSgvHs14lIVcX%2FMW1HO4zQNx5OsnRVxQg%2F6XaftFnjxApKp%2BMZdArhOo6m4f%0AwKJXy0771hkOjXbCNvo%3D%0A)

 

### For Console Admins

1. Log in to your Console account as an Admin.
2. Navigate to **[Settings > Organization and access](http://platform.claude.com/settings/organization)**.
3. Locate the **Session security** section.
4. Click “Enable” next to **Shortened session length**, then select a duration from the dropdown: 1 day, 3 days, or 7 days.
5. Confirm your selection by clicking “Enable.”

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469435/7a766bbe02e61c7d8f05deb5b8f0/b0bda400-47c6-43dd-9907-131ebe180b36?expires=1779066000&signature=8a7d5698db89b1b713d1b877f7a74a2356833376c0b69575709ec2fa00344699&req=dSgvHs14lIVcXPMW1HO4zWzx17A2IXkhXZ5D7eVpMtdPWmJfiYJN6PYTf3vD%0A5Ym2PM%2FpyRy9f5A6xW0%3D%0A)

 

### What happens after enabling shortened session length?

- Existing sessions older than the selected duration will expire immediately.
- Other active sessions will expire no later than the selected duration.
- Users whose sessions expire will be directed to sign in again.

 

## Updating session duration

You can change the session duration at any time by selecting a new value from the dropdown. If you select a shorter duration:

- Sessions older than the new duration will expire immediately.
- Sessions scheduled to expire beyond the new duration will have their expiration shortened accordingly.

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1888469437/46ac5bc55484ca01556d87a5ade7/b01a7651-ad65-4b32-93ff-16dbc9ca97c0?expires=1779066000&signature=09f3a74e97444b4c1255c8bcb656b22e1e0d4610d399dd3854d2b77a64acd95f&req=dSgvHs14lIVcXvMW1HO4zZ7mVcGb4T%2BjA00cbyPOLDXkcMfqkA01r%2BZnOU05%0APfdY0mlRRQ9xjLAFcXE%3D%0A)

 

## Disabling session length settings

To disable session duration, select "Disable" next to** Shortened session length**. Existing active sessions will continue to expire at their scheduled time. New sessions will return to default behavior, where sessions remain active as long as the user stays active.

 

## Users in multiple organizations

If a user belongs to multiple organizations with different session duration settings, the shortest duration will be applied. For example, if a user is a member of Organization A (7-day limit) and Organization B (28-day limit), their sessions will expire after seven days. This is because a single session is used across all their organizations, so the most restrictive setting takes precedence.


---

## Related Articles

- [Important considerations before enabling single sign-on (SSO) and JIT/SCIM provisioning](https://support.claude.com/en/articles/10276682-important-considerations-before-enabling-single-sign-on-sso-and-jit-scim-provisioning)
- [Set up single sign-on (SSO)](https://support.claude.com/en/articles/13132885-set-up-single-sign-on-sso)
- [Set up JIT or SCIM provisioning](https://support.claude.com/en/articles/13133195-set-up-jit-or-scim-provisioning)
- [Manage members on Team and Enterprise plans](https://support.claude.com/en/articles/13133750-manage-members-on-team-and-enterprise-plans)
- [Microsoft Entra ID SSO setup](https://support.claude.com/en/articles/13917889-microsoft-entra-id-sso-setup)
