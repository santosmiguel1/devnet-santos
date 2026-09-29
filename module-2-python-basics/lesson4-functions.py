"""
Module 2 — Lesson 4: Functions
Student: [Santos, Miguel]
Date: [9/29/26]

============================================
WHAT IS THIS TOPIC?
============================================
A function is a reusable block of code that performs
a specific task. Instead of writing the same code many
times, we can put it inside a function and call it
whenever we need it.

A function can receive information, process it, and
return a result. In Python, we create a function using
the def keyword.

============================================
KEY VOCABULARY
============================================
- function: A reusable block of code.
- def: The keyword used to define a function.
- parameter: A variable listed in a function definition.
- argument: A value passed to a function when calling it.
- return: Sends a result back from a function.
- function call: Runs a function.

============================================
MY OWN EXAMPLE(S)
============================================
"""

def calculate_total(price, quantity):
    total = price * quantity
    return total


price = 50
quantity = 3

total_price = calculate_total(price, quantity)

print("Price:", price)
print("Quantity:", quantity)
print("Total:", total_price)

"""
============================================
A MISTAKE I MADE
============================================
One mistake I want to avoid is confusing parameters
and arguments. Parameters are the variables listed
when defining a function, while arguments are the
actual values passed when calling the function.

============================================
HOW THIS CONNECTS TO SOMETHING ELSE
============================================
Functions can be used with variables, conditions,
loops, and lists. They help organize code into smaller
parts that can be reused whenever needed.
"""