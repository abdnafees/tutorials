# AGENTS.md

Instructions for AI coding agents (Codex, Cursor, Copilot, Claude, or any other agent) working in this repository.

---

## Context

This is **tutorials** — an educational repository for a Data Analytics Bootcamp. The target audience is **muggles**: people with basic computer literacy (they can open a browser and download a file) but no programming background whatsoever.

**Clarity over sophistication, always.** A clean, readable 20-line script beats a clever 5-line one every single time in this repo.

---

## Repo structure

```
tutorials/
├── README.md
├── CLAUDE.md
├── AGENTS.md
├── web-scraping/
├── python-basics/
├── sql-essentials/
├── power-bi/
├── excel-for-humans/
├── data-cleaning/
├── api-101/
├── automation-no-code/
└── ai-for-analytics/
```

Each topic folder contains numbered Python scripts, a README, a `data/` folder, and a `challenge/` subfolder (details below).

---

## Content generation rules

- **Audience has basic computer literacy but zero programming background.** Do not assume they know what a function, a variable, or a loop is until the tutorial introduces it.
- **Explain terms on first use.** Define every technical term the first time it appears — inline, in plain English.
- **Use analogies before definitions.** Introduce a concept with a real-world comparison, then give the technical definition. Never the other way around.
- **Heavy code comments.** Comment every non-trivial line. Comments should explain *why* something is done, not just *what* the line does.
- **Every file must be self-contained.** A learner should be able to download a single `.py` file, run it, and have it work — without needing other files from the repo (unless the tutorial explicitly teaches imports).

---

## Code standards

- **Python 3.10+** — use modern Python syntax, but nothing bleeding-edge that adds confusion.
- **No formatter enforced.** Readability trumps PEP 8 compliance. Don't auto-format in a way that makes code harder to read for beginners.
- **Minimize external packages.** Use the standard library when possible. When third-party packages are needed, add a `# pip install package-name` comment at the top of the file.
- **No type hints in tutorial code.** They are visual noise for beginners and will cause confusion before they've learned what a type is.
- **No classes unless the tutorial is explicitly about OOP.** Functions and simple procedural code only.
- **Prefer `print()` over `return` values.** Learners need to *see* output. Silent functions feel broken to someone who doesn't know how to inspect a return value.

---

## File naming

- **Numbered prefixes for scripts:** `01_intro.py`, `02_variables.py`, `03_loops.py` — always two digits so they sort correctly.
- **Lowercase with hyphens for folders:** `web-scraping/`, `python-basics/`, `api-101/`.
- **`README.md` is mandatory in every tutorial folder.** It should include: what this tutorial covers, prerequisites, and a brief agenda of what each numbered script does.

---

## Testing

There is **no formal test suite** in this repo.

- Verify scripts by running them: `python 01_intro.py`
- Every script must produce **visible terminal output** — if it runs silently, add a `print()`.
- Include **expected output as comments** at the bottom of scripts where it's helpful:
  ```python
  # Expected output:
  # Tokyo, Japan — Pop: 13,960,000
  # Delhi, India — Pop: 11,034,555
  ```

---

## What NOT to do

- **No CI/CD.** No GitHub Actions, no automated testing pipelines. Keep it simple.
- **No pre-commit hooks.** Don't add linters, formatters, or hooks that could confuse contributors.
- **No DRY refactoring at the expense of step-by-step clarity.** If repeating three lines makes a script easier to follow, repeat them. Don't extract a helper function to save lines.
- **No design patterns.** No factories, no singletons, no abstract base classes. Just plain functions and variables.
- **No root `requirements.txt`.** Each tutorial is self-contained; install instructions live inside the scripts themselves.
- **Never commit API keys.** Not even test keys, not even keys with no permissions. Use placeholder strings like `"YOUR_API_KEY_HERE"` and add a comment pointing to where learners can get their own.

---

## Adding a new tutorial

Follow this checklist every time:

1. **Create the folder** using lowercase with hyphens: `mkdir topic-name/`
2. **Add a `README.md`** inside the folder: what it covers, prerequisites, script-by-script agenda.
3. **Add numbered scripts** starting from `01_`: one concept per file, heavy comments, `print()` output, self-contained.
4. **Add a `data/` subfolder** if the tutorial uses sample datasets. Include the data files — don't link to external downloads only.
5. **Add a `challenge/` subfolder** with a `README.md` describing open-ended tasks. No solutions in the repo.
6. **Update the root `README.md` table** if the topic folder is new and not already listed.

---

## Commit message format

- Present tense
- Prefixed with the folder name
- One line

**Examples:**
```
web-scraping: add pagination tutorial
python-basics: fix typo in 02_variables.py
api-101: add dummyjson example
data-cleaning: add challenge tasks
```
