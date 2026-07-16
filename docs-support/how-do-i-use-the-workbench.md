# How do I use the Workbench?

*Updated over 2 weeks ago*

---

 

## What is Workbench?

Workbench is built directly on the public **[Messages API](https://platform.claude.com/docs/en/build-with-claude/working-with-messages)**, so the request you build in Workbench is the same request you'll send in your code. 

 

Use it to:

- Try a model or a new API feature before you write any code
- Iterate on a prompt and inspect the full response
- Learn how API requests and responses are structured
- Export your work as a code snippet you can run in your own application

Workbench doesn't store your prompts or conversations on Anthropic's servers. Your current draft stays in your browser, and you can go to the "code" tab to keep a copy of any request.

 

## Open Workbench

1. Log in to the **[Claude Console](https://platform.claude.com/)**.
2. Select "Workbench" in the navigation.
3. If your organization uses workspaces, choose the workspace you want to work in.

 

## Write and run a request

1. Enter a user message in the prompt area. You can also add a system prompt to set instructions or context.
2. Click "Run" to send the request.
3. Review Claude's response, along with the token counts and usage shown for the request.
4. Edit your prompt and run it again to keep iterating.

Workbench also includes example templates you can load and modify.

 

## Choose a model and adjust settings

Use the model selector to switch between Claude models, and open the model settings to adjust parameters like temperature and maximum output tokens. 

 

Running the same prompt with different models or settings is a quick way to see how the response changes. As you think about building your application with the Messages API, use the workbench to understand the power of the models. 

 

## Use tools and structured outputs

Add tool definitions to your request to test tool use, and use structured outputs to have Claude return data in a shape you define. Workbench shows tool calls and tool results in the response, so you can see exactly how they're represented in the API.

 

## View the raw request and response

Workbench can show the raw API request and response, including the full message structure, stop reason, and usage. This is the same shape your application sends and receives and is a practical way to try out the features of the Messages API.

 

## Turn your work into code

Click the "code" toggle to export your current request as a code snippet. The snippet reflects exactly what you've tested in the Workbench, so you can paste it into your project and run it with your own API key.

 

Code examples in our documentation include an "Open in Workbench" option, which loads the example into Workbench so you can run and modify it.

 

---

 

## How do I use Workbench (legacy)?

Workbench (legacy) allows you to create and test prompts within your Claude Console account. You can enter your prompt into the "Human" dialogue box and click "Run" to test Claude's output. Click on the + icon in the upper left to create a new prompt, or click on the bulleted list icon to see prompts you've tested in the past:

 

![image](https://downloads.intercomcdn.com/i/o/888021849/31a22a0dc4d1fc4b605cc8ee/Screenshot+2023-11-19+at+4.21.51+PM.png?expires=1784220300&signature=a49c8fa0ea7c06ffab56031bede9a75372b97f975b5939aa541e978eac0f7463&req=fCgvFst%2FlYVWFb4f3HP0gKWhcDkO0kVbOkmmaOsi7ICznBYzmCCjTS9waCqM%0A8AZ6rNxspIlhf5G0Ww%3D%3D%0A)

 

Workbench (legacy) also allows you to configure several settings when prompting Claude. You can click on the slider icon to review your model settings. This allows you to select the model, temperature, and max tokens to sample:

 

![image](https://downloads.intercomcdn.com/i/o/888023061/61e26396355f6f6cd506d7e4/Screenshot+2023-11-19+at+4.09.28+PM.png?expires=1784220300&signature=8e6c066c60cc3ad1b59ba3459018ad158cfa1a67c7710154ab63f13c931e4f2e&req=fCgvFst9nYdeFb4f3HP0gN55XdDSOYe3DUq7%2BRvcmSMY%2B6S1Otakg4rfWAKP%0AnXciV5Wt1sqWv%2BhWPw%3D%3D%0A)

 

After crafting your prompt, click on the "Get code" button to generate a sample using our Python and Typescript SDKs:

 

![image](https://downloads.intercomcdn.com/i/o/888023545/b12afe07f16f079daff7587d/Screenshot+2023-11-19+at+4.28.27+PM.png?expires=1784220300&signature=5af28ff589a69400e20429ec08abed271e83b5e84da180cb4eaa8fd1f8948926&req=fCgvFst9mIVaFb4f3HP0gEZTsDqc4ufrRWixPJbjiQdexEJMgajmgVq%2FGled%0A49iB%2FSkrLq4U8X5x%2FQ%3D%3D%0A)

 

## How can I access my previous work and prompt history in Workbench (legacy)?

You can access your previous Workbench prompts on your Console account by following these steps:

 

1. Log in at platform.claude.com.

2. Navigate to your [Workbench](https://platform.claude.com/workbench).

3. Click the "List prompts" button on the upper left corner of the page, next to the "+" button to create a new prompt:

 

![image](https://downloads.intercomcdn.com/i/o/lupk8zyo/1945992985/45a8969fb6cec956bd44fb5c4ba7/CleanShot+2026-01-15+at+12_07_22%402x.png?expires=1784220300&signature=4109c4ffe6a97c6f1705759e800fd401ebeb13e8c56719017feef2cecf8394c3&req=dSkjE8B3n4hXXPMW1HO4zQQ9sFULNXO7TyGSpkcb8MUniAnQeDiEWL%2BTRPfN%0AJYUDIJR7xiEU7QxIMzg%3D%0A)

 

4. A list of your previously-saved prompts will appear.

5. You can use the search bar at the top of the prompt list if you're looking for something specific.

 

---

 

## Frequently asked questions

### What’s changing in Workbench?

We’re refreshing Workbench to be a simpler, stateless way to try Claude models and API features in the Console. The main differences are that it now:

- It doesn't store your work on Anthropic's servers. Your current draft stays in your browser, and you can export any request as code. With Workbench (legacy) you were able to save prompts, prompt history, and run evals. 
- It is built directly on the public Messages API and shows the full request and response, so what you see matches what your code sends and receives.
- Saved prompts, prompt versions, evals, and prompt sharing aren't part of the refreshed Workbench. Use the export function in the legacy version to download your data. 

 

### Will Workbench (legacy) keep working for me right now?

Yes, it keeps working until further notice. You'll see a banner in Workbench pointing to the legacy version if you choose to use it, and you'll get notice of any deprecation plans whether anything changes for your account.

 

### What happens to my saved prompts and evals?

They stay in Workbench (legacy) for now. Use the Export option in Workbench (legacy) to download them before then. The refreshed Workbench doesn't include saved prompts or evals, so keep your exported copies in your own tools, such as the repository where your application code lives.

 

### How do I get access to my existing data from Workbench (legacy)?

Your saved prompts and completions are still available in Workbench (legacy) today. You'll see an Export option in Workbench (legacy) that lets you download your saved prompts, prompt revisions, and completions. 

 

### Can I import my Workbench (legacy) data into refreshed Workbench?

No. The refreshed version of Workbench doesn't save prompts or conversations, so there's nothing to import into. The export gives you a copy of your Workbench data so you can keep it or move it into your own tools.


---

## Related Articles

- [Business Associate Agreements (BAA) for Commercial Customers](https://support.claude.com/en/articles/8114513-business-associate-agreements-baa-for-commercial-customers)
- [How do I pay for my Claude API usage?](https://support.claude.com/en/articles/8977456-how-do-i-pay-for-my-claude-api-usage)
- [What are artifacts and how do I use them?](https://support.claude.com/en/articles/9487310-what-are-artifacts-and-how-do-i-use-them)
- [View usage analytics for Team and Enterprise plans](https://support.claude.com/en/articles/12883420-view-usage-analytics-for-team-and-enterprise-plans)
- [Enable US-only inference for your organization](https://support.claude.com/en/articles/15422948-enable-us-only-inference-for-your-organization)
