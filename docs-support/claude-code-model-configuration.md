# Claude Code model configuration

*Updated over 2 weeks ago*

---

This guide shows you three ways to change which Claude model you're using with Claude Code: the quick <code>/model</code> command for instant changes, the <code>--model</code> flag for one-time session changes, and environment variables to set your preferred model as the permanent default.

 

## Easiest method: Use /model command

The simplest way to change models is to use the /model command directly within Claude Code. This works immediately without restarting your terminal.

1. Start Claude Code: <code>claude</code>
2. Type <code>/model</code> and choose your desired model from the interactive menu.
3. Your model change takes effect immediately.

## Supported models

- Opus 5, <code>claude-opus-5</code>
- Sonnet 5, <code>claude-sonnet-5</code>
- Fable 5, <code>claude-fable-5</code>
- Opus 4.8, <code>claude-opus-4-8</code>
- Opus 4.7, <code>claude-opus-4-7</code>
- Sonnet 4.6, <code>claude-sonnet-4-6</code>
- Opus 4.6, <code>claude-opus-4-6</code>
- Opus 4.5, <code>claude-opus-4-5-20251101</code>
- Haiku 4.5, <code>claude-haiku-4-5-20251001</code>
- Sonnet 4.5, <code>claude-sonnet-4-5-20250929</code>

 

## Change model for current session only

Use the <code>--model</code> flag when starting Claude Code. 

1. Start a fresh Terminal session.
2. Enter the following commands (depending on the model you’d like to use for that session):
2. - **For Opus 5**: <code>claude --model claude-opus-5</code>
- **For Sonnet 5**: <code>claude --model claude-sonnet-5</code>
- **For Fable 5**: <code>claude --model claude-fable-5</code>
- **For Opus 4.8**: <code>claude --model claude-opus-4-8</code>
- **For Opus 4.7**: <code>claude --model claude-opus-4-7</code>
- **For Sonnet 4.6**:** **<code>claude --model claude-sonnet-4-6</code>
- **For Opus 4.6**:** **<code>claude --model claude-opus-4-6</code>
- **For Opus 4.5**:** **<code>claude --model claude-opus-4-5-20251101</code>
- **For Haiku 4.5: **<code>claude --model** **claude-haiku-4-5-20251001</code>
- **For Sonnet 4.5**: <code>claude --model claude-sonnet-4-5-20250929</code>

 

## Change default model for all future sessions 

**Step 1)** Check your shell type by running: <code>echo $SHELL</code>

- <code>/bin/zsh</code> → You're using zsh (macOS default)
- <code>/bin/bash</code> → You're using bash (Linux default)

**Step 2)** Add model setting to your shell config:

 

### For ZSH users (macOS)

- Opus 5: <code>echo 'export ANTHROPIC_MODEL="claude-opus-5"' >> ~/.zshrc</code>
- Sonnet 5: <code>echo 'export ANTHROPIC_MODEL="claude-sonnet-5"' >> ~/.zshrc</code>
- Fable 5: <code>echo 'export ANTHROPIC_MODEL="claude-fable-5"' >> ~/.zshrc</code>
- Opus 4.8: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-8"' >> ~/.zshrc</code> 
- Opus 4.7: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.zshrc</code> 
- Sonnet 4.6: <code>echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.zshrc</code>
- Opus 4.6: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.zshrc</code>
- Opus 4.5: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.zshrc</code>
- Haiku 4.5: <code>echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.zshrc</code>
- Sonnet 4.5: <code>echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.zshrc</code>

 

### For BASH users (Linux)

- Opus 5: <code>echo 'export ANTHROPIC_MODEL="claude-opus-5"' >> ~/.bashrc</code>
- Sonnet 5: <code>echo 'export ANTHROPIC_MODEL="claude-sonnet-5"' >> ~/.bashrc</code>
- Fable 5: <code>echo 'export ANTHROPIC_MODEL="claude-fable-5"' >> ~/.bashrc</code>
- Opus 4.8: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-8"' >> ~/.bashrc</code>
- Opus 4.7: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-7"' >> ~/.bashrc</code>
- Sonnet 4.6: <code>echo 'export ANTHROPIC_MODEL="claude-sonnet-4-6"' >> ~/.bashrc</code>
- Opus 4.6: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-6"' >> ~/.bashrc</code>
- Opus 4.5: <code>echo 'export ANTHROPIC_MODEL="claude-opus-4-5-20251101"' >> ~/.bashrc</code>
- Haiku 4.5: <code>echo 'export ANTHROPIC_MODEL="claude-haiku-4-5-20251001"' >> ~/.bashrc</code>
- Sonnet 4.5: <code>echo 'export ANTHROPIC_MODEL="claude-sonnet-4-5-20250929"' >> ~/.bashrc</code>

 

**Step 3)** Apply the changes:

- For ZSH: <code>source ~/.zshrc</code>
- For BASH: <code>source ~/.bashrc</code>

**Step 4)** Close Terminal completely, then reopen it.

 

**Step 5)** Start Claude Code in a fresh Terminal session: <code>claude</code>.

 

Now your chosen model will be the default for all future Claude Code sessions.


---

## Related Articles

- [How up-to-date is Claude's training data?](https://support.claude.com/en/articles/8114494-how-up-to-date-is-claude-s-training-data)
- [Model availability in Claude for Government](https://support.claude.com/en/articles/14503794-model-availability-in-claude-for-government)
- [Models, usage, and limits in Claude Code](https://support.claude.com/en/articles/14552983-models-usage-and-limits-in-claude-code)
- [Why Claude switched models in your conversation with Fable 5](https://support.claude.com/en/articles/15363606-why-claude-switched-models-in-your-conversation-with-fable-5)
- [Why Claude switched models in your conversation with Opus 5](https://support.claude.com/en/articles/16049681-why-claude-switched-models-in-your-conversation-with-opus-5)
