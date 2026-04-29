# ============================================================
# 01_intro.py — What Is Python, and How Do I Talk to It?
# ============================================================
#
# Before we write code, let's understand what we're actually doing.
#
# Python is a programming language — a way of giving instructions
# to a computer. Think of it like a recipe. You write the steps,
# the computer follows them exactly, top to bottom, in order.
#
# This file is a "script" — a plain text file full of Python
# instructions. When you run it, Python reads line by line and
# does what you asked.
#
# HOW TO RUN THIS FILE:
#   1. Open your terminal (Mac: Cmd+Space → "Terminal"  |  Windows: Win+R → "cmd")
#   2. Navigate to this folder:  cd path/to/python-basics
#   3. Make sure your venv is active (see README.md for setup)
#   4. Type:  python 01_intro.py
#   5. Press Enter and watch the magic happen
# ============================================================


# ── The print() function ──────────────────────────────────────
#
# print() is how Python shows you text on the screen.
# Think of it as Python "speaking" to you.
# Anything inside the brackets and quotes gets displayed.

print("Hello! Welcome to Python.")
print("This is your first script.")


# ── Variables ─────────────────────────────────────────────────
#
# A variable is like a labelled box. You put something in the box,
# give it a name, and later you can refer to it by that name.
#
# Syntax:  box_name = value
#
# The = sign doesn't mean "equals" the way it does in maths.
# It means "store this value in this box."

your_name = "Alex"              # a box labelled "your_name" holding the text "Alex"
your_age = 28                   # a box labelled "your_age" holding the number 28
city = "Karachi"                # a box labelled "city" holding the text "Karachi"

# Now let's use those boxes in a print statement.
# The f"..." syntax is called an "f-string" — it lets you drop
# variable values directly into text using curly braces { }.

print(f"Hi, my name is {your_name}.")
print(f"I am {your_age} years old and I live in {city}.")


# ── You can change a variable's value ─────────────────────────
#
# Variables can be overwritten. The box gets a new value.

your_age = 29           # birthday! the box now holds 29 instead of 28

print(f"One year later, I am now {your_age}.")


# ── A quick note about comments ───────────────────────────────
#
# Any line that starts with # is a "comment" — Python ignores it.
# Comments are notes for humans (you, future you, teammates).
# They don't do anything — they explain what and WHY.
# You'll see lots of them in these tutorials. That's on purpose.


# ── Running calculations ──────────────────────────────────────
#
# Python can do maths. Use it like a calculator.

price = 49.99           # price of a product
discount = 0.10         # 10% discount (written as a decimal)

discounted_price = price - (price * discount)

print(f"Original price: ${price}")
print(f"After 10% discount: ${discounted_price}")


# ── Asking the user for input ─────────────────────────────────
#
# input() pauses the script and waits for the user to type something.
# Whatever they type gets stored as text (a "string").

user_name = input("What's your name? ")    # waits for you to type and press Enter
print(f"Nice to meet you, {user_name}!")


# ============================================================
# Try it yourself:
#   1. Change the value of "city" to your actual city.
#   2. Add a new variable called "job" and print a sentence using it.
#   3. Add a second discount calculation — what if the discount was 25%?
# ============================================================

# Expected output (will vary based on what you type at the input prompt):
# Hello! Welcome to Python.
# This is your first script.
# Hi, my name is Alex.
# I am 28 years old and I live in Karachi.
# One year later, I am now 29.
# Original price: $49.99
# After 10% discount: $44.991
# What's your name? [you type here]
# Nice to meet you, [your name]!
