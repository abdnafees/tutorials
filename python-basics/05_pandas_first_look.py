# pip install pandas
# ============================================================
# 05_pandas_first_look.py — Your First Real Dataset
# ============================================================
#
# Everything we've done so far — variables, loops, functions —
# has been building up to this moment.
#
# pandas is the most important library in data analytics.
# If Excel is a spreadsheet, pandas is a programmable spreadsheet.
# You load data, ask questions, filter rows, calculate totals —
# all in a few lines of Python.
#
# KEY TERM — DataFrame:
#   A DataFrame is pandas' name for a table of data.
#   Think of it exactly like an Excel sheet: rows and columns,
#   with column headers at the top. The difference is you can
#   manipulate it with code instead of clicking around.
#
# KEY TERM — EDA (Exploratory Data Analysis):
#   Before you build charts or draw conclusions, you "explore"
#   the data — how many rows? what columns? any missing values?
#   what do the numbers look like? That's EDA. This script walks
#   you through the standard EDA checklist.
#
# This script uses the file: data/sample_products.csv
# Make sure you run it from the python-basics/ folder.
# ============================================================

import pandas as pd   # "as pd" is a nickname — saves typing "pandas" every time

# ── Loading data ──────────────────────────────────────────────
#
# pd.read_csv() reads a CSV file and turns it into a DataFrame.
# CSV stands for "Comma-Separated Values" — a plain text file
# where each row is a line and columns are separated by commas.

df = pd.read_csv("data/sample_products.csv")
# "df" is the conventional short name for a DataFrame — you'll see
# it everywhere in data analytics code.


# ── Step 1: Get the lay of the land ──────────────────────────
#
# First thing after loading any new dataset: look at it.

print("=== FIRST 5 ROWS ===")
print(df.head())                # .head() shows the first 5 rows — like peeking inside the file
print()

print("=== SHAPE (rows, columns) ===")
print(df.shape)                 # returns (number_of_rows, number_of_columns)
print(f"This dataset has {df.shape[0]} products and {df.shape[1]} columns.")
print()

print("=== COLUMN NAMES ===")
print(df.columns.tolist())      # all column headers as a list
print()


# ── Step 2: Understand what's in each column ─────────────────
#
# .info() is the single most useful EDA command — it shows:
#   - column names
#   - how many non-null (non-empty) values each column has
#   - the data type of each column (int, float, object = text, bool)

print("=== DATA TYPES AND NULL COUNTS ===")
df.info()
print()


# ── Step 3: Summary statistics ───────────────────────────────
#
# .describe() calculates count, mean, min, max, and percentiles
# for every numeric column automatically.
# This is how you get a "feel" for a dataset in 10 seconds.

print("=== SUMMARY STATISTICS ===")
print(df.describe().round(2))   # .round(2) keeps it clean — 2 decimal places
print()


# ── Step 4: Accessing columns ────────────────────────────────
#
# You access a single column using square brackets, just like a dictionary.
# The result is a "Series" — pandas' name for a single column of data.

print("=== PRODUCT NAMES ===")
print(df["name"])               # prints the entire "name" column
print()

# Calculating with a column
average_price = df["price"].mean()
highest_price = df["price"].max()
lowest_price  = df["price"].min()

print("=== PRICE STATS ===")
print(f"Average price: ${average_price:.2f}")    # :.2f means format to 2 decimal places
print(f"Most expensive: ${highest_price}")
print(f"Least expensive: ${lowest_price}")
print()


# ── Step 5: Filtering rows ────────────────────────────────────
#
# Filtering in pandas works like this:
#   df[condition]
# The condition is a True/False test on a column.
# Only rows where the condition is True are returned.

print("=== PRODUCTS PRICED UNDER $30 ===")
cheap_products = df[df["price"] < 30]           # keep only rows where price < 30
print(cheap_products[["name", "price", "rating"]])   # show only these 3 columns
print()

print("=== HIGHLY RATED PRODUCTS (4.5 or above) ===")
top_rated = df[df["rating"] >= 4.5]
print(top_rated[["name", "rating", "category"]])
print()

# You can combine conditions with & (and) and | (or)
# Note: each condition must be wrapped in its own parentheses
print("=== AFFORDABLE AND HIGHLY RATED (under $30 AND rated 4.2+) ===")
good_deals = df[(df["price"] < 30) & (df["rating"] >= 4.2)]
print(good_deals[["name", "price", "rating"]])
print()


# ── Step 6: Grouping and aggregating ─────────────────────────
#
# "Grouping" means: split the data by a category, then
# calculate a summary for each group.
# It's the pandas equivalent of Excel's SUMIF or a pivot table.

print("=== AVERAGE PRICE BY CATEGORY ===")
avg_by_category = df.groupby("category")["price"].mean().round(2)
# groupby("category") — split rows into groups by the "category" column
# ["price"]           — work with the price column within each group
# .mean()             — calculate the average for each group
print(avg_by_category)
print()

print("=== NUMBER OF PRODUCTS PER CATEGORY ===")
count_by_category = df.groupby("category")["name"].count()
print(count_by_category)
print()


# ── Step 7: Sorting ───────────────────────────────────────────

print("=== TOP 5 PRODUCTS BY RATING ===")
top5 = df.sort_values("rating", ascending=False).head(5)
# sort_values() sorts the rows by a column
# ascending=False means highest first (descending order)
print(top5[["name", "rating", "price"]])
print()


# ── Step 8: Adding a new column ───────────────────────────────
#
# You can create a new column by assigning a calculation to it.
# Here we add a "price_with_tax" column — 15% added to every price.

df["price_with_tax"] = (df["price"] * 1.15).round(2)

print("=== PRICES WITH 15% TAX ADDED ===")
print(df[["name", "price", "price_with_tax"]].head(5))
print()


# ── Step 9: Checking for missing data ────────────────────────
#
# Real-world datasets almost always have missing values.
# .isnull().sum() counts how many empty cells exist per column.

print("=== MISSING VALUES PER COLUMN ===")
print(df.isnull().sum())
print("(0 means no missing values in that column — our sample data is clean!)")
print()


# ── Step 10: Saving results ───────────────────────────────────
#
# Once you've cleaned or filtered data, you can save it back to CSV.

good_deals.to_csv("data/good_deals.csv", index=False)
# index=False stops pandas from writing the row numbers as a column
print("Saved 'good_deals.csv' to the data/ folder.")


# ============================================================
# Try it yourself:
#   1. Find all products in the "Electronics" category.
#      Hint: df[df["category"] == "Electronics"]
#   2. What is the average rating across all products?
#   3. Sort products by price (cheapest first) and print the result.
#   4. Add a column called "is_budget" that is True when price < 25.
#      Hint: df["is_budget"] = df["price"] < 25
# ============================================================

# Expected output (abbreviated):
# === FIRST 5 ROWS ===
#    id                  name      category  price  rating  in_stock
# 0   1  Wireless Headphones  Electronics  79.99     4.5      True
# ...
#
# === SHAPE (rows, columns) ===
# (15, 6)
# This dataset has 15 products and 6 columns.
