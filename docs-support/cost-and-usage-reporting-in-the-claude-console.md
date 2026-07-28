# Cost and Usage Reporting in the Claude Console

*Updated over 4 months ago*

---

The Claude Console provides detailed cost and usage reporting to help you effectively manage your API usage and associated costs. This guide walks you through these features and how to use them.

 

## Accessing Cost and Usage Reports

Users with access to these reports can click into them on the left navigation menu on the Console:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584654217/db0a977417e38e43639f060d96e0/image.png?expires=1785248100&signature=b93219ce71b76a188169cbece93160e2a02446bbb9a92034c44d7bce4e6d4ccf&req=dSUvEs97mYNeXvMW1HO4zYCWiSEahc6buqqBX2puyxRZjbFDbOQE%2Bpnfrpso%0APEthx%2BlO4%2FM456XPPWI%3D%0A)

 

---

 

## Usage Reporting

The [Usage page](https://platform.claude.com/usage) offers a detailed breakdown of your API usage across different models and API keys.

 

### Key Features

- **Detailed Breakdown**: View usage data by model, date/time, and API key. Click into the bars on the bar chart for hour and minute granularity.
- **Flexible Filtering**: Use selectors to choose specific models, months, or API keys
- **Visual Representation**: A chart with input and output token counts.
- **Usage Statistics**: See total input and output tokens for your selected filters.
- **Rate-Limited Requests:** Review your requests that were blocked due to hitting rate limits.
- **Rate Limit Use: **Visualizations of input and output tokens per minute compared with the overall ITPM or OTPM rate limit. 
- **CSV Export**: Download your usage data for further analysis or reporting.

### How to Use

1. Select the Workspace you want to view (or choose "All Workspaces").
2. Select the model you want to view (or choose "All Models").
3. Choose the month you're interested in (or narrow to a specific month/day).
4. Select an API key (or view data for all keys).
5. The chart and statistics will update based on your selections.
6. Use the export button to download a CSV of the displayed data.

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584664321/59b50eba0b61e0789f7055fcf9f4/image+%285%29.png?expires=1785248100&signature=a14395eb3fd6317904ef9a8cff29e2820c843bcdb8495bc4405070d216a1476b&req=dSUvEs94mYJdWPMW1HO4zQwER3YoJYdnqMITUZbanFDlxAhNfBfXh7vMngpo%0AC5eb2stbzDUrXTBKh1E%3D%0A)

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584693386/aed472efe163abcbc14fa32f3699/rate+limited+requests.png?expires=1785248100&signature=e3b783eaba55234428dad7a7ae83cd92161695a2b039e6e6df767f470fccd563&req=dSUvEs93noJXX%2FMW1HO4zRxEwW5P4llt21D6pckxWMZiQeofwUWxYYayxewJ%0AvFVn2gy3IPmFYnpqa2c%3D%0A)

 

### Rate Limit Use

The Usage page also includes a separate section displaying rate limit use per-model for input and output tokens. You can click the dropdown in the upper left corner of this section to change the model and view related rate limit metrics. These visualizations can be used to determine when you’re hitting peak use for your organization, which specific rate limits need to be increased, and how you can increase your caching rate.

 

**Rate Limit Use + Caching - Input Tokens: **This chart displays the hourly maximum number of uncached input tokens per minute (ITPM) alongside your cache rate (i.e. the percentage of input tokens read from the cache) and your current ITPM rate limit. 

 

**Rate Limit Use - Output Tokens: **This chart displays the hourly maximum number of output tokens per minute (OTPM) alongside your current OTPM rate limit.

 

---

 

## Cost Reporting

The [Cost page](https://platform.claude.com/cost) helps you understand your spending across different models.

 

### Key Features

- **Model-Specific Data**: View costs for individual models or all models combined.
- **Monthly Breakdown**: See costs for specific months.
- **Daily Cost Chart**: Visualize your spending over time.
- **Total Cost Statistics**: Get an overview of your total spending for the selected period, including web search and code execution costs.
- **CSV Export**: Download cost data for your records for further analysis.

### How to Use

1. Choose the Workspace you want to view costs for (or select "All Workspaces").
2. Choose the model you want to view costs for (or select "All Models").
3. Select the month you're interested in.
4. You can see the chart, token cost, and tool use costs, which will update based on your selections.
5. Use the export button to download a CSV of the cost data.

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1584679401/4d0bc8ed08625e1adee414e77030/CleanShot+2025-06-23+at+08_54_40%402x.png?expires=1785248100&signature=8dc44a2a96a718e892aa944751c451631804158fc3a73909edb7ab516686e1dd&req=dSUvEs95lIVfWPMW1HO4zUR%2Bh5nBV9hgCyIF5nuUsbwqZv2rD%2F5oTefPLPZA%0AdSMYrDkGBTsb5ioKClM%3D%0A)

 


---

## Related Articles

- [Claude Console roles and permissions](https://support.claude.com/en/articles/10186004-claude-console-roles-and-permissions)
- [Manage usage credits for paid Claude plans](https://support.claude.com/en/articles/12429409-manage-usage-credits-for-paid-claude-plans)
- [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
- [Claude Code on Console to Enterprise migration](https://support.claude.com/en/articles/14128775-claude-code-on-console-to-enterprise-migration)
- [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
