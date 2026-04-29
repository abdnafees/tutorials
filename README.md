# tutorials

> Hands-on tutorials for people who don't speak fluent tech — yet.

---

## Who is this for?

This repo is for **muggles** — people who haven't discovered their data powers yet — and for the trainers and advanced self-learners who want to help them get there.

More specifically, you'll feel right at home here if you are:

- **A complete beginner** who has never written a line of code and finds words like "repository" mildly terrifying (don't worry, you'll be fine).
- **A spreadsheet wizard** who lives in Excel or Google Sheets and suspects there might be a better way to do *some* of this stuff.
- **A curious non-coder** — maybe you're in ops, marketing, finance, or HR — who keeps getting handed datasets and wants to actually *do* something with them.
- **A trainer or advanced self-learner** looking for structured, well-commented material you can use, adapt, or build on.

No CS degree required. No prior coding experience required. Just a willingness to try things, break things, and try again.

---

## What's inside

| Folder | What you'll learn |
|---|---|
| `web-scraping/` | How to pull data off websites automatically — no copy-pasting required |
| `python-basics/` | Python from zero: variables, loops, functions, and "wait, this is actually useful" moments |
| `sql-essentials/` | How to ask a database questions in plain(-ish) English using SQL |
| `power-bi/` | Turning raw numbers into dashboards your boss will actually look at |
| `excel-for-humans/` | Excel tricks that will make your colleagues ask "how did you do that?" |
| `data-cleaning/` | Because real-world data is always messy, and someone has to fix it |
| `api-101/` | What APIs are, why they matter, and how to talk to them without a translator |
| `automation-no-code/` | Automating repetitive tasks without writing a single line of code |
| `ai-for-analytics/` | Using AI tools (ChatGPT, Claude, etc.) as your data co-pilot |

---

## How each tutorial works

Every tutorial folder follows the same structure so you always know where to look:

```
topic-name/
├── README.md          ← Agenda, learning goals, and what to expect
├── 01_intro.py        ← First concept — start here
├── 02_next_step.py    ← Builds on the previous file
├── ...
├── data/              ← Sample datasets used in the tutorial
└── challenge/         ← Your turn — open-ended tasks to try solo
```

- **Numbered scripts** — run them in order; each one is self-contained with comments explaining what's happening and *why*.
- **Comments are your friends** — we write them assuming you haven't seen this before.
- **Challenges** — no solutions provided. Google is allowed. Asking questions is encouraged.

---

## Running the code

You'll need Python installed. If you don't have it yet:
👉 [Download Python](https://www.python.org/downloads/) (get the latest 3.x version)

Most tutorials use a handful of common libraries. Install them once and you're set:

```bash
pip install requests pandas matplotlib beautifulsoup4
```

If a tutorial needs something extra, the script will tell you at the top.

---

## Contributing

Are you a **trainer or TA**? Great — contributions are welcome.

The rules are simple:

1. Follow the folder structure above. Consistency is kindness.
2. Write like you're explaining to a smart friend who has never coded. Not like you're writing documentation.
3. Open a PR with a clear title (e.g. `web-scraping: add pagination tutorial`).
4. **Golden rule:** if your explanation needs an explanation, simplify it.

---

*MIT License — use it, share it, remix it.*
