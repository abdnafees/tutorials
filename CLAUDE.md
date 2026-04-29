# CLAUDE.md

Instructions for Claude (via Claude Code, the API, or any Anthropic-powered tool) when working in this repository.

---

## About this repo

This is **tutorials** — a collection of hands-on data tutorials for a Data Analytics Bootcamp. The audience is non-technical to mildly technical learners we affectionately call **muggles**: smart people who just haven't been exposed to this stuff yet.

Your job when contributing here is not to show off. It's to make things clear.

---

## Writing style rules

- **Explain like you're talking to a smart friend who has never coded.** Not a colleague. Not a student. A friend.
- **No unexplained jargon.** If you use a technical term, define it immediately — in plain English, not with another technical term.
- **Use everyday analogies before you introduce a concept.** A DataFrame is like a spreadsheet. An API is like a waiter who takes your order to the kitchen. Start there.
- **Code comments explain *why*, not just *what*.** `# loop through each row` is useless. `# we loop because pandas doesn't know which city we care about — we have to tell it` is useful.
- **Short paragraphs.** One idea per paragraph. Two sentences is fine. Five is getting long.
- **Humor is welcome.** Condescension is not. There's a difference between a friendly joke and making someone feel dumb for not knowing something.

---

## Code style rules

- **Python is the primary language** across all tutorials.
- **Every script must be self-contained and runnable** from top to bottom with a single `python filename.py`. No imports from other scripts in the same folder unless explicitly part of the tutorial.
- **Include pip install instructions as a comment at the top** of every script that uses external libraries:
  ```python
  # pip install requests
  ```
- **Use `print()` generously.** Learners need to see things happening. Silent scripts feel broken.
- **Avoid clever one-liners.** `[x for x in things if condition]` is valid Python. It is not valid tutorial Python. Write it as a loop until the tutorial is specifically about list comprehensions.
- **Use obvious variable names.** `book_titles` not `bt`. `user_age` not `ua`. `products_list` not `pl`. Name things like you'll forget what they are in a week — because the learner definitely will.

---

## Tutorial folder structure

Every tutorial folder should look like this:

```
topic-name/
├── README.md           ← Overview, agenda, learning goals
├── 01_intro.py         ← First concept — the "why" and a simple example
├── 02_next_step.py     ← Builds on the first file
├── 03_...py
├── data/               ← Sample datasets (CSV, JSON, etc.)
└── challenge/          ← Open-ended tasks for learners to try solo
    └── README.md       ← Challenge descriptions (no solutions here)
```

---

## Rules for creating new tutorials

1. **Start with the "why."** Before any code, answer: why would a real person need this skill? What problem does it solve?
2. **Show something relatable before you show code.** A screenshot, a real-world scenario, a question the learner has probably asked themselves.
3. **One new concept per script.** If you're introducing loops, don't also introduce functions in the same file. Save that for the next script.
4. **End with a challenge.** Give learners something to try on their own — open-ended enough to require thought, bounded enough to be achievable in 15–20 minutes.
5. **Include backup URLs.** External websites go down. If a tutorial depends on a live URL, include at least one fallback in the comments.

---

## Things to avoid

- **Don't assume students know what a terminal is.** If they need to open one, tell them how.
- **Don't use `lambda`, list comprehensions, or decorators without explaining them first.** These are intermediate Python features that look like magic to beginners.
- **Don't skip error handling in scripts that make network calls.** Show `try/except` blocks — and explain what they're for.
- **Don't require paid API keys without flagging the cost.** If an example uses OpenAI or Anthropic, clearly mark it with a `# NOTE: this requires a paid API key` comment and suggest a free alternative where possible.
- **Don't reference internal or organisation-specific systems**, internal URLs, Slack channels, or anything that an external learner wouldn't have access to.
