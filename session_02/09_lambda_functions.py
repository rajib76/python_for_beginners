# Lambda Functions — anonymous (nameless) one-line functions
# Syntax: lambda parameters: expression
# Used when you need a small, short-lived function — especially as an argument to another function

# ---- Basic lambda ----

# Regular function
def square(x):
    return x ** 2

# Same function written as a lambda
square_lambda = lambda x: x ** 2

print(square(5))          # 25
print(square_lambda(5))   # 25 — same result

# Lambda with two parameters
add = lambda a, b: a + b
print(add(3, 4))          # 7

# Lambda with a condition (ternary style)
classify = lambda x: "even" if x % 2 == 0 else "odd"
print(classify(4))        # even
print(classify(7))        # odd

# ---- The real power: using lambda with built-in functions ----

# sorted() with a key= argument
# key= takes a function that tells sorted() WHAT to sort by

students = [("Alice", 85), ("Bob", 92), ("Charlie", 78)]

# Sort by grade (second element of each tuple)
by_grade = sorted(students, key=lambda student: student[1])
print(by_grade)
# [('Charlie', 78), ('Alice', 85), ('Bob', 92)]

# Sort in descending order
by_grade_desc = sorted(students, key=lambda student: student[1], reverse=True)
print(by_grade_desc)
# [('Bob', 92), ('Alice', 85), ('Charlie', 78)]

# Sort a list of dictionaries
products = [
    {"name": "Apple",  "price": 1.50},
    {"name": "Banana", "price": 0.50},
    {"name": "Cherry", "price": 3.00},
]

by_price = sorted(products, key=lambda p: p["price"])
for product in by_price:
    print(f"{product['name']}: ${product['price']}")

# ---- filter() ----
# Keeps only items where the function returns True

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
print(even_numbers)    # [2, 4, 6, 8, 10]

# Filter out empty strings from a list
names = ["Alice", "", "Bob", "", "Charlie"]
non_empty = list(filter(lambda name: name != "", names))
print(non_empty)       # ['Alice', 'Bob', 'Charlie']

# ---- map() ----
# Applies a function to EVERY item in a list, returns transformed values

doubled = list(map(lambda x: x * 2, numbers))
print(doubled)         # [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

# Convert a list of strings to uppercase
fruits = ["apple", "banana", "cherry"]
upper_fruits = list(map(lambda fruit: fruit.upper(), fruits))
print(upper_fruits)    # ['APPLE', 'BANANA', 'CHERRY']

# ---- When NOT to use lambda ----
# If the logic is complex or needs a name for clarity, use a regular def instead
# Lambda is for simple, one-line operations only
