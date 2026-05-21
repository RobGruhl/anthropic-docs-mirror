# Our approach to rate limits for the Claude API

*Updated over 2 months ago*

---

Your rate limit depends on your usage tier, and is currently measured in three key metrics:

1. Requests per minute (RPM)
2. Input tokens per minute (ITPM)
3. Output tokens per minute (OTPM)

If you exceed any of these rate limits, you will get a 429 error describing which rate limit was exceeded, along with a <code>retry-after</code> header indicating how long to wait.

 

Rate limits are set at the organization level and are defined by usage tiers. Each tier has different spend and rate limits, with automatic tier advancement based on usage thresholds up to Tier 4.

 

You can view your organization's current tier and limits in the [Claude Console](https://platform.claude.com).

 

More information on usage tiers and rate limits can be found in [our Claude docs](https://docs.claude.com/en/api/rate-limits).


---

## Related Articles

- [Cost and Usage Reporting in the Claude Console](https://support.claude.com/en/articles/9534590-cost-and-usage-reporting-in-the-claude-console)
- [How can I advance my Claude API usage to Tier 2?](https://support.claude.com/en/articles/10366389-how-can-i-advance-my-claude-api-usage-to-tier-2)
- [Get started with the Claude Enterprise Analytics API](https://support.claude.com/en/articles/13694757-get-started-with-the-claude-enterprise-analytics-api)
- [Claude Enterprise Analytics API reference guide](https://support.claude.com/en/articles/13703965-claude-enterprise-analytics-api-reference-guide)
- [Claude Enterprise consumption guide](https://support.claude.com/en/articles/14782391-claude-enterprise-consumption-guide)
