# ============================================================
# 03_loops.py — Doing the Same Thing Many Times, Automatically
# ============================================================
#
# Imagine you have a spreadsheet with 500 product rows and you need
# to add tax to every price. You wouldn't do it by hand. You'd
# write a formula and copy it down.
#
# In Python, that's what a LOOP does. You tell Python:
#   "For every item in this collection, do this thing."
#
# This is one of the most powerful ideas in programming — and it's
# the reason web scraping and data processing are so useful.
# Instead of copy-pasting 500 rows, you write 5 lines of code.
# ============================================================


# ── The "for" loop — the workhorse ───────────────────────────
#
# Syntax:
#   for item in collection:
#       do something with item
#
# Python reads this as: "For each item in the collection, run the
# indented block of code below, using that item."
#
# The word "item" is just a name you make up — you can call it anything.
# "product", "row", "x", "p" — whatever makes your code readable.

categories = ["Electronics", "Sports", "Kitchen", "Office", "Home"]

print("--- Looping through a list ---")
for category in categories:
    print(category)                 # prints each category on its own line


# ── Doing something useful inside the loop ───────────────────

prices = [79.99, 25.00, 49.99, 19.99, 129.99]
tax_rate = 0.15                    # 15% tax

print("\n--- Adding tax to every price ---")
for price in prices:
    price_with_tax = round(price * (1 + tax_rate), 2)   # calculate taxed price
    print(f"Original: ${price}  →  With tax: ${price_with_tax}")


# ── Looping through a list of dictionaries ───────────────────
#
# This is the pattern you'll use constantly in web scraping and
# data analytics. An API response, for example, is almost always
# a list of dictionaries — one dictionary per product/user/post/etc.

products = [
    {"name": "Wireless Headphones", "price": 79.99, "rating": 4.5},
    {"name": "Yoga Mat",            "price": 25.00, "rating": 4.2},
    {"name": "Coffee Maker",        "price": 49.99, "rating": 4.7},
    {"name": "Running Shoes",       "price": 89.99, "rating": 4.3},
    {"name": "Desk Lamp",           "price": 19.99, "rating": 4.0},
]

print("\n--- Looping through a list of products ---")
for product in products:
    # product is a dictionary — use square brackets to get a value by key
    print(f"{product['name']} — ${product['price']} — Rating: {product['rating']}")


# ── Filtering inside a loop ───────────────────────────────────
#
# You can use an "if" statement inside a loop to only act on
# items that meet a condition. This is how you filter data.

print("\n--- Only products rated above 4.3 ---")
for product in products:
    if product["rating"] > 4.3:                 # condition: is rating greater than 4.3?
        print(f"⭐ {product['name']} — {product['rating']}")


# ── Building a new list from a loop ──────────────────────────
#
# A very common pattern: start with an empty list, then add to it
# inside the loop. This is how you "collect" results.

expensive_products = []             # start with an empty list

for product in products:
    if product["price"] > 50:       # if price is over $50...
        expensive_products.append(product["name"])   # ...add the name to our list

print(f"\nProducts over $50: {expensive_products}")


# ── The range() function — looping a set number of times ─────
#
# Sometimes you don't have a list to loop through — you just want
# to repeat something N times. range() gives you a sequence of numbers.

print("\n--- Counting to 5 with range() ---")
for number in range(1, 6):         # range(1, 6) produces 1, 2, 3, 4, 5  (stops BEFORE 6)
    print(number)


# ── enumerate() — when you need the position AND the value ───
#
# Sometimes you want to know both the index (position number)
# and the value at that position. enumerate() gives you both.

print("\n--- Products with their position numbers ---")
for index, product in enumerate(products, start=1):    # start=1 so we count from 1, not 0
    print(f"{index}. {product['name']}")


# ── Scraping simulation — how loops power web scrapers ───────
#
# When you scrape multiple pages of a website, you loop through
# page numbers. Here's a simplified version of what that looks like:

base_url = "https://example.com/products?page="

print("\n--- URLs that a scraper would visit ---")
for page_number in range(1, 6):                         # pages 1 through 5
    url = base_url + str(page_number)                   # build the URL for each page
    print(f"Fetching: {url}")
    # In a real scraper, you'd call requests.get(url) here


# ── while loops — keep going until a condition changes ───────
#
# A "while" loop keeps running as long as a condition is True.
# Think of it like: "While the kettle hasn't boiled, wait."
# Use carefully — if the condition never becomes False, it runs forever.

print("\n--- while loop example ---")
attempts = 0
max_attempts = 3

while attempts < max_attempts:
    attempts = attempts + 1         # increase the counter (don't forget this — or it loops forever!)
    print(f"Attempt {attempts} of {max_attempts}")

print("Done.")


# ============================================================
# Try it yourself:
#   1. Loop through the products list and print only the ones
#      with a price BELOW $30.
#   2. Use a loop to calculate the AVERAGE rating across all products.
#      Hint: add all ratings up in a loop, then divide by the count.
#   3. Build a list of all product names in UPPERCASE using a loop.
# ============================================================

# Expected output (abbreviated):
# --- Looping through a list ---
# Electronics
# Sports
# Kitchen
# Office
# Home
#
# --- Adding tax to every price ---
# Original: $79.99  →  With tax: $91.99
# ... (and so on)
