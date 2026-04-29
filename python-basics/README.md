# Python Basics

> Everything you need to know before (and while) writing your first real Python scripts — explained in plain English.

---

## Who is this for?

You've heard about Python. Maybe you've even installed it. But the moment someone says "activate your virtual environment" or "import a library," your brain goes blank.

This folder is for you.

We start from zero. No prior programming knowledge assumed. Every technical term gets explained in plain English before we use it in code.

---

## What's in here

| File | What you'll learn |
|---|---|
| `01_intro.py` | What Python is, how to run a script, your first `print()` |
| `02_data_types.py` | Numbers, text, lists, and dictionaries — the building blocks of data |
| `03_loops.py` | How to process a list of things automatically (no more copy-paste) |
| `04_functions.py` | How to package up instructions so you can reuse them |
| `05_pandas_first_look.py` | Loading and exploring a real dataset — your first taste of data analytics |

Run them **in order**. Each one builds on the last.

---

## Before you run anything: Set up Python properly

This section covers **virtual environments** — the single best habit you can build as a Python developer. Skip it now, regret it later.

### What is a virtual environment? (Plain English)

Imagine your computer is a kitchen. Python packages (libraries) are ingredients. If every recipe you ever cooked shared the same fridge, ingredients would clash, go missing, or spoil each other. A **virtual environment** is a separate mini-fridge for each project — it keeps one project's ingredients completely isolated from another's.

Without virtual environments, installing a library for one project can quietly break another. With them, each project has exactly what it needs and nothing else.

**Bottom line:** Always use a virtual environment for every Python project. It's two extra commands and saves you hours of mysterious bugs.

---

### Setting up a virtual environment

#### On Mac or Linux

Open your **Terminal** (Mac: press `Cmd + Space`, type "Terminal", press Enter).

```bash
# Step 1: Navigate to your project folder
# Replace "my-project" with wherever your folder actually is
cd my-project

# Step 2: Create a virtual environment
# This creates a folder called "venv" inside your project
python3 -m venv venv

# Step 3: Activate it
# Your terminal prompt will change — you'll see "(venv)" at the start
source venv/bin/activate

# Step 4: Install packages INTO this environment (not globally)
pip install requests pandas matplotlib beautifulsoup4

# Step 5: Run your script as normal
python 01_intro.py

# Step 6: When you're done, deactivate
deactivate
```

> **How do I know it's working?**
> Look at your terminal prompt. When the venv is active, you'll see `(venv)` at the beginning of every line. When you `deactivate`, it disappears.

---

#### On Windows

Open **Command Prompt** (press `Win + R`, type `cmd`, press Enter) or **PowerShell**.

```bat
REM Step 1: Navigate to your project folder
cd my-project

REM Step 2: Create a virtual environment
python -m venv venv

REM Step 3: Activate it (Command Prompt)
venv\Scripts\activate.bat

REM Step 3 (alternative): Activate it in PowerShell
REM venv\Scripts\Activate.ps1

REM Step 4: Install packages
pip install requests pandas matplotlib beautifulsoup4

REM Step 5: Run your script
python 01_intro.py

REM Step 6: Deactivate when done
deactivate
```

> **PowerShell security error?** If you see an error about "running scripts is disabled", run this once:
> `Set-ExecutionPolicy -ExecutionPolicy RemoteSigned -Scope CurrentUser`
> Then try activating again.

---

### The `requirements.txt` file — how professionals share dependencies

When you want to share your project or set it up on another machine, don't send a list of packages in a chat message. Use a `requirements.txt` file instead.

```bash
# Save all currently installed packages to a file
pip freeze > requirements.txt

# On any other machine (after creating and activating a new venv), install everything at once
pip install -r requirements.txt
```

This is the standard way Python projects are shared. When you clone someone's repo and see a `requirements.txt`, that's your shopping list.

---

### Quick-reference cheat sheet

| Task | Mac/Linux | Windows (cmd) |
|---|---|---|
| Create venv | `python3 -m venv venv` | `python -m venv venv` |
| Activate | `source venv/bin/activate` | `venv\Scripts\activate.bat` |
| Deactivate | `deactivate` | `deactivate` |
| Install a package | `pip install package-name` | `pip install package-name` |
| See installed packages | `pip list` | `pip list` |
| Save dependencies | `pip freeze > requirements.txt` | `pip freeze > requirements.txt` |
| Install from file | `pip install -r requirements.txt` | `pip install -r requirements.txt` |

---

## Glossary — technical terms explained

You'll run into these words constantly. Here's what they actually mean.

| Term | Plain English |
|---|---|
| **Python** | A programming language. It's a way of giving instructions to a computer using readable English-like text. |
| **Script** | A text file full of Python instructions. You run it, the computer follows the instructions top to bottom. |
| **Library / Package** | A collection of pre-written code someone else already wrote. Instead of building a car from scratch, you import one. |
| **pip** | Python's package installer. It's like an app store for Python libraries, but free and command-line based. |
| **Virtual environment (venv)** | A self-contained folder that holds Python and its packages for one specific project. Keeps things clean and separate. |
| **Variable** | A named box that stores a value. `price = 49.99` means "create a box called `price` and put `49.99` in it." |
| **String** | Text data. Always wrapped in quotes: `"hello"` or `'world'`. |
| **Integer** | A whole number, no decimal point: `42`, `0`, `-7`. |
| **Float** | A number with a decimal point: `3.14`, `99.9`. |
| **Boolean** | A value that is either `True` or `False`. Named after mathematician George Boole. Used for yes/no decisions. |
| **List** | An ordered collection of items: `["apple", "banana", "cherry"]`. Like a numbered to-do list. |
| **Dictionary** | A collection of key-value pairs: `{"name": "Alice", "age": 30}`. Like a real dictionary — you look up a word (key) to get its definition (value). |
| **Loop** | An instruction to repeat something. "For every item in this list, do X." |
| **Function** | A named, reusable block of instructions. You define it once, call it as many times as you need. |
| **Import** | Loading a library into your script so you can use its tools. `import pandas` is like opening a toolbox. |
| **Module** | A single Python file that contains reusable code. Libraries are made of many modules. |
| **DataFrame** | A table of data in pandas — rows and columns, like a spreadsheet, but in Python. |
| **CSV** | "Comma-Separated Values" — a simple file format for tabular data. Each row is a line; columns are separated by commas. Excel can open them. |
| **JSON** | "JavaScript Object Notation" — a common format for sending data between systems. Looks like a Python dictionary. |
| **API** | "Application Programming Interface" — a way to ask a website or service for data programmatically, without going through a browser. |
| **Web scraping** | Automatically extracting data from web pages using code, instead of copying and pasting manually. |
| **HTML** | The markup language that web pages are built with. Every webpage you see is HTML under the hood. |
| **EDA** | "Exploratory Data Analysis" — the process of loading a dataset and poking around to understand what's in it before doing deeper analysis. |
| **Syntax** | The grammar rules of a programming language. A syntax error means Python couldn't understand your sentence. |
| **Terminal / Command Prompt** | A text-based interface to your computer. You type commands; the computer runs them. No mouse needed. |

---

## Prerequisites

- Python 3.10 or newer installed ([Download here](https://www.python.org/downloads/))
- A terminal or command prompt (instructions above for opening one)
- 30 minutes and a cup of something warm

---

*Run the scripts in order. Read every comment. Break things on purpose. That's how this works.*
