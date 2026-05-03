# 🧪 Take-Home Assignment — Web Scraping for Muggles

**Covered in session:** Hidden APIs, `requests`, Playwright basics, and scraping ethics
**Deadline:** Before the next session
**Difficulty:** Easy — if you followed along in class, you can do this

---

## Task: Build a Mini Data Collector

Pick **one** of the two options below. Both use what we covered in class — no new concepts needed.

---

### Option A: Lahore Weather Report (using `requests`)

**Target API:**
```
https://api.open-meteo.com/v1/forecast?latitude=31.55&longitude=74.35&daily=temperature_2m_max,temperature_2m_min&past_days=30&timezone=Asia/Karachi
```

Open that URL in your browser first. Look at the JSON. You'll see three lists inside `"daily"` — dates, max temperatures, and min temperatures — all lined up by position. Day 1's date matches day 1's max temp and day 1's min temp.

Write a Python script that:

1. Fetches the last 30 days of weather data for Lahore
2. Prints each day's **date**, **max temperature**, and **min temperature** in a clean format
3. At the end, prints the **hottest day** and the **coldest night** from the last 30 days

**Expected output should look something like:**
```
Lahore Weather — Last 30 Days
------------------------------
2026-04-03 | High: 35.2°C | Low: 19.8°C
2026-04-04 | High: 36.1°C | Low: 20.3°C
2026-04-05 | High: 33.7°C | Low: 18.9°C
...

🔥 Hottest day: 2026-04-15 at 42.1°C
🧊 Coldest night: 2026-04-03 at 16.5°C
```

**Starter code (fill in the blanks):**

```python
import requests

url = "https://api.open-meteo.com/v1/forecast"
params = {
    "latitude": 31.55,
    "longitude": 74.35,
    "daily": "temperature_2m_max,temperature_2m_min",
    "past_days": 30,
    "timezone": "Asia/Karachi"
}

response = requests.get(url, params=params)
data = response.json()

dates = data["daily"]["_______________"]           # the list of date strings
max_temps = data["daily"]["_______________"]       # the list of max temperatures
min_temps = data["daily"]["_______________"]       # the list of min temperatures

print("Lahore Weather — Last 30 Days")
print("-" * 30)

hottest_temp = -100       # start with an impossibly low number
hottest_date = ""
coldest_temp = 100        # start with an impossibly high number
coldest_date = ""

for i in range(len(dates)):
    date = dates[i]
    high = max_temps[i]
    low = min_temps[i]

    print(f"{date} | High: {high}°C | Low: {low}°C")

    if high > hottest_temp:
        hottest_temp = _______________    # update the record
        hottest_date = _______________    # remember which date

    if low < coldest_temp:
        coldest_temp = _______________    # update the record
        coldest_date = _______________    # remember which date

print(f"\n🔥 Hottest day: {hottest_date} at {hottest_temp}°C")
print(f"🧊 Coldest night: {coldest_date} at {coldest_temp}°C")
```

> **Hint:** The JSON keys inside `"daily"` are exactly the same words you see in the URL: `time`, `temperature_2m_max`, `temperature_2m_min`. Not sure how dictionaries work? Revisit [`../python-basics/02_data_types.py`](../python-basics/02_data_types.py).

---

### Option B: The Playwright Route

**Target:** `https://quotes.toscrape.com/js/page/1/`

This page needs JavaScript to load — plain `requests` won't work. Write a Playwright script that:

1. Opens the page (use `headless=False` so you can watch it work)
2. Extracts every **quote** and its **author**
3. Prints them numbered
4. Saves all the quotes to a `.txt` file

**Expected output should look something like:**
```
1. "The world as we have created it..." — Albert Einstein
2. "It is our choices, Harry..." — J.K. Rowling
...

Saved 10 quotes to quotes.txt
```

**Starter code (fill in the blanks):**

```python
from playwright.sync_api import sync_playwright

with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto("https://quotes.toscrape.com/js/page/1/")

    quotes = page.query_selector_all(".quote")

    all_lines = []

    for i, q in enumerate(quotes, start=1):
        text = q.query_selector("___________").inner_text()     # CSS class for the quote text
        author = q.query_selector("___________").inner_text()   # CSS class for the author name

        line = f'{i}. {text} — {author}'
        print(line)
        all_lines.append(line)

    browser.close()

# Save to file
with open("quotes.txt", "w") as f:
    for line in all_lines:
        f.write(line + "\n")

print(f"\nSaved {len(all_lines)} quotes to quotes.txt")
```

> **Hint:** Open the page in Chrome, right-click a quote → Inspect, and look for the CSS class names on the `<span>` elements. You used these exact selectors in class.

---

## Ethics Check (required — just answer in comments at the top of your script)

Add these three lines as comments at the very top of whichever script you write:

