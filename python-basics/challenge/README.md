# Python Basics — Challenge

Well done for making it through the five scripts. Now it's your turn.

These challenges don't have solutions in this repo. That's on purpose. Looking things up, making mistakes, and figuring out why something broke is how you actually learn — not by following steps someone else wrote.

---

## Challenge 1 — Variables and Maths (`01_intro.py`)

You run an online shop. Write a script that:

1. Stores a product name, original price, and discount percentage as variables.
2. Calculates the discounted price and prints a sentence like:
   `"Red Shoes: was $120.00, now $96.00 (20% off)"`
3. Asks the user to enter their name and greets them with the discount offer.

**Stretch goal:** Ask the user to enter *their own* discount percentage using `input()`, then recalculate.

---

## Challenge 2 — Data Types (`02_data_types.py`)

Create a dictionary that represents a single job listing scraped from a website. It should include at least:
- job title
- company name
- location
- salary (as a number)
- remote (True or False)
- required skills (as a list)

Then:
1. Print the job title and company in the format: `"Senior Analyst at Contoso"`
2. Print whether the job is remote.
3. Print the number of required skills.
4. Add a new key `"posted_date"` with today's date as a string.

---

## Challenge 3 — Loops (`03_loops.py`)

You have a list of 10 prices scraped from a website (make them up — mix of floats, some above $50, some below):

1. Print all prices above $50.
2. Calculate and print the total and average of all prices.
3. Build a new list containing only the prices below $30, then print it.
4. Print each price with its index number, e.g. `"1. $12.99"`

**Stretch goal:** Find the highest and lowest price without using `max()` or `min()` — use a loop and an `if` statement instead.

---

## Challenge 4 — Functions (`04_functions.py`)

Write a function called `summarise_products` that:
- Takes a list of product dictionaries (each with `name`, `price`, `rating`)
- Prints the total number of products
- Prints the average price (rounded to 2 decimal places)
- Prints the name of the highest-rated product

Test it with at least 5 products.

**Stretch goal:** Add a parameter `min_rating` that makes the function only consider products above that rating. Default it to `0` so existing calls still work.

---

## Challenge 5 — Pandas (`05_pandas_first_look.py`)

Load `data/sample_products.csv` and answer these questions using pandas — no manual counting:

1. How many products are currently in stock (`in_stock == True`)?
2. What is the most expensive product in the "Electronics" category?
3. Which category has the highest average rating?
4. Create a new column `"value_score"` = `rating / price * 10` (higher is better value for money). Which product has the highest value score?
5. Save a filtered DataFrame containing only in-stock products rated above 4.2 to a new file called `data/recommended.csv`.

---

## Tips

- If something breaks, read the error message carefully — Python tells you the line number and what went wrong.
- Google is not cheating. Searching "how to sort a list in Python" is a completely normal thing professional developers do every day.
- `print()` everything. When in doubt, print the variable and see what's actually in it.
