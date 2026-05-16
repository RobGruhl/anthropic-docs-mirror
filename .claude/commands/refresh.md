---
description: Pull the latest docs from the remote repository
allowed-tools: Bash(git pull:*), Bash(git status)
---

# Refresh Local Docs

Pull the latest documentation from the remote repository.

## Steps

### Step 1: Pull latest changes

```bash
git pull --ff-only
```

If the fast-forward pull fails (due to local changes), inform the user and suggest:
- `git stash && git pull && git stash pop` if they want to keep local changes
- `git reset --hard origin/main` if they want to discard local changes (confirm first)

### Step 2: Report what changed

Run `git log --oneline HEAD@{1}..HEAD` to show what commits were pulled, and give the user a brief summary.

If already up to date, just say so.
