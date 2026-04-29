# Web Scraping Session — Trainer Content Guide

**Session:** Friday, 7:00–9:00 PM
**Audience:** Data Analytics Bootcamp students (Python basics covered)

---

## Part 1: The Hidden API Hunt (30 min)

### Key Concept
Most modern websites don't render data from HTML — they fetch it from internal APIs as JSON. You can intercept these requests and skip HTML parsing entirely.

### Setup
Students need:
- Chrome or Edge browser
- Python with `requests` and `json` (both pre-installed)

### Live Demo — Target Websites

**Website 1: Books to Scrape (Warm-up)**
- URL: `https://books.toscrape.com/`
- This is a classic training site — show the BS4 way first (5 min), then say "now forget all of that."

**Website 2: GitHub Jobs / Repositories API**
- URL: `https://api.github.com/search/repositories?q=python&sort=stars`
- Open the URL directly in the browser — clean JSON, no scraping needed.
- Key point: many sites have public APIs you can just *ask* nicely.

```python
import requests
import json

response = requests.get(
    "https://api.github.com/search/repositories",
    params={"q": "data analytics", "sort": "stars", "per_page": 10}
)

data = response.json()

for repo in data["items"]:
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

```python
# Once you find the hidden endpoint
response = requests.get("https://dummyjson.com/products?limit=10")
products = response.json()["products"]

for p in products:
    print(f"{p['title']} | ${p['price']} | Rating: {p['rating']}")
```

**Website 4: Real-World Practice — Quotable API**
- URL: `https://api.quotable.io/quotes?page=1`
- Students fetch quotes, authors, and tags — easy to loop through pages.

```python
response = requests.get("https://api.quotable.io/quotes", params={"page": 1, "limit": 5})
data = response.json()

for quote in data["results"]:
    print(f'"{quote["content"]}" — {quote["author"]}')
```

### Key Takeaway to Emphasize
> "Before you write a single line of scraping code, check the Network tab. 8 out of 10 times, the data is already sitting there in JSON."

---

## Part 2: Playwright — The Selenium Killer (25 min)

### Key Concept
Playwright is faster, more reliable, auto-waits for elements (no `time.sleep`), and has a codegen tool that writes code by recording your clicks.

### Installation (have students run this at the start of session or during break)
```bash
pip install playwright
playwright install chromium
```

### Demo 1: Basic Scraping with Playwright

Target: `https://quotes.toscrape.com/js/` (this site requires JavaScript — BS4 can't handle it, Selenium can but painfully)

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)  # headless=False so students can watch
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/")

    # Auto-waits for elements — no sleep needed
    quotes = page.query_selector_all(".quote")

    for q in quotes:
        text = q.query_selector(".text").inner_text()
        author = q.query_selector(".author").inner_text()
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
import requests
from bs4 import BeautifulSoup

response = requests.get("https://en.wikipedia.org/wiki/List_of_largest_cities")
soup = BeautifulSoup(response.text, "html.parser")

# Grab just the first big table to keep tokens manageable
table = soup.find("table", {"class": "wikitable"})
table_html = str(table)[:4000]  # Truncate to save tokens/cost

print(f"HTML length: {len(table_html)} characters")
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
import json

cities = json.loads(message.content[0].text)

for city in cities[:10]:
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
