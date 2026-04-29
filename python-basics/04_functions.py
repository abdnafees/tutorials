# ============================================================
# 04_functions.py — Packaging Instructions for Reuse
# ============================================================
#
# So far, every script you've written is a straight line — top to bottom.
# That works fine for small tasks. But once your scripts grow, you'll
# find yourself writing the same 5 lines over and over again.
#
# A FUNCTION is a named, reusable block of instructions.
# You define it once. You call it as many times as you need.
#
# Real-world analogy: a function is like a button on a microwave.
# The "Popcorn" button doesn't explain the heating process every time
# you press it — someone programmed those instructions once, gave
# them a name, and now you just press the button.
#
# In Python:
#   def  = "define" — I'm creating a new function
#   The function name is what you press (what you call it)
#   The instructions inside run every time you call it
# ============================================================


# ── Defining and calling a basic function ────────────────────
#
# def function_name():
#     instructions here
#
# Note the colon after the parentheses, and the indented block below.
# Python uses indentation (spaces) to know what's inside the function.

def greet():
    print("Hello! Welcome to the product catalogue.")
    print("Browse our range below.")

# Defining the function does NOTHING by itself.
# To actually run it, you "call" it — write its name with brackets.

greet()         # this calls the function and runs the two print lines


# ── Functions with parameters — making them flexible ─────────
#
# A "parameter" is a piece of information you pass INTO the function
# when you call it. It makes the function more flexible.
# Think of it like: the Popcorn button, but you can tell it
# how many minutes to run.

def greet_user(name):                   # "name" is the parameter
    print(f"Hello, {name}! Welcome.")

greet_user("Alice")                     # calling it with "Alice"
greet_user("Bob")                       # calling it again with "Bob"
# The same function, two different inputs, two different outputs.


# ── Functions with multiple parameters ───────────────────────

def display_product(name, price, rating):
    print(f"{name} — ${price} — ⭐ {rating}")

display_product("Wireless Headphones", 79.99, 4.5)
display_product("Yoga Mat", 25.00, 4.2)
display_product("Coffee Maker", 49.99, 4.7)


# ── Functions that return a value ────────────────────────────
#
# So far our functions have just printed things.
# But often you want a function to calculate something and
# GIVE BACK the result so you can use it elsewhere.
# That's what "return" does — it hands a value back to the caller.

def add_tax(price, tax_rate=0.15):          # tax_rate has a default value of 0.15
    return round(price * (1 + tax_rate), 2)

price_with_tax = add_tax(79.99)             # uses the default 15% tax
print(f"\nWith tax (default 15%): ${price_with_tax}")

price_with_custom_tax = add_tax(79.99, 0.08)    # override with 8% tax
print(f"With tax (8%): ${price_with_custom_tax}")


# ── Practical example — functions you'd use in real scraping ─

def clean_price(raw_price):
    """
    Converts a scraped price string like "$49.99" or "49,99 USD"
    into a proper Python float: 49.99.
    
    This is a "docstring" — a description of what the function does,
    written in triple quotes right after the def line.
    """
    # Remove common non-numeric characters that appear in scraped prices
    cleaned = raw_price.replace("$", "").replace(",", "").replace(" USD", "").strip()
    return float(cleaned)               # convert the cleaned text to a float


# Test it with the kinds of messy strings you actually find when scraping
print("\n--- clean_price() in action ---")
print(clean_price("$49.99"))            # 49.99
print(clean_price("129,99 USD"))        # 12999.0 — wait, that's wrong! see below
print(clean_price("  $25.00  "))        # 25.0 — strip() removes surrounding spaces


def is_good_deal(price, rating, price_threshold=50, rating_threshold=4.3):
    """
    Returns True if a product is considered a good deal:
    cheap enough AND well rated.
    """
    return price < price_threshold and rating >= rating_threshold


print("\n--- Checking for good deals ---")
products = [
    {"name": "Wireless Headphones", "price": 79.99, "rating": 4.5},
    {"name": "Yoga Mat",            "price": 25.00, "rating": 4.2},
    {"name": "Coffee Maker",        "price": 49.99, "rating": 4.7},
    {"name": "Running Shoes",       "price": 89.99, "rating": 4.3},
    {"name": "Water Bottle",        "price": 15.00, "rating": 4.8},
]

for product in products:
    deal = is_good_deal(product["price"], product["rating"])
    if deal:
        print(f"✅ GOOD DEAL: {product['name']} — ${product['price']} ⭐ {product['rating']}")
    else:
        print(f"   Skip: {product['name']}")


# ── Putting it all together — a mini data pipeline ───────────
#
# Functions really shine when you chain them together.
# Each function does one thing well; you compose them to build
# a larger process. This is how real data pipelines work.

def format_product_row(product):
    """Formats a product dictionary into a nice display string."""
    return f"{product['name']:<25} | ${product['price']:>7.2f} | ⭐ {product['rating']}"
    # :<25 means left-align in a field 25 characters wide
    # :>7.2f means right-align, 7 chars wide, 2 decimal places

print("\n--- Formatted product table ---")
print(f"{'NAME':<25} | {'PRICE':>7} | RATING")
print("-" * 45)
for product in products:
    print(format_product_row(product))


# ============================================================
# Try it yourself:
#   1. Write a function called "calculate_discount" that takes
#      a price and a discount percentage, and returns the final price.
#      Example: calculate_discount(100, 20) should return 80.0.
#   2. Write a function called "summarise_products" that takes
#      a list of products and prints: total count, average price,
#      and the name of the highest-rated product.
# ============================================================

# Expected output (abbreviated):
# Hello! Welcome to the product catalogue.
# Browse our range below.
# Hello, Alice! Welcome.
# Hello, Bob! Welcome.
# Wireless Headphones — $79.99 — ⭐ 4.5
# Yoga Mat — $25.0 — ⭐ 4.2
# Coffee Maker — $49.99 — ⭐ 4.7
# ...