```python
# 1. Does this website have a robots.txt? (yes/no, and paste the URL you checked)
# 2. Am I scraping public data or something behind a login? (public/private)
# 3. Did I add a delay or a User-Agent header? (yes/no — and why or why not for this case)
```

---

## Submission

- Submit your `.py` file (and `quotes.txt` if you did Option B)
- Make sure it **runs without errors** before submitting
- Code should have **at least 3 comments** explaining what's happening

---

## Bonus (optional, not graded)

If both options felt too easy, try one or both of these:

- **Stretch bonus:** Add `precipitation_sum` and `windspeed_10m_max` to your API request and print a "Weather Summary" that flags any day where rain was above 5mm or wind was above 30 km/h. Check the API docs at `https://open-meteo.com/en/docs` for the exact parameter names.

- **LLM bonus — Let AI build your CSV:** Take the weather data you already fetched in Option A and use ChatGPT or Claude (the chat, not the API) to turn it into a clean CSV file. No extra libraries, no code — just copy, paste, prompt, and save.

**Here's how:**

1. Run your Option A script but add this line at the very end to print the raw JSON:
```python
print(response.text)
```

2. Copy the entire JSON output from your terminal.

3. Open ChatGPT or Claude in your browser and paste this prompt:

```
Convert this JSON into a CSV file. The CSV should have three columns:
date, max_temp, min_temp. Include a header row. Return ONLY the CSV
data, nothing else — no explanation, no code blocks, no markdown.

[paste your JSON here]
```

4. Copy the CSV output the LLM gives you, open Notepad (or any text editor), paste it in, and save it as `lahore_weather.csv`.

5. Open the `.csv` file in Excel or Google Sheets — you should see a clean table with 30 rows of weather data.

**Submit:** Your `.csv` file alongside your `.py` script.

> **Why this matters:** In real data work, you'll constantly get messy data dumps that need reshaping before anyone on your team can use them. Knowing how to use an LLM as a quick data formatting tool — not just a chatbot — is a practical skill you'll reach for again and again.

---

## 🛟 Stuck? How to Debug Using LLMs

Before you message the group chat at 2 AM, try asking an LLM first. Here's how to do it well — because "it's not working" gets you a useless answer from both humans and AI.

### The Golden Rule of Asking for Help

**Bad:** "My code doesn't work please help"

**Good:** Paste your code, paste the error, and say what you expected to happen.

### Step-by-Step: How to Ask ChatGPT or Claude to Fix Your Code

**1. Copy your FULL error message**

When Python crashes, it prints a traceback — that red wall of text. Copy ALL of it, not just the last line. It tells the LLM exactly where things broke.

```
Traceback (most recent call last):
  File "weather.py", line 12, in <module>
    dates = data["daily"]["time"]
KeyError: 'daily'
```

**2. Use this template**

Paste this into ChatGPT, Claude, or any LLM — fill in the three sections:

```
I'm a beginner learning Python. I'm trying to [what you're trying to do].

Here's my code:
[paste your full script here]

Here's the error I get when I run it:
[paste the full traceback here]

What's wrong and how do I fix it? Explain simply.
```

**3. If there's no error but the output looks wrong**

Sometimes the code runs fine but prints garbage or nothing. In that case:

```
My code runs without errors but the output is wrong.

Here's my code:
[paste code]

Here's what it prints:
[paste actual output]

Here's what I expected it to print:
[describe or paste expected output]

What's going wrong?
```

### Common Issues You'll Hit in This Assignment

| What you see | What it probably means | What to ask the LLM |
|---|---|---|
| `ModuleNotFoundError: No module named 'requests'` | You forgot to install it or your venv isn't active | "How do I install the requests library in Python?" |
| `KeyError: 'daily'` | You're accessing a dictionary key that doesn't exist — likely a typo | "What keys are in this JSON?" and paste the raw response |
| `JSONDecodeError` | The API returned an error page instead of JSON | "My API call returns this instead of JSON: [paste response]" |
| `TypeError: 'NoneType'` in Playwright | Your CSS selector didn't match anything on the page | "This Playwright selector returns None: [paste your selector]. Here's the page HTML: [paste a snippet]" |
| Code runs but prints nothing | Your loop variable or key name is wrong | Use the "no error but wrong output" template above |

### Pro Tips

- **Add `print()` statements everywhere** while debugging. Print the API response before trying to parse it. Print a dictionary's `.keys()` before accessing a key. Print inside your loop to see what each iteration looks like. Delete the extra prints when it works.
- **Ask the LLM to explain the error, not just fix it.** "What does KeyError mean in Python?" teaches you something. "Fix this" doesn't.
- **If the LLM gives you code that doesn't work either**, paste the NEW error back and say "I tried your fix and now I get this error instead." LLMs are good at iterating.
- **Don't paste your API key** into ChatGPT or any public LLM. Replace it with `"YOUR_KEY_HERE"` before pasting.
