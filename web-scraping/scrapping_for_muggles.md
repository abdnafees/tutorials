# Web Scraping Session — Trainer Content Guide

**Session:** Friday, 7:00–9:00 PM
**Audience:** Data Analytics Bootcamp students (Python basics covered)

---

## Python Foundations — Quick Reference

New to Python or just a bit rusty on any of the concepts below? Every term used in this session has a dedicated explanation in the [`../python-basics/`](../python-basics/) folder. Point students there before the session or use it as a reference when questions come up.

| Concept used in this session | Where to learn it |
|---|---|
| Variables, `print()`, f-strings | [`01_intro.py`](../python-basics/01_intro.py) |
| Strings, numbers, lists, **dictionaries**, booleans, **JSON** | [`02_data_types.py`](../python-basics/02_data_types.py) |
| `for` loops, filtering, building result lists | [`03_loops.py`](../python-basics/03_loops.py) |
| Writing and reusing functions | [`04_functions.py`](../python-basics/04_functions.py) |
| Glossary: API, JSON, HTML, library, module, EDA, CSV… | [`README.md — Glossary`](../python-basics/README.md#glossary--technical-terms-explained) |
| Setting up `venv` + `pip` on Mac/Linux and Windows | [`README.md — venv setup`](../python-basics/README.md#before-you-run-anything-set-up-python-properly) |

---

## Part 1: The Hidden API Hunt (30 min)

### Key Concept
Most modern websites don't render data from HTML — they fetch it from internal APIs as JSON. You can intercept these requests and skip HTML parsing entirely.

> 🔤 **New to these terms?**
> - **HTML** — the markup language every webpage is built with. Your browser reads it and turns it into the page you see. See the [glossary](../python-basics/README.md#glossary--technical-terms-explained).
> - **API** — a way to ask a web server for data directly, without going through a browser. Like calling the kitchen directly instead of using the menu. See the [glossary](../python-basics/README.md#glossary--technical-terms-explained).
> - **JSON** — the format APIs use to send data back. It looks *exactly* like a Python dictionary. See [`02_data_types.py`](../python-basics/02_data_types.py) — the Dictionaries section.

### Setup
Students need:
- Chrome or Edge browser
- Python with `requests` and `json` (both pre-installed)

> 📦 **What are libraries?** A library is pre-written code that someone else built and shared for free — you just `import` it and use it. `requests` lets Python make web requests; `json` lets Python read and write JSON data. New to libraries or `pip`? See the [glossary](../python-basics/README.md#glossary--technical-terms-explained) and the [venv setup guide](../python-basics/README.md#before-you-run-anything-set-up-python-properly).

### Live Demo — Target Websites

**Website 1: Books to Scrape (Warm-up)**
- URL: `https://books.toscrape.com/`
- This is a classic training site — show the BS4 way first (5 min), then say "now forget all of that."

**Website 2: GitHub Jobs / Repositories API**
- URL: `https://api.github.com/search/repositories?q=python&sort=stars`
- Open the URL directly in the browser — clean JSON, no scraping needed.
- Key point: many sites have public APIs you can just *ask* nicely.

```python
import requests   # library that lets Python fetch data from URLs — see ../python-basics/README.md
import json       # library for parsing JSON into Python dicts/lists — see ../python-basics/02_data_types.py

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "data analytics", "sort": "stars", "per_page": 10}
    # params is a dictionary — Python key-value pairs — see ../python-basics/02_data_types.py
)

data = response.json()   # converts the JSON response into a Python dictionary

for repo in data["items"]:   # loop through the list at key "items" — see ../python-basics/03_loops.py
    # data["items"] — dictionary key access — see ../python-basics/02_data_types.py
    # f"..." — f-string, embeds variable values in text — see ../python-basics/01_intro.py
    print(f"{repo['name']} — ⭐ {repo['stargazers_count']} — {repo['html_url']}")
```

**Website 3: Finding the Hidden API (The Wow Moment)**
- URL: `https://dummyjson.com/` (simulates a real e-commerce backend)
- But pretend this is a real site. Walk through the DevTools method:

### DevTools Steps (show on screen)
1. Open any dynamic website (or `https://dummyjson.com/products`)
2. Right-click → Inspect → **Network** tab
3. Filter by **Fetch/XHR**
4. Reload the page
5. Click on requests appearing — look at the **Response** tab
6. Find the JSON payload — that's your data

> 💡 **What does that JSON actually look like?** It's a nested structure of curly braces `{}` (dictionaries) and square brackets `[]` (lists) — identical to Python dictionaries and lists. If that's unfamiliar, work through [`02_data_types.py`](../python-basics/02_data_types.py) before this session.

```python
# Once you find the hidden endpoint
response = requests.get("https://dummyjson.com/products?limit=10")
products = response.json()["products"]   # ["products"] gets the list at the "products" key
                                         # see ../python-basics/02_data_types.py

for p in products:   # loop through each product dictionary — see ../python-basics/03_loops.py
    # p['title'], p['price'], p['rating'] — dictionary key access
    # f"..." — f-string — see ../python-basics/01_intro.py
    print(f"{p['title']} | ${p['price']} | Rating: {p['rating']}")
```

**Website 4: Real-World Practice — Quotable API**
- URL: `https://api.quotable.io/quotes?page=1`
- Students fetch quotes, authors, and tags — easy to loop through pages.

```python
response = requests.get("https://api.quotable.io/quotes", params={"page": 1, "limit": 5})
# params is a dictionary — see ../python-basics/02_data_types.py
data = response.json()

for quote in data["results"]:   # loop through a list — see ../python-basics/03_loops.py
    # quote["content"] and quote["author"] — dictionary key access — see ../python-basics/02_data_types.py
    print(f'"{quote["content"]}" — {quote["author"]}')
```

### Key Takeaway to Emphasize
> "Before you write a single line of scraping code, check the Network tab. 8 out of 10 times, the data is already sitting there in JSON."

---

## Part 2: Playwright — The Selenium Killer (25 min)

### Key Concept
Playwright is faster, more reliable, auto-waits for elements (no `time.sleep`), and has a codegen tool that writes code by recording your clicks.

> 🔤 **New to these terms?**
> - **Library / package** — pre-written code you install and `import`. `playwright` is a library for controlling a real browser from Python. See the [glossary](../python-basics/README.md#glossary--technical-terms-explained).
> - **`pip install`** — the command that downloads and installs Python libraries. Always run it inside an activated `venv`. See the [venv setup guide](../python-basics/README.md#before-you-run-anything-set-up-python-properly).
> - **JavaScript** — a different programming language that runs *inside the browser* and builds page content dynamically. `requests` fetches a page's raw HTML before JS runs; Playwright launches a real browser so JS has time to execute first.

### Installation (have students run this at the start of session or during break)
```bash
pip install playwright
playwright install chromium
```

### Demo 1: Basic Scraping with Playwright

Target: `https://quotes.toscrape.com/js/` (this site requires JavaScript — BS4 can't handle it, Selenium can but painfully)

> 📖 The code below uses `from ... import` to load part of a library, and a `for` loop to process each scraped element. Unfamiliar with either? See [`04_functions.py`](../python-basics/04_functions.py) for functions/imports context and [`03_loops.py`](../python-basics/03_loops.py) for loops.

```python
from playwright.sync_api import sync_playwright   # import one specific tool from the playwright library

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False so students can watch
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")

    # Auto-waits for elements — no sleep needed
    quotes = page.query_selector_all(".quote")

    for q in quotes:   # loop through each scraped element — see ../python-basics/03_loops.py
        text = q.query_selector(".text").inner_text()
        author = q.query_selector(".author").inner_text()
        # f"..." — f-string, embeds variables in text — see ../python-basics/01_intro.py
        print(f"{text} — {author}")

    browser.close()
```

### Demo 2: The Codegen Magic Trick

This is the moment that gets reactions. Run this in the terminal:

```bash
playwright codegen https://quotes.toscrape.com/
```

- A browser opens AND a code window opens side by side
- Every click, type, and scroll you do gets recorded as Python code
- Click around, select elements, fill forms — code writes itself
- Copy the generated code, paste it in your script, done

**Let students try this for 5 minutes on any website they choose.**

### Demo 3: Screenshots and PDFs

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch()
    page = browser.new_page()
    page.goto("https://books.toscrape.com/")

    # Screenshot
    page.screenshot(path="bookstore.png", full_page=True)

    # PDF (only in headless Chromium)
    page.pdf(path="bookstore.pdf")

    browser.close()
```

### Playwright vs Selenium — Quick Comparison to Mention

| Feature | Selenium | Playwright |
|---|---|---|
| Auto-wait | No (`time.sleep`) | Yes, built-in |
| Speed | Slower | Significantly faster |
| Codegen | No | Yes (`playwright codegen`) |
| Multi-browser | Yes | Yes (Chromium, Firefox, WebKit) |
| Setup pain | WebDriver downloads | One command |

---

## Part 3: LLM-Assisted Scraping (25 min)

### Key Concept
Instead of writing CSS selectors or XPath for messy pages, feed the raw HTML to an LLM and ask it to extract structured data. The AI *understands* the page like a human would.

> 🔤 **New to these terms?**
> - **CSS selectors** — patterns that target specific HTML elements, like `.price` or `h1.title`. They are how BS4 and Playwright find things on a page.
> - **XPath** — an alternative way of navigating HTML/XML structure, e.g. `//table[@class='wikitable']`.
> - **LLM** — "Large Language Model" — the AI behind tools like ChatGPT and Claude. Here we send it raw HTML and ask it to extract data in structured form.
> - **HTML** — the markup code every webpage is built from. See the [glossary](../python-basics/README.md#glossary--technical-terms-explained).
> - **Structured data** — data organised into a predictable shape (like rows and columns, or a list of dictionaries) rather than a wall of unformatted text.

### Setup
Students need an API key for OpenAI or Anthropic (provide a shared key for the session if possible), or use the free tier.

```bash
pip install openai
# or
pip install anthropic
```

### Demo — Scraping an Unstructured Page

**Target: A Wikipedia page (messy HTML, dense tables)**
- URL: `https://en.wikipedia.org/wiki/List_of_largest_cities`

**Step 1: Grab the raw HTML (just the relevant section)**

```python
import requests                        # library for making web requests
from bs4 import BeautifulSoup          # library for parsing HTML — "BS4" for short

response = requests.get("https://en.wikipedia.org/wiki/List_of_largest_cities")
soup = BeautifulSoup(response.text, "html.parser")
# response.text is a string containing the full HTML of the page
# BeautifulSoup parses it so we can search and navigate it

# Grab just the first big table to keep tokens manageable
table = soup.find("table", {"class": "wikitable"})
# soup.find() searches for an HTML element matching the criteria
# {"class": "wikitable"} is a dictionary of HTML attributes to match
# see ../python-basics/02_data_types.py for dictionaries
table_html = str(table)[:4000]  # Truncate to save tokens/cost
# [:4000] is a list/string slice — takes the first 4000 characters
# see ../python-basics/03_loops.py for slicing

print(f"HTML length: {len(table_html)} characters")
# f"..." — f-string — see ../python-basics/01_intro.py
```

**Step 2: Send to Claude and ask for structured data**

```python
import anthropic

client = anthropic.Anthropic(api_key="YOUR_KEY_HERE")

message = client.messages.create(
    model="claude-sonnet-4-20250514",
    max_tokens=1024,
    messages=[
        {
            "role": "user",
            "content": f"""Extract data from this HTML table and return ONLY a JSON array.
Each object should have: city, country, population

HTML:
{table_html}

Return ONLY valid JSON, no explanation."""
        }
    ]
)

print(message.content[0].text)
```

**Step 3: Parse and use**

```python
import json   # library for converting JSON text into Python objects — see ../python-basics/02_data_types.py

cities = json.loads(message.content[0].text)
# json.loads() converts a JSON-formatted string into a Python list of dictionaries
# the result is exactly like the dictionaries you saw in 02_data_types.py

for city in cities[:10]:   # [:10] takes only the first 10 items — slicing a list
    # see ../python-basics/03_loops.py for loops and slicing
    # city['city'], city['country'], city['population'] — dictionary key access
    # see ../python-basics/02_data_types.py
    print(f"{city['city']}, {city['country']} — Pop: {city['population']}")
```

### When This Shines — Show the Contrast

Pick a truly messy page — a local restaurant menu, a government notice board, a poorly structured blog. Show that writing BS4 selectors for it would take 30+ minutes and break if anything changes. The LLM approach takes 5 lines and handles layout changes gracefully.

**Good messy targets to bookmark:**
- Any local Pakistani restaurant website (Urdu + English mixed)
- `http://books.toscrape.com/catalogue/category/books/travel_2/index.html` (simple but show how prompt flexibility beats rigid selectors)
- A real Craigslist or OLX listing page

### Cost Awareness — Mention Briefly
- Truncate HTML before sending (remove scripts, styles, nav bars)
- Use `soup.get_text()` when structure isn't needed
- A single extraction call costs fractions of a cent

---

## BREAK (10 min)

---

## Part 4: Scrape Wars — Challenge Round (25 min)

### How It Works
- Students work solo or in pairs
- Give them 2–3 target URLs
- They pick ANY method from the session
- First to produce clean, printed output wins
- You judge on: correctness, speed, code cleanliness

### Challenge Targets

**Level 1 (Easy):**
- URL: `https://dummyjson.com/users?limit=5`
- Task: Print each user's name, email, and city
- Expected method: Direct API call with `requests`

**Level 2 (Medium):**
- URL: `https://quotes.toscrape.com/js/page/2/`
- Task: Extract all quotes, authors, and tags from page 2
- Catch: Page requires JavaScript rendering — `requests` alone won't work
- Expected method: Playwright

**Level 3 (Hard):**
- URL: `https://en.wikipedia.org/wiki/Pakistan` (or any dense Wikipedia article)
- Task: Extract the entire infobox (country details) as structured JSON
- Catch: Infobox HTML is notoriously messy
- Expected method: LLM-assisted (or creative BS4 if they're brave)
- Not sure what JSON is? See [`02_data_types.py`](../python-basics/02_data_types.py) — Dictionaries section.

### Running the Competition
- Share the URLs on screen or in a shared doc/chat
- Set a 15-minute timer visible on screen
- Walk around / monitor screens
- Have students paste their output in chat or show on screen
- Pick a winner based on who got clean data fastest

---

## Part 5: Ethics & Getting Blocked (5 min)

### Points to Cover Conversationally

**Check before you scrape:**
```python
import requests
# Always check robots.txt first
r = requests.get("https://example.com/robots.txt")
print(r.text)
```

**Be a good citizen:**
- Add delays between requests: `time.sleep(1)`
- Set a proper User-Agent header:
```python
# headers is a dictionary — Python key-value pairs — see ../python-basics/02_data_types.py
# A "User-Agent" tells the server what kind of client is making the request
headers = {"User-Agent": "atomcamp-student-project/1.0 (educational)"}
response = requests.get(url, headers=headers)
```
- Respect `robots.txt` directives
- Never scrape personal/private data
- Prefer official APIs over scraping — always

**When scraping is NOT okay:**
- Behind login walls (unauthorized access)
- Ignoring explicit Terms of Service
- Scraping and reselling data commercially
- Overloading a server with rapid requests

**When scraping IS generally okay:**
- Public data for personal/educational use
- Research purposes with proper attribution
- When no API alternative exists
- Rate-limited, respectful access

---

## Quick Reference — All Commands in One Place

> 📦 These `pip install` commands install libraries into your Python environment. Always run them inside an activated virtual environment (`venv`) so they don't affect other projects. See the [venv setup guide](../python-basics/README.md#before-you-run-anything-set-up-python-properly) if you haven't set one up yet.

```bash
# Installation
pip install requests beautifulsoup4
pip install playwright
playwright install chromium
pip install anthropic

# Playwright codegen
playwright codegen https://any-website.com

# Run a Python script
python scraper.py
```

---

## Backup Websites (if any target is down)

| Site | URL | Good For |
|---|---|---|
| HTTPBin | `https://httpbin.org/` | Testing headers, requests |
| JSONPlaceholder | `https://jsonplaceholder.typicode.com/posts` | Fake API practice |
| Scrapethissite | `https://www.scrapethissite.com/pages/` | Structured scraping practice |
| Fake Store API | `https://fakestoreapi.com/products` | E-commerce JSON |
| Hacker News API | `https://hacker-news.firebaseio.com/v0/topstories.json` | Real live data |
