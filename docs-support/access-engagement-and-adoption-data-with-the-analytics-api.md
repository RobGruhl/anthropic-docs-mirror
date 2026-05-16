# Access engagement and adoption data with the Analytics API

*Updated this week*

---

The Analytics API gives Enterprise plan Primary Owners programmatic access to engagement and adoption data for their organization. Use it to build internal dashboards, track adoption trends, and feed Claude engagement data into your existing reporting tools.

 

## How is this different from the analytics dashboard and Compliance API?

All three options give you different views into your organization's data:

 

The **Analytics dashboard** (accessed via **[Analytics](https://claude.ai/analytics/activity)**) shows visualized usage data in the product. It's the right tool for day-to-day monitoring when you don't need to integrate data elsewhere.

 

The **Analytics API** returns the same aggregated usage and engagement metrics, but programmatically—so you can pull them into BI tools, map them against org charts, or automate reporting workflows. Data is aggregated per organization, per day.

 

The **Compliance API** is for governance and auditing use cases. It gives you access to individual user actions, raw activity events, and conversation content. If you need aggregated engagement metrics for dashboards, rather than raw events for auditing, use the Analytics API.

 

---

 

## Get started

To access the Analytics API, you need Primary Owner access to your Enterprise organization.

 

Follow these steps:

1. Navigate to **[Analytics > API keys](http://claude.ai/analytics/api-keys)**.
2. Find the **Access** toggle under **Analytics API** and toggle it on.
3. Click “+ Create key” to generate a new API key. Keep this key private—treat it like a password.
4. Use the key with the <code>x-api-key</code> header in your requests.

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/2053687376/dac20c85f3d3fcab64c98fee0d1c/c0af2448-7bfb-4d10-b474-025cb4f04f59?expires=1771884000&signature=3e7d6d4aca420e93566f405bf245ed2a3be06704829e7d8000ea446f83dc6dc6&req=diAiFc92moJYX%2FMW1HO4zUxhx6xN0q%2BP2G8yJDINvfTfGWKMWg03gWLLES3N%0AAEDrVlylUJqiyFflH48%3D%0A)

 

For full authentication details, endpoint references, and code examples, refer to our **[Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide)**.

 

---

 

## What data is available?

The Analytics API includes five endpoints. All data is aggregated per organization, per day, and is available for up to the past 90 days (not before January 1, 2026).

- **User activity**: Per-user engagement metrics including conversation counts, messages sent, projects created, files uploaded, artifacts created, skills used, connectors used, and Claude Code metrics like commits, pull requests, and lines of code.
- **Activity summary**: Organization-wide daily, weekly, and monthly active user counts, along with seat utilization and pending invite counts. Supports date ranges up to 31 days per request.
- **Chat project usage**: Conversation and user counts broken down by project, for Claude projects.
- **Skill usage**: How many users are using each skill, with breakdowns for Claude and Claude Code sessions separately.
- **Connector usage**: Which connectors your organization is using and how many unique users have used each one.
-  

---

 

## Data limits

All endpoints return data for a single date or date range. Data is only available after January 1, 2026, and for dates more than three days ago.

 

The API has a default rate limit of 60 requests per minute. If this doesn't meet your organization's needs, reach out to your Anthropic Contact or our **[Sales team](https://claude.com/contact-sales)**.


---

## Related Articles

- [What is the Enterprise plan?](https://support.claude.com/en/articles/9797531-what-is-the-enterprise-plan)
- [Release notes](https://support.claude.com/en/articles/12138966-release-notes)
- [Claude Code usage analytics](https://support.claude.com/en/articles/12157520-claude-code-usage-analytics)
- [Usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-usage-analytics-for-team-and-enterprise-plans)
- [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide)
