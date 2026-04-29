# ============================================================
# 02_data_types.py — The Kinds of Data Python Understands
# ============================================================
#
# In the real world, data comes in different flavours:
#   - A name is text ("Alice")
#   - A price is a decimal number (9.99)
#   - A quantity is a whole number (3)
#   - A yes/no answer is a true/false value
#   - A shopping basket is a list of items
#   - A contact card is a collection of labelled facts
#
# Python has a specific "data type" for each of these.
# Understanding data types is the foundation of everything —
# especially when you're scraping websites or analysing data,
# because you constantly need to know what kind of thing you're
# working with before you can do anything useful with it.
# ============================================================


# ── 1. Strings — Text ────────────────────────────────────────
#
# A "string" is just text. Any text. Always wrapped in quotes.
# (Single quotes or double quotes — both work. Pick one and be consistent.)

product_name = "Wireless Headphones"
brand = 'SoundMax'

print("--- STRINGS ---")
print(product_name)
print(brand)

# You can join (concatenate) strings with +
full_label = brand + " — " + product_name
print(full_label)

# Useful string methods — these are built-in tools for working with text
print(product_name.upper())          # all caps: "WIRELESS HEADPHONES"
print(product_name.lower())          # all lowercase: "wireless headphones"
print(product_name.replace("Wireless", "Bluetooth"))  # swap one word for another
print(len(product_name))             # how many characters long is this string?


# ── 2. Integers — Whole Numbers ───────────────────────────────
#
# An "integer" (int) is a number with no decimal point.
# Use them for things you count: items in a basket, pages scraped, etc.

items_in_stock = 42
pages_scraped = 0
years_in_business = 5

print("\n--- INTEGERS ---")
print(items_in_stock)
print(items_in_stock + 8)           # maths works as expected
print(items_in_stock * 2)
print(type(items_in_stock))         # type() tells you what kind of data something is


# ── 3. Floats — Decimal Numbers ───────────────────────────────
#
# A "float" is a number with a decimal point.
# Named after "floating point" — the way computers store decimals.
# Use them for prices, percentages, ratings, measurements.

price = 79.99
rating = 4.5
tax_rate = 0.15

print("\n--- FLOATS ---")
print(price)
print(round(price * (1 + tax_rate), 2))    # price with 15% tax, rounded to 2 decimal places
print(type(rating))


# ── 4. Booleans — True or False ───────────────────────────────
#
# A "boolean" (bool) can only be one of two values: True or False.
# (Capital T and F — Python is picky about this.)
# Use them for yes/no flags: is the item in stock? is the user logged in?

is_in_stock = True
is_on_sale = False

print("\n--- BOOLEANS ---")
print(is_in_stock)
print(is_on_sale)

# Booleans come from comparisons — asking Python a yes/no question
print(price > 50)                   # True, because 79.99 is greater than 50
print(price == 79.99)               # True — note: == means "is equal to", = means "assign"
print(rating >= 5.0)                # False — 4.5 is not greater than or equal to 5


# ── 5. Lists — Ordered Collections ───────────────────────────
#
# A "list" holds multiple values in a specific order, inside square brackets [].
# Think of it like a numbered to-do list — item 1, item 2, item 3...
# Each position has an "index" — and in Python, counting starts at 0.
# So the first item is at index 0, the second at index 1, and so on.

categories = ["Electronics", "Sports", "Kitchen", "Office", "Home"]
prices = [79.99, 25.00, 49.99, 19.99, 129.99]

print("\n--- LISTS ---")
print(categories)                   # the whole list
print(categories[0])                # first item (index 0): "Electronics"
print(categories[2])                # third item (index 2): "Kitchen"
print(categories[-1])               # last item: "Home" — negative index counts from the end

print(f"Number of categories: {len(categories)}")   # how many items in the list

# Adding and removing items
categories.append("Clothing")       # add "Clothing" to the end
print(f"After adding: {categories}")

categories.remove("Clothing")       # remove it again
print(f"After removing: {categories}")

# Slicing — grabbing a portion of a list
print(categories[1:3])              # items at index 1 and 2 (stops BEFORE index 3): ['Sports', 'Kitchen']


# ── 6. Dictionaries — Labelled Collections ───────────────────
#
# A "dictionary" (dict) stores data as key-value pairs, inside curly braces {}.
# Think of it like a real dictionary: you look up a word (the key)
# and get back its definition (the value).
# Or think of it like a contact card: name → "Alice", phone → "0300-1234567".
#
# This is VERY important for web scraping and data analytics —
# JSON data (the format most APIs send data in) looks exactly like a Python dictionary.

product = {
    "name": "Wireless Headphones",
    "brand": "SoundMax",
    "price": 79.99,
    "rating": 4.5,
    "in_stock": True,
    "tags": ["audio", "wireless", "bluetooth"]    # a list inside a dictionary — totally fine
}

print("\n--- DICTIONARIES ---")
print(product)                          # the whole dictionary
print(product["name"])                  # look up the value for the key "name"
print(product["price"])
print(product["tags"])                  # this returns the list of tags
print(product["tags"][0])               # first tag: "audio"

# Adding a new key-value pair
product["discount"] = 0.10
print(f"Product with discount key added: {product['discount']}")

# Check if a key exists before trying to use it (avoids errors)
if "brand" in product:
    print(f"Brand is: {product['brand']}")

# Get all keys / all values / all pairs
print(list(product.keys()))
print(list(product.values()))


# ── Type conversion — switching between types ─────────────────
#
# Sometimes you get a number that's stored as text (this happens constantly
# in web scraping — everything scraped from a webpage starts as a string).
# You need to convert it to a number before you can do maths on it.

scraped_price = "49.99"              # looks like a number, but it's text
real_price = float(scraped_price)    # convert it to a float

print("\n--- TYPE CONVERSION ---")
print(type(scraped_price))           # <class 'str'>
print(type(real_price))              # <class 'float'>
print(real_price * 1.15)             # now we can do maths on it


# ============================================================
# Expected output (abbreviated):
# --- STRINGS ---
# Wireless Headphones
# SoundMax
# SoundMax — Wireless Headphones
# WIRELESS HEADPHONES
# wireless headphones
# Bluetooth Headphones
# 20
#
# --- INTEGERS ---
# 42
# 50
# 84
# <class 'int'>
# ... (and so on)
# ============================================================
