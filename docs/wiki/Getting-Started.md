# Getting Started with Oracle

This guide takes you from zero to your first generated test.
It should take about five minutes.

## Prerequisites

You'll need:

- Python 3.11 or later (`python --version` to check)
- An Anthropic API key ([console.anthropic.com][anthropic])
- Git

[anthropic]: https://console.anthropic.com

## Step 1: Install Oracle

```bash
git clone https://github.com/bri-stevenski/oracle-test-ai-agent.git
cd oracle-test-ai-agent
pip install -e .
```

Verify the install worked:

```bash
oracle version
```

You should see: `Oracle AI v0.1 (MVP)`

## Step 2: Set Your API Key

Oracle uses Claude (Anthropic) by default. Set your key in your
shell before running any generation commands:

```bash
export ANTHROPIC_API_KEY="sk-ant-..."
```

To make this permanent, add that line to your `~/.zshrc` or
`~/.bashrc`.

> **Using a different provider?** See
> [LLM Providers & Configuration](LLM-Providers-and-Configuration.md)
> for OpenAI and Gemini setup.

## Step 3: Generate Your First Test

Run this command (swap in whatever you'd like to test):

```bash
oracle generate "Test that GET /api/health returns 200"
```

Oracle will:

1. Classify the intent (API test)
2. Pick the best framework (pytest)
3. Generate a test file
4. Print the path to the file

The output looks something like:

```text
Oracle Processing Request...

Test Type: api
Framework: pytest

Reasoning:
 - HTTP endpoint test maps to API category
 - Python ecosystem detected, pytest preferred

Output File:
tests/generated/api/test_api_health_get_200.py
```

## Step 4: Look at the Generated File

Open the file Oracle just created:

```bash
cat tests/generated/api/test_api_health_get_200.py
```

Read through it. Check that:

- The endpoint matches what you intended
- The assertion matches the expected behavior
- There are no placeholder values you need to fill in

## Step 5: Run the Test

Run it immediately with the `--run` flag (or execute manually
with pytest):

```bash
oracle generate "Test that GET /api/health returns 200" --run
```

Or, if you already have the file:

```bash
pytest tests/generated/api/test_api_health_get_200.py
```

## What Happens to Generated Tests

Generated tests live in `tests/generated/` — a scratch space
that is **not** committed to git. They're yours to review and
run freely.

Once a test passes review, you can promote it into the committed
test suite. See the
[oracle-promote-test][promote-skill] skill for
the full promotion checklist.

[promote-skill]: ../skills/claude-code/oracle-promote-test/SKILL.md

## Want a Preview Without Generating?

Use `--recommend-only` to see what Oracle would pick without
calling the LLM (no API key needed):

```bash
oracle generate "load test the search endpoint" --recommend-only
```

This is useful for understanding Oracle's routing logic before
committing to a full generation.

## Next Steps

- [Writing Good Prompts](Writing-Good-Prompts.md) — get the
  test you actually want on the first try
- [For Manual Testers](For-Manual-Testers.md) — if you're
  coming from a manual testing background
- [Troubleshooting](Troubleshooting.md) — if something
  went wrong above
