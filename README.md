# Python for Beginners 

### We may not write code in future, but we may still need to understand what AI writes

---

## Welcome — Before We Write a Single Line of Code

### The Story of How We Got Here

Programming did not start with Python. It started with machines that could barely do anything without someone speaking their language — and their language was brutal.

**The 1940s–50s: Talking Directly to the Hardware**

The first computers were programmed with raw binary — sequences of `0`s and `1`s that mapped directly to electrical signals inside the processor. Every instruction meant something like: *"move this voltage to this register, flip this bit, jump to this memory address."* Programmers had to think like the machine, not like a human.

Then came **Assembly language** — a tiny step up. Instead of `10110000 01100001`, you could write `MOV AL, 61h`. Still one instruction per processor operation. Still tied completely to the specific chip you were programming. Write code for one processor, throw it away for another.

**The 1950s–70s: High-Level Languages — Humans Take Over**

The breakthrough was the **compiler** — a program that could translate human-readable instructions into machine code automatically. Suddenly you could write:

```
total = price * quantity
```

...and the compiler would figure out which processor instructions to generate. The programmer was freed from thinking about registers and memory addresses. They could think about the **problem** instead of the machine.

FORTRAN (1957) was first — built for scientific calculations. COBOL followed for business. Then C, which gave us operating systems. Then came the explosion: Java, C++, JavaScript, Ruby, and eventually **Python** in 1991.

Each generation of language moved further from the machine and closer to human thinking. The code got shorter. More readable. More powerful per line written.

**The 2000s–2010s: Frameworks & Abstraction Layers**

Developers stopped writing everything from scratch. Need a web server? Import Flask. Need to analyse a million rows of data? Import Pandas. Need machine learning? Import TensorFlow. The skill shifted from *"how do I make the computer do X"* to *"which tool do I pick, and how do I connect the pieces."*

A single developer with the right libraries could build in a week what would have taken a team a year in the 1980s.

**The 2020s: The Shift We Are Living Through Right Now**

Something fundamental is changing again — and you are here at exactly the right moment to understand it.

AI coding assistants (GitHub Copilot, Claude, ChatGPT) can now write large amounts of working code from a plain English description. You describe *what* you want, and the AI produces the *how*.

This means two things:

1. **The barrier to entry is lower than ever.** Someone who understands concepts but hasn't memorised every syntax detail can still build real software by working with AI effectively.

2. **Understanding still matters more than ever — not less.** AI writes code you have to read, debug, modify, and take responsibility for. If you don't understand what the code is doing, you can't tell when it is wrong. And it will be wrong sometimes.

> The programmer who thrives in this era is not the one who memorises syntax.
> It is the one who understands *why* code is structured the way it is —
> and can direct AI to build the right thing, then verify that it did.

**Where Python fits in this story**

Python sits at a sweet spot. It is close enough to plain English that beginners grasp it quickly. It is powerful enough that professionals use it for everything from scripts to machine learning systems at scale. And it is the language most AI tools are currently built with. This is also one of the languages AI understands better.

Learning Python today means you are learning:
- The concepts that underlie almost every programming language
- The language the world's AI tools speak most fluently
- The foundation you need to actually understand and direct what AI builds for you

---

## What You Will Learn  — Course Overview

This is a **hands-on, project-based session**. You will not just read about Python — you will build a real, working application from scratch, adding capability to it in every session.

### The Application: ChocoPOS

You are building the point-of-sale system for **Chocolate Fantasy**, a chocolate shop. By the end of 4 hours it will:

- Display a product catalog
- Take customer orders
- Apply discounts
- Track stock levels
- Save orders to disk
- Load data from JSON files
- Be built from a clean, professional class hierarchy

Every concept taught today lands directly in this application. You will always see *why* the concept matters, not just *what* it is.

### Session Breakdown

| Session | Time | What you build | Key concepts |
|---|---|---|---|
| **Session 1** | Hour 1 | Receipt printer — show a menu, take an order, print a receipt | Variables, data types, f-strings, input(), if/elif/else, for/while loops, list comprehension, string slicing |
| **Session 2** | Hour 2 | Smart menu — functions, daily special, sort by price, filter by budget | Functions, *args/**kwargs, lambda, map/filter/sorted, random, datetime, math, custom modules |
| **Session 3** | Hour 3 | Persistent inventory — stock survives restarts, orders saved to disk | Data structures, file I/O, JSON, exception handling, dict methods, enumerate/zip |
| **Session 4** | Hour 4 | Full OOP engine — everything is a class, clean hierarchy | Classes, inheritance, ABC, polymorphism, dunder methods, @property, @classmethod, @staticmethod |

### The Progression Story

Each session solves a real problem the previous version had:

- **After Session 1:** *"The menu is hardcoded and nothing is remembered between runs"*
- **After Session 2:** *"Every behaviour is a function now, but the code is still one big flat script"*
- **After Session 3:** *"The shop remembers everything — but data and functions are still separate"*
- **After Session 4:** *"Data and behaviour live together as objects — this is how professional software is structured"*

### What This Course Is Not

This is not a comprehensive Python reference. It does not cover every feature of the language. What it does is give you a solid mental model of the core concepts — the ones you will use constantly 


---

## The Project Goal

As part of this course, every student builds **ChocoPOS** — a chocolate shop point-of-sale terminal for *Chocolate Fantasy*.

Each session produces a fully runnable version of the app. Every concept is taught with a focused example file, then immediately applied in ChocoPOS so students see exactly why it matters.

```
Session 1  →  session1_receipt.py     — Receipt printer (vars, loops, if/else)
Session 2  →  session2_menu.py        — Smart menu    (functions, stdlib, lambda)
Session 3  →  session3_tracker.py     — Inventory hub (JSON, files, exceptions)
Session 4  →  session4_shop_engine.py — OOP engine    (classes, inheritance, decorators)
```

**By the end:** students run `python3 choco_pos/session4_shop_engine.py` and the shop loads from a JSON catalog, tracks stock, saves orders, and is built from a clean class hierarchy.

---

## Course Structure at a Glance

| Session | Hour | What gets built | Core concepts |
|---|---|---|---|
| 1 | 0–60 min | Receipt printer | Variables, types, loops, if/else, list comprehension, string slicing |
| 2 | 61–120 min | Smart menu system | Functions, *args/**kwargs, lambda, map/filter, random, datetime, math |
| 3 | 121–180 min | Persistent inventory tracker | Data structures, file I/O, JSON, exception handling |
| 4 | 181–240 min | Full OOP shop engine | Classes, inheritance, ABC, polymorphism, dunder methods, decorators |

---

---

# SESSION 1 (Hour 1) — Python Basics

## What You Will Build Today

`choco_pos/session1_receipt.py` — A menu-driven terminal that:
- Shows 5 chocolates with prices
- Lets a customer add items by number
- Warns about dark chocolate (logical operators)
- Applies a tiered discount (15% for 5+ items, 10% for 3+)
- Prints a formatted receipt with string slicing and f-strings

**Run at the end:**
```bash
python3 choco_pos/session1_receipt.py
```

---

## [0:00–0:05] Setting the Stage (5 min)

**Concept: What is Python and how does it run?**
- Python is an **interpreted** language — the interpreter reads your `.py` file line by line, top to bottom
- Show `session_01/hello_world.py` — the simplest possible program

### Deep Dive: `print()` — The Most Fundamental Built-in

`print()` is built-in — Python provides it automatically, no import needed.

```python
print("Hello World")     # prints a string
print(42)                # prints a number
print(True)              # prints a boolean
print()                  # prints a blank line
```

**Printing multiple values:**
```python
name = "Rajib"
print("Name:", name, "Age:", 30)
# Output: Name: Rajib Age: 30
```
Python puts a **space** between each value by default.

**`sep` — controlling the separator:**
```python
print("2024", "03", "08", sep="-")   # Output: 2024-03-08
```

**`end` — controlling the line ending:**
```python
print("Hello", end=" ")
print("World")            # Output: Hello World  (same line)
```
By default `print()` adds `\n` (newline) at the end. Change it with `end=""`.

**Key lesson:** `print()` does **not** return a value — it only displays. Its return value is `None`.
```python
result = print("Hello")   # prints "Hello"
print(result)             # prints None
```

### Deep Dive: `__name__` and `if __name__ == "__main__":`

`__name__` is a special variable Python sets automatically for every `.py` file.

| Situation | Value of `__name__` |
|---|---|
| File is run directly (`python hello_world.py`) | `"__main__"` |
| File is imported by another file | The file's own name (e.g. `"hello_world"`) |

**Why it matters — the problem:**
```python
# calculator.py
def add(a, b): return a + b

print("Testing:", add(3, 5))   # runs when imported too — unwanted!
```

**The fix:**
```python
def add(a, b): return a + b

if __name__ == "__main__":
    print("Testing:", add(3, 5))   # ONLY runs when you execute this file directly
```

> Think of it as: *"Run this block only if I am the one in charge."*

**Three things to remember:**
1. `__name__` is set by Python — you never assign it
2. It equals `"__main__"` only at the entry point of execution
3. Use it to separate reusable functions from demo/test code

**Other approaches — quick overview:**

| Approach | Best For |
|---|---|
| `if __name__ == "__main__":` | Single files, scripts, learning |
| `def main()` + `if __name__` | Professional code — all examples in this course use this |
| Separate files (module + script) | Large projects with clear separation |
| `__main__.py` in a package | Runnable packages (`python -m my_package`) |
| `python -m module` flag | Running modules that need path resolution |

**For this course:** use `if __name__ == "__main__": main()` throughout.

---

## [0:05–0:35] Variables & Data Types (30 min)

**File:** `session_01/01_variables_and_datatypes.py`

**Concept: Variables — Named containers for data**
- A variable is a label that points to a value in memory
- Python is **dynamically typed** — you don't declare types, Python infers them
- Naming rules: no spaces, no special characters (except `_`), cannot start with a digit

**The 4 core types — Chocolate Shop style:**

| Variable | Value | Type | Why |
|---|---|---|---|
| `name` | `"Chocolate Fantasy"` | `str` | text |
| `number_of_chocolates_in_stock` | `10` | `int` | whole number |
| `unit_price` | `4.978656` | `float` | decimal |
| `dark_chocolate` | `True` | `bool` | yes/no |

**f-strings (formatted string literals):**
```python
name = "Chocolate Fantasy"
unit_price = 4.978656
print(f"Shop: {name}")
print(f"Price: {unit_price:.2f}")   # .2f = 2 decimal places
```
- Prefix with `f`, embed variables inside `{}`
- Format specifiers: `:.2f` → float with 2 decimals, `:<18` → left-align in 18 chars

**Arithmetic operators:**
- `*` multiply, `/` true division (returns float), `//` floor division (returns int), `**` power
- `11 // 3` → `3` (floor division: useful when you can't buy half a chocolate)

**Type conversion:**
- **Implicit:** Python auto-promotes `5 + 2.5` → `7.5` (int promoted to float)
- **Explicit:** `int(3.75)` → `3` (truncates, does NOT round), `float("4.99")` → `4.99`
- **Why this matters:** `input()` always returns a `str` — you must convert to do math

**`input()` — Getting data from the user:**
```python
user_input = input("Enter your name: ")   # always returns str
number = int(input("Enter a number: "))   # convert immediately
```

### → In Your ChocoPOS Today

Open `choco_pos/session1_receipt.py` — find these concepts:

```python
SHOP_NAME  = "Chocolate Fantasy"     # str constant
OWNER      = "Rajib"                 # str constant
BORDER     = "=" * 42                # str * int repetition

MENU = [
    ("Dark Delight",  4.99, True),   # tuple: (str, float, bool)
    ("Milk Marvel",   3.49, False),
    ...
]
```
- `SHOP_NAME` is a `str`, `4.99` is a `float`, `True` is a `bool`
- `"=" * 42` — string repetition operator, not multiplication

```python
print(f"  {name:<22}  ${price:.2f}")   # f-string with format specifiers
```
- `{name:<22}` — left-align in 22 chars, `{price:.2f}` — float with 2 decimals

---

## [0:35–1:00] Control Structures (25 min)

**Files:** `session_01/02_control_structures.py`, `session_01/03_logical_operators.py`, `session_01/04_string_slicing.py`

**Concept: `if / elif / else` — Making decisions**
- Python uses **indentation** (4 spaces) to define code blocks — no curly braces
- Comparison operators: `>`, `<`, `>=`, `<=`, `==`, `!=`

```python
def determine_student_grade(marks):
    if marks <= 70:
        grade = "C"
    elif 70 < marks <= 80:   # Python's chained comparison — reads like math
        grade = "B"
    else:
        grade = "A"
```

**Concept: `for` loop — Iterating over a sequence**
```python
for i, (name, price, is_dark) in enumerate(MENU, start=1):
    tag = "[DARK]" if is_dark else ""
    print(f"  {i}. {name:<16} ${price:.2f}  {tag}")
```
- `enumerate()` gives both the index and the value — avoids manual counter variables
- `range(start, stop, step)` — stop is **exclusive**

**Concept: `while` loop — Repeat until condition is false**
```python
while True:           # infinite loop
    choice = input("Item number (or 'done'): ").strip()
    if choice.lower() == "done":
        break         # exit immediately
    if not choice.isdigit():
        continue      # skip the rest, go back to top of loop
```
- `break` — exits the loop immediately
- `continue` — skips the rest of the current iteration, restarts the loop
- `.strip()` — removes leading/trailing whitespace from user input

**Concept: Logical operators**
```python
if is_dark and display_name not in ["", " "]:
    print(f"  {name} is a rich dark chocolate — bold choice!")

if confirm not in ["yes", "y"]:
    continue
```
- `and` — both must be True
- `or` — at least one must be True
- `not` — inverts the boolean
- `in` / `not in` — membership test in a list or string

**Concept: List Comprehension — Compact loops**
```python
bulk_prices = [f"${p * 0.9:.2f}" for _, p, _ in MENU]
# Result: ["$4.49", "$3.14", "$3.59", "$4.59", "$4.04"]
```
Structure: `[expression for variable in iterable]`

**Concept: String Slicing**
```python
text = "Chocolate Fantasy"
text[0]       # "C"       — index 0 (first character)
text[-1]      # "y"       — index -1 (last character)
text[0:9]     # "Chocolat" — slice from 0 up to (not including) 9
text[:9]      # "Chocolat" — same, start defaults to 0
text[10:]     # "Fantasy"  — from index 10 to end
text[::2]     # every second character
```

### → In Your ChocoPOS Today

```python
# String slicing — cap display name to 15 chars
display_name = customer_name[:15]

# List comprehension — preview bulk prices
bulk_prices = [f"${p * 0.9:.2f}" for _, p, _ in MENU]

# if/elif/else — tiered discount
if len(cart) >= 5:
    discount_pct = 0.15
    tier_label   = "Gold (15%)"
elif len(cart) >= 3:
    discount_pct = 0.10
    tier_label   = "Loyalty (10%)"
else:
    discount_pct = 0.0
    tier_label   = None

# Logical operator — dark chocolate warning
if is_dark and display_name not in ["", " "]:
    print(f"  {name} is a rich dark chocolate — bold choice!")

# not in — confirm before adding more than 3 of same item
if confirm not in ["yes", "y"]:
    continue
```

---

## [0:55–1:00] Session 1 Checkpoint — Run Your Shop

```bash
python3 choco_pos/session1_receipt.py
```

**Your shop can now:**
- Show a formatted menu with prices
- Take items from a customer
- Apply a tiered discount
- Print a receipt to the terminal

**What it still can't do:** Remember anything between runs. The menu is hardcoded. No file, no persistence. That's Session 3's problem to solve.

---

---

# SESSION 2 (Hour 2) — Functions, Modules & the Standard Library

## What You Will Build Today

`choco_pos/session2_menu.py` + `choco_pos/session2_utils.py` — The same shop, but:
- Every behaviour is now wrapped in a named function
- A daily special is picked randomly each time the shop opens
- The menu sorts by price and can be filtered by customer budget
- Receipts carry a timestamp
- A loyalty tier is calculated with math
- A custom utility module (`session2_utils.py`) is imported for formatting

**Run at the end:**
```bash
python3 choco_pos/session2_menu.py
```

---

## [1:00–1:25] Functions (25 min)

**Files:** `session_02/03_python_functions_and_modules.py`, `session_02/my_modules/my_math_module.py`

**Concept: What is a function?**
- A reusable block of code with a name
- Defined once, called many times — DRY (Don't Repeat Yourself)

**Defining and calling:**
```python
def upper_to_lower_case(input_str: str) -> str:
    return input_str.lower()

result = upper_to_lower_case("HELLO")   # result = "hello"
```
- `def` keyword starts the definition
- `input_str: str` — **type hint** (not enforced, but documents intent)
- `-> str` — return type hint
- `return` sends a value back. Without `return`, the function returns `None`

**Parameters vs Arguments:**
- **Parameter** — variable name in the definition (`input_str`)
- **Argument** — actual value passed when calling (`"HELLO"`)

**Default parameters:**
```python
def display_menu(menu: list, sort_by: str = "name", budget: float = None):
```
- If `sort_by` is not provided, it defaults to `"name"`
- Optional parameters must come after required ones

**Global vs Local scope:**
```python
my_variable = "global"

def show_local():
    my_variable = "local"   # creates a LOCAL variable — does NOT change the global
    print(my_variable)      # prints "local"

show_local()
print(my_variable)          # prints "global" — unchanged
```
- Variables inside a function are **local** — they die when the function returns
- Use `global` keyword inside a function only when you truly need to modify a global (rare)

**`*args` — Accept any number of positional arguments:**
```python
def calculate_total(*items, discount_rate: float = 0.0):
    subtotal = sum(price for _, price in items)
    return subtotal * (1 - discount_rate)

calculate_total(("Milk Marvel", 3.49), ("Berry Bliss", 4.49))
```
- `*items` collects all positional arguments into a tuple
- Parameters after `*args` must be passed as keyword arguments

**`**kwargs` — Accept any number of keyword arguments:**
```python
def build_receipt(customer: str, **line_items):
    for label, value in line_items.items():
        print(f"  {label}: {value}")

build_receipt("Rajib", subtotal="$7.98", tax="$0.64", total="$8.62")
```
- `**line_items` collects all keyword arguments into a dict
- Perfect when you don't know in advance what keys will be passed

**Custom modules:**
- `session_02/my_modules/my_math_module.py` — contains `add()`
- `session_02/my_modules/__init__.py` — makes the folder a **package**
- Import styles:
```python
import math                                # use as math.sqrt()
from math import sqrt                      # use as sqrt()
from my_modules.my_math_module import add  # import from custom module
import session2_utils as utils             # import with alias
```

### → In Your ChocoPOS Today

```python
# *args — calculate_total accepts any number of (name, price) tuples
def calculate_total(*items, discount_rate: float = 0.0, apply_tax: bool = True) -> tuple:
    subtotal = sum(price for _, price in items)
    discount = subtotal * discount_rate
    after_discount = subtotal - discount
    tax = after_discount * TAX_RATE if apply_tax else 0.0
    total = math.ceil((after_discount + tax) * 100) / 100
    return subtotal, discount, tax, total

# **kwargs — build_receipt turns keyword args into receipt rows
def build_receipt(customer: str, timestamp: str, **line_items) -> str:
    for label, value in line_items.items():
        formatted_label = label.replace("_", " ").title()
        lines.append(utils.format_receipt_row(formatted_label, str(value)))

# Custom module — session2_utils.py is imported for formatting helpers
import session2_utils as utils
utils.print_header(SHOP_NAME, get_timestamp())
utils.format_currency(4.99)   # returns "$4.99"
```

---

## [1:25–2:00] Standard Library + Lambda (35 min)

**Files:** `session_02/04–06_python_standard_function_*.py`, `session_02/08_args_and_kwargs.py`, `session_02/09_lambda_functions.py`

**Concept: What is the Standard Library?**
- Python ships with hundreds of pre-built modules — no `pip install` needed
- Import only what you use

### `random` module (10 min)

| Function | What it does | Example result |
|---|---|---|
| `random.randint(1, 10)` | Random int, both ends inclusive | `7` |
| `random.random()` | Random float 0.0 to 1.0 | `0.4823` |
| `random.shuffle(my_list)` | Shuffles list **in-place** (modifies original, returns None) | list shuffled |
| `random.choice(my_list)` | Picks one random item | `"Mint Fusion"` |
| `random.sample(range(1,11), 3)` | 3 unique items from range, no repeats | `[4, 8, 2]` |

### `datetime` module (10 min)

| Code | What it does |
|---|---|
| `datetime.datetime.now()` | Current date and time |
| `now.strftime("%Y-%m-%d %H:%M:%S")` | Format as string |
| `datetime.datetime(2023, 4, 15)` | Create a specific date |
| `specific_date - now` | Returns `timedelta` (a duration) |

Format codes: `%Y` = 4-digit year, `%m` = month, `%d` = day, `%H` = hour (24h), `%M` = minute, `%S` = second, `%A` = weekday name, `%B` = month name

### `math` module (5 min)

| Code | Result |
|---|---|
| `math.sqrt(25)` | `5.0` |
| `math.ceil(8.1)` | `9` (round up) |
| `math.floor(8.9)` | `8` (round down) |
| `math.factorial(5)` | `120` |
| `math.pi` | `3.14159...` |

**Key:** `math.ceil()` is used in ChocoPOS to never shortchange the shop.

### `lambda`, `map()`, `filter()`, `sorted()` with key (10 min)

**`lambda` — anonymous (one-line) function:**
```python
double = lambda x: x * 2
double(5)   # 10

# More useful: as the key in sorted()
sorted(menu, key=lambda item: item["price"])
```

**`sorted()` with `key=`:**
```python
# Sort list of dicts by price
sorted(menu, key=lambda item: item["price"])

# Sort descending
sorted(units_sold.items(), key=lambda x: x[1], reverse=True)
```

**`filter()` — keep only items that match a condition:**
```python
affordable = list(filter(lambda item: item["price"] <= budget, menu))
```

**`map()` — transform every item:**
```python
formatted_prices = list(map(lambda item: f"${item['price']:.2f}", menu))
```

**`zip()` — iterate two sequences in parallel:**
```python
for item, price_str in zip(sorted_menu, formatted_prices):
    print(f"  {item['name']:<18} {price_str}")
```

### → In Your ChocoPOS Today

```python
def get_daily_special(menu: list) -> dict:
    shuffled = menu[:]          # copy — don't modify original
    random.shuffle(shuffled)    # in-place shuffle on the copy
    return random.choice(shuffled)

def get_timestamp() -> str:
    return datetime.datetime.now().strftime("%A, %B %d %Y  —  %H:%M")

def calculate_total(*items, discount_rate=0.0, apply_tax=True):
    ...
    total = math.ceil((after_discount + tax) * 100) / 100   # never shortchange

def display_menu(menu, sort_by="name", budget=None):
    sorted_menu = sorted(menu, key=lambda item: item[sort_by])       # lambda sort key
    if budget:
        sorted_menu = list(filter(lambda i: i["price"] <= budget, sorted_menu))  # filter
    formatted_prices = list(map(lambda i: utils.format_currency(i["price"]), sorted_menu))  # map
    for i, (item, price_str) in enumerate(zip(sorted_menu, formatted_prices), start=1):     # zip
        print(f"  {i}. {item['name']:<18} {price_str}")
```

---

## [1:55–2:00] Session 2 Checkpoint — Run Your Shop

```bash
python3 choco_pos/session2_menu.py
```

**Your shop can now:**
- Show a daily special chosen randomly
- Sort the menu by price
- Filter by customer budget
- Print a receipt with a timestamp
- Show a loyalty tier (Bronze / Silver / Gold)

**What it still can't do:** Remember stock levels. Every run the menu is full again. Session 3 fixes this.

---

---

# SESSION 3 (Hour 3) — Data Structures, File I/O & Exception Handling

## What You Will Build Today

`choco_pos/session3_tracker.py` — The shop now **remembers everything**:
- `catalog.json` is the live inventory — stock decreases with every sale
- Each order is appended to `orders.json`
- A `.txt` receipt is written to `receipts/`
- A sales report ranks products by units sold
- Bad input is handled gracefully with exceptions

**Run at the end:**
```bash
python3 choco_pos/session3_tracker.py
```

---

## [2:00–2:40] Data Structures (40 min)

**File:** `session_03/08_Data_Structures.py`, `session_03/11_advanced_data_structure_operations.py`

**Concept: Why data structures?**
- A single variable holds one value. A data structure holds many, organized differently.
- Different structures trade off: ordering, mutability, uniqueness, key-based access

### Lists (10 min)

```python
products = ["Dark Delight", "Milk Marvel", "White Wonder"]
```

- **Ordered** — items have a fixed position (index 0, 1, 2, ...)
- **Mutable** — add, remove, change items
- **Allows duplicates**
- **Zero-indexed** — first item is `[0]`, last is `[-1]`

| Operation | Code | Result |
|---|---|---|
| Access | `products[0]` | `"Dark Delight"` |
| Negative index | `products[-1]` | `"White Wonder"` |
| Append | `products.append("Mint Fusion")` | Adds to end |
| Extend | `products.extend(["Berry Bliss"])` | Adds a list |
| Iterate | `for p in products:` | — |

### Tuples (5 min)

```python
coordinates = (37.7749, -122.4194)   # immutable GPS point
```

- **Ordered**, **immutable** — cannot be changed after creation
- Use tuples for data that should never change: coordinates, RGB colors, menu entries
- Use lists when you need to add/remove/reorder

### Dictionaries (10 min)

```python
catalog = {
    "Dark Delight": {"price": 4.99, "stock": 10, "is_dark": True},
    "Milk Marvel":  {"price": 3.49, "stock": 15, "is_dark": False},
}
```

- **Key-value pairs** — access by key, not by position
- **Mutable** — add, update, remove pairs
- **Keys must be unique**
- **Ordered** (Python 3.7+) — insertion order preserved

| Operation | Code |
|---|---|
| Read | `catalog["Dark Delight"]` |
| Safe read (no error if missing) | `catalog.get("Unknown", {})` |
| Update | `catalog["Dark Delight"]["stock"] = 8` |
| Remove | `catalog.pop("Mint Fusion")` |
| All keys | `catalog.keys()` |
| All values | `catalog.values()` |
| All key-value pairs | `catalog.items()` |

**`dict.get()` with a default:** avoids `KeyError` when the key might not exist:
```python
units_sold.get("Dark Delight", 0)   # returns 0 if key doesn't exist
```

### Sets (5 min)

```python
my_set = {1, 2, 3, 2, 1}   # {1, 2, 3} — duplicates removed
```
- **Unordered** — no indexing
- **No duplicates** — useful for deduplication and membership tests
- `frozenset` — immutable set

### Strings Deep Dive (10 min)

Strings are sequences — you can index and slice them like lists.

| Operation | Code | Result |
|---|---|---|
| Length | `len("hello")` | `5` |
| Strip whitespace | `" hello ".strip()` | `"hello"` |
| Split | `"a|b|c".split("|")` | `["a","b","c"]` |
| Join | `"|".join(["a","b","c"])` | `"a|b|c"` |
| Replace | `"cat".replace("c","b")` | `"bat"` |
| Ends with | `"hello.py".endswith(".py")` | `True` |

**Strings are immutable** — methods return a NEW string, they never modify the original.

### Advanced Dict Operations (10 min)

**`enumerate()` — loop with index + value:**
```python
for i, (name, details) in enumerate(available, start=1):
    print(f"  {i}. {name:<18} ${details['price']:.2f}")
```

**`zip()` — pair two sequences:**
```python
ranks  = range(1, len(ranked) + 1)
names  = [name for name, _ in ranked]
qtys   = [qty  for _, qty  in ranked]

for rank, name, qty in zip(ranks, names, qtys):
    print(f"  {rank}. {name:<18} {qty} unit(s)")
```

**`sorted()` with `lambda` key + reverse:**
```python
# Sort catalog by price (cheapest first)
available = sorted(catalog.items(), key=lambda x: x[1]["price"])

# Sort sales tally by units sold (highest first)
ranked = sorted(units_sold.items(), key=lambda x: x[1], reverse=True)
```

**Nested data structures:**
```python
# Build sales tally from order history
units_sold = {}
for order in orders:
    for item in order["items"]:
        name = item["name"]
        units_sold[name] = units_sold.get(name, 0) + item["qty"]
```

### → In Your ChocoPOS Today

```python
# catalog.json loads into a nested dict
catalog = {
    "Dark Delight": {"price": 4.99, "stock": 10, "is_dark": True}
}

# .items() + sorted() — display menu by price
available = sorted(
    [(name, d) for name, d in catalog.items() if d["stock"] > 0],
    key=lambda x: x[1]["price"]
)
for i, (name, details) in enumerate(available, start=1):
    print(f"  {i}. {name:<18} ${details['price']:.2f}")

# .get() with default — build sales tally without KeyError
units_sold[name] = units_sold.get(name, 0) + item["qty"]

# zip() — sales report with rank numbers
for rank, name, qty in zip(range(1, len(ranked)+1), names, qtys):
    print(f"  {rank}. {name:<18} {qty} unit(s)")
```

---

## [2:40–3:00] File Handling, JSON & Exceptions (20 min)

**Files:** `session_03/09_file_handling_read.py`, `session_03/10_file_handling_write.py`, `session_03/12_exception_handling.py`, `session_03/13_json_file_handling.py`

### Reading Files (5 min)

**Four ways to read:**
```python
# 1. read() — whole file as one string
with open(file_path, "r") as f:
    content = f.read()

# 2. readlines() — list of lines (each includes \n)
with open(file_path, "r") as f:
    lines = f.readlines()

# 3. readline() in a loop — one line at a time (memory-efficient for large files)
with open(file_path, "r") as f:
    while True:
        line = f.readline()
        if not line: break
        print(line.strip())

# 4. Iterate directly — cleanest for line-by-line
with open(file_path, "r") as f:
    for line in f:
        print(line.strip())
```

**`with` statement (context manager):** automatically closes the file when the block exits — even if an error occurs. Always prefer `with open(...)` over manual `open()` + `close()`.

### Writing Files (5 min)

| Mode | Behavior |
|---|---|
| `"w"` | Overwrite entire file. Creates if not exists. |
| `"a"` | Append to end. Creates if not exists. |

```python
with open(file_path, "w") as f:
    f.write("Line 1\n")
    f.write("Line 2\n")
```

### JSON (5 min)

JSON is the universal format for storing and exchanging structured data.

| Function | Direction | Use |
|---|---|---|
| `json.load(f)` | JSON file → Python dict/list | Read from a file |
| `json.dump(data, f, indent=4)` | Python dict/list → JSON file | Write to a file |
| `json.loads(string)` | JSON string → Python dict/list | Parse from a string |
| `json.dumps(data)` | Python dict/list → JSON string | Serialize to string |

```python
import json

with open("catalog.json", "r") as f:
    catalog = json.load(f)              # dict

catalog["Dark Delight"]["stock"] -= 1  # update

with open("catalog.json", "w") as f:
    json.dump(catalog, f, indent=4)     # save back
```

### Exception Handling (5 min)

```python
try:
    qty = int(input("How many? ").strip())
    if qty <= 0:
        raise ValueError("Quantity must be at least 1.")
    if qty > details["stock"]:
        raise ValueError(f"Only {details['stock']} in stock.")
except ValueError as e:
    print(f"  Error: {e}")    # runs if ValueError raised in try
    continue
else:
    cart[name] = {"price": details["price"], "qty": qty}   # runs ONLY if NO exception
    details["stock"] -= qty
finally:
    save_catalog(catalog)     # ALWAYS runs — even if an exception occurred
```

| Block | When it runs |
|---|---|
| `try` | Always — the code that might fail |
| `except` | Only if an exception of the specified type was raised |
| `else` | Only if **no** exception was raised in `try` |
| `finally` | **Always** — exception or not — use for cleanup |

**Common exceptions:**
- `ValueError` — wrong type of value (e.g. `int("hello")`)
- `FileNotFoundError` — file doesn't exist
- `IndexError` — index out of range
- `KeyError` — dict key doesn't exist
- `TypeError` — wrong type for operation

**`raise`** — throw your own exceptions with a message:
```python
raise ValueError("Quantity must be at least 1.")
```

### → In Your ChocoPOS Today

```python
def load_catalog() -> dict:
    with open(CATALOG_FILE, "r") as f:
        return json.load(f)             # JSON → dict

def save_catalog(catalog: dict):
    with open(CATALOG_FILE, "w") as f:
        json.dump(catalog, f, indent=4) # dict → JSON file

def save_order(order: dict):
    orders = load_orders()              # read existing list
    orders.append(order)                # add new order
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)  # write whole list back

def write_receipt(order: dict) -> str:
    os.makedirs(RECEIPTS_DIR, exist_ok=True)
    file_path = os.path.join(RECEIPTS_DIR, f"receipt_{safe_ts}.txt")
    with open(file_path, "w") as f:
        f.write(f"  TOTAL: ${order['total']:.2f}\n")
    return file_path

# try/except/else/finally in take_order()
try:
    qty = int(input(f"  How many {name}? ").strip())
    if qty <= 0: raise ValueError("Must be at least 1.")
    if qty > details["stock"]: raise ValueError(f"Only {details['stock']} in stock.")
except ValueError as e:
    print(f"  Error: {e}")
    continue
else:
    cart[name] = {"price": details["price"], "qty": qty}
    details["stock"] -= qty
finally:
    save_catalog(catalog)   # always persists stock changes
```

---

## [2:55–3:00] Session 3 Checkpoint — Run Your Shop

```bash
python3 choco_pos/session3_tracker.py
```

**Your shop can now:**
- Load the catalog from `catalog.json` (stock survives restarts!)
- Decrement stock and save it back after every sale
- Save every order to `orders.json`
- Write a `.txt` receipt to `receipts/`
- Generate a sales report from order history
- Handle bad input gracefully (no crashes)

**What it still can't do:** The code is still procedural — functions and data are separate. Session 4 bundles them together into classes.

---

---

# SESSION 4 (Hour 4) — Object-Oriented Programming

## What You Will Build Today

`choco_pos/session4_shop_engine.py` — A complete OOP refactor of the shop:

```
Product (ABC)
│   @abstractmethod describe()
│   @property price (with setter validation)
│   @classmethod from_dict()
│   @staticmethod format_price()
│   __str__, __repr__, __eq__
│
├── ChocolateProduct(Product)
│       overrides from_dict()
│
└── SpecialProduct(ChocolateProduct)
        discounted_price @property
        overrides describe()  ← polymorphism

ShoppingCart
    private __validate()
    __len__, __str__

BaseShop (ABC)
    @abstractmethod open()

ChocoShop(BaseShop)
    private __load_catalog(), __save_catalog(), __save_order()
    implements open()
```

**Run at the end:**
```bash
python3 choco_pos/session4_shop_engine.py
```
Uses the same `catalog.json` and `orders.json` from Session 3.

---

## [3:00–3:20] Classes & Objects Fundamentals (20 min)

**Files:** `session_04/11_classes_and_objects.py`, `session_04/12_class_instance_attributes.py`, `session_04/13_class_methods.py`, `session_04/14_class_creating_objects.py`

**Concept: What is OOP and why?**
- Procedural code: functions acting on separate data
- OOP: **bundles data + behavior together** into one object
- Real-world analogy: `Car` is the blueprint (class), your actual car is the object (instance)

**Defining a class:**
```python
class Car:
    def __init__(self, color: str, brand: str):
        self.color = color    # instance attribute
        self.brand = brand    # instance attribute

    def start(self):
        print(f"{self.color} {self.brand} is starting.")
```
- `class Car:` — defines the blueprint (PascalCase convention)
- `__init__` — the **constructor** — runs automatically when you create an object
- `self` — refers to the specific object being created
- `self.color = color` — stores the argument as an attribute on the object

**Creating objects (instantiation):**
```python
car1 = Car("Red", "Toyota")
car2 = Car("Blue", "Honda")
car1.start()   # "Red Toyota is starting."
car2.start()   # "Blue Honda is starting."
```
Each object is independent — changing `car1.color` does not affect `car2`.

**Class attributes vs Instance attributes:**
```python
class Car:
    year = "2012"               # class attribute — shared by ALL Car objects

    def __init__(self, color, brand):
        self.color = color      # instance attribute — unique to each object
```

| | Class Attribute | Instance Attribute |
|---|---|---|
| Defined | In class body, outside `__init__` | Inside `__init__`, using `self.` |
| Shared? | Yes — same for all instances | No — each object has its own |
| Access | `Car.year` or `car1.year` | `car1.color` only |

**Private methods — name mangling:**
```python
class Car:
    def __start(self):      # double underscore = private (name-mangled)
        print("starting...")

    def start(self):        # public method
        self.__start()      # calls private method internally — correct
```
- `__method` → Python renames to `_ClassName__method` (name mangling)
- This signals "do not call from outside the class" — not true enforcement
- Single underscore `_method` → convention for "internal use", no renaming

### → In Your ChocoPOS Today

```python
class Product(ABC):
    tax_rate = 0.08     # class attribute — shared by ALL Product instances
    currency = "USD"    # class attribute

    def __init__(self, name: str, price: float, stock: int):
        self._name  = name    # instance attribute (single _ = "use the property")
        self._price = price
        self._stock = stock

class ShoppingCart:
    def __init__(self):
        self._items = []

    def __validate(self, qty: int):   # private method — called only inside the class
        if not isinstance(qty, int) or qty < 1:
            raise ValueError(f"Quantity must be a positive integer, got: {qty!r}")

    def add(self, product, qty=1):
        self.__validate(qty)   # call private method
        ...
```

---

## [3:20–3:35] Inheritance (15 min)

**File:** `session_04/15_class_objects_inheritance.py`

**Concept: What is inheritance?**
- A child class inherits all attributes and methods from a parent class
- Enables code reuse — define common behavior once in the parent
- The child can extend or override the parent's behavior

```python
from abc import ABC, abstractmethod

class Vehicle(ABC):              # Abstract Base Class — cannot be instantiated directly
    def __init__(self, color, brand):
        self.color = color
        self.brand = brand

    def start(self):             # concrete method — inherited as-is
        print(f"{self.color} {self.brand} is starting.")

    @abstractmethod
    def stop(self):              # abstract method — MUST be implemented by every subclass
        pass

class Car(Vehicle):
    def stop(self):              # provides the required implementation
        print(f"{self.color} {self.brand} is stopping.")

    def __init__(self, color, brand, doors):
        super().__init__(color, brand)   # call parent's __init__
        self.doors = doors
```

**Key concepts:**
- **`ABC`** (Abstract Base Class) — a class that exists only to be inherited, never instantiated directly
- **`@abstractmethod`** — if a subclass doesn't implement it, you get `TypeError` on instantiation
- **`super()`** — calls the parent class. Use `super().__init__(...)` to avoid duplicating init code
- **`class Car(Vehicle)`** — `Car` is the child/subclass, `Vehicle` is the parent/superclass

**Why abstract classes?** They enforce a contract: *"anything that claims to be a Vehicle MUST have a `stop()` method."*

### → In Your ChocoPOS Today

```python
# 3-level inheritance chain
class Product(ABC):          # level 1 — abstract base, cannot instantiate
    ...

class ChocolateProduct(Product):   # level 2 — concrete, implements describe()
    def __init__(self, name, price, stock, is_dark=False):
        super().__init__(name, price, stock)   # call Product.__init__
        self._is_dark = is_dark

    def describe(self) -> str:
        return "[Dark Chocolate]" if self._is_dark else "[Milk/White Chocolate]"

class SpecialProduct(ChocolateProduct):   # level 3 — adds discount, overrides describe()
    def __init__(self, name, price, stock, is_dark, discount_pct):
        super().__init__(name, price, stock, is_dark)  # call ChocolateProduct.__init__
        self._discount_pct = discount_pct

# Shop hierarchy
class BaseShop(ABC):
    @abstractmethod
    def open(self): pass

class ChocoShop(BaseShop):
    def __init__(self, name, owner):
        super().__init__(name, owner)
        self.__load_catalog()     # private — loads catalog.json on startup
```

---

## [3:35–3:45] Polymorphism & Method Overriding (10 min)

**Files:** `session_04/16_class_object_polymorphism.py`, `session_04/17_method_overriding.py`

**Concept: Polymorphism — "many forms"**
Same method name, different behavior per class. Python calls the right one at runtime.

```python
for animal in [budhia, rajib]:   # budhia is Cow, rajib is Human
    animal.eat()                  # Python picks the right eat() for each
```
You don't check `isinstance` — polymorphism handles dispatch automatically.

**Concept: Method overriding**
A child class provides its own version of a parent method, completely replacing it.

```python
class Vehicle:
    def start(self): print("Vehicle starting.")

class Car(Vehicle):
    def start(self): print("Car starting.")   # replaces Vehicle.start for Car objects
```

### → In Your ChocoPOS Today

```python
# describe() is @abstractmethod in Product
# ChocolateProduct implements it one way
class ChocolateProduct(Product):
    def describe(self) -> str:
        return "[Dark Chocolate]" if self._is_dark else "[Milk/White Chocolate]"

# SpecialProduct OVERRIDES it — same method name, completely different output
class SpecialProduct(ChocolateProduct):
    def describe(self) -> str:
        base = super().describe()   # reuse parent's output, then extend it
        return f"{base}  ★ SPECIAL {int(self._discount_pct * 100)}% OFF"

# Polymorphism in action — same loop handles both types
for product in self._catalog:
    print(product.describe())   # Python calls the right describe() per object type
```

---

## [3:45–4:00] Dunder Methods & Decorators (15 min)

**Files:** `session_04/18_dunder_methods.py`, `session_04/19_class_decorators.py`

### Dunder Methods (7 min)

Dunder = "double underscore". Python calls these automatically in specific situations.

| Dunder | Python calls it when you | Example output |
|---|---|---|
| `__str__` | `print(obj)` or `str(obj)` | `"Dark Delight  $4.99  (stock: 10)"` |
| `__repr__` | `repr(obj)`, in the REPL | `"ChocolateProduct(name='Dark Delight', ...)"` |
| `__eq__` | `obj1 == obj2` | `True` if names match |
| `__len__` | `len(obj)` | number of items in cart |
| `__lt__` | `obj1 < obj2` (also enables `sorted()`) | comparison by price |

```python
class Product:
    def __str__(self) -> str:
        return f"{self._name:<18} ${self._price:.2f}  (stock: {self._stock})"

    def __repr__(self) -> str:
        return f"ChocolateProduct(name='{self._name}', price={self._price})"

    def __eq__(self, other) -> bool:
        return isinstance(other, Product) and self._name == other._name
```

**Rule of thumb:** `__str__` is for humans (readable), `__repr__` is for developers (unambiguous, ideally enough to recreate the object).

### Decorators (8 min)

**`@property` — access a method like an attribute:**
```python
class Product:
    @property
    def price(self) -> float:
        return self._price        # call as product.price, not product.price()

    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError("Price cannot be negative.")
        self._price = value       # validates before storing
```
Why use `_price` + a property? The property controls how data is read and written — you can add validation without changing how callers use the attribute.

**`@classmethod` — method that receives the class, not the instance:**
```python
@classmethod
def from_dict(cls, name: str, data: dict):
    return cls(name=name, price=data["price"], stock=data["stock"])
```
- First parameter is `cls` (the class itself), not `self`
- Common use: **factory methods** — alternative constructors
- Called as `ChocolateProduct.from_dict("Dark Delight", {"price": 4.99, "stock": 10})`

**`@staticmethod` — regular function that lives inside a class:**
```python
@staticmethod
def format_price(amount: float) -> str:
    return f"${amount:.2f}"
```
- No `self`, no `cls` — doesn't touch the object or class
- Use when the logic is related to the class conceptually, but doesn't need instance/class data
- Called as `Product.format_price(4.99)` → `"$4.99"`

### → In Your ChocoPOS Today

```python
# @property + setter — price with validation
@property
def price(self) -> float:
    return self._price

@price.setter
def price(self, value: float):
    if value < 0:
        raise ValueError(f"Price cannot be negative: {value}")
    self._price = value

# @classmethod — factory from catalog.json dict
@classmethod
def from_dict(cls, name: str, data: dict):
    return cls(name=name, price=data["price"], stock=data["stock"])
# Usage: ChocolateProduct.from_dict("Dark Delight", {"price": 4.99, "stock": 10})

# @staticmethod — formatting utility with no instance state needed
@staticmethod
def format_price(amount: float) -> str:
    return f"${amount:.2f}"
# Usage: Product.format_price(4.99)  →  "$4.99"

# __str__ — what prints when you do print(product)
def __str__(self) -> str:
    return (f"{self._name:<18} {self.format_price(self._price)}"
            f"  (stock: {self._stock})  {self.describe()}")

# __len__ — len(cart) returns number of items
def __len__(self) -> int:
    return len(self._items)

# __eq__ — cart1 == cart2 compares by name
def __eq__(self, other) -> bool:
    return isinstance(other, Product) and self._name == other._name
```

---

## [3:55–4:00] Session 4 Checkpoint — Run Your Shop

```bash
python3 choco_pos/session4_shop_engine.py
```

**Your shop can now:**
- Load products from `catalog.json` into proper `ChocolateProduct` objects
- Use `@property` to validate prices before accepting them
- Build a `ShoppingCart` that calculates subtotal, tax, and total
- Display a clean receipt via `__str__`
- Save orders and update stock (same files as Session 3)

**The 4 pillars of OOP — where you saw each in ChocoPOS:**

| Pillar | What it means | In ChocoPOS |
|---|---|---|
| **Encapsulation** | Bundle data + methods, hide internals | `ShoppingCart.__validate()`, `ChocoShop.__load_catalog()` |
| **Abstraction** | Hide implementation behind a contract | `Product(ABC)`, `BaseShop(ABC)`, `@abstractmethod` |
| **Inheritance** | Reuse parent code in child classes | `SpecialProduct → ChocolateProduct → Product` |
| **Polymorphism** | Same method, different behavior | `describe()` on `ChocolateProduct` vs `SpecialProduct` |

---

---

# Quick Reference

## Module-to-Session Map

| Session | Hour | Concept Files | ChocoPOS File |
|---|---|---|---|
| 1 | 0–60 min | `session_01/` → `hello_world.py`, `01_variables_and_datatypes.py`, `02_control_structures.py`, `03_logical_operators.py`, `04_string_slicing.py` | `choco_pos/session1_receipt.py` |
| 2 | 61–120 min | `session_02/` → `03_python_functions_and_modules.py`, `04–06_stdlib.py`, `07_import_module_example.py`, `08_args_and_kwargs.py`, `09_lambda_functions.py`, `my_modules/` | `choco_pos/session2_menu.py` + `session2_utils.py` |
| 3 | 121–180 min | `session_03/` → `08_Data_Structures.py`, `09_file_handling_read.py`, `10_file_handling_write.py`, `11_advanced_data_structure_operations.py`, `12_exception_handling.py`, `13_json_file_handling.py`, `data/` | `choco_pos/session3_tracker.py` |
| 4 | 181–240 min | `session_04/` → `11_classes_and_objects.py` through `17_method_overriding.py`, `18_dunder_methods.py`, `19_class_decorators.py` | `choco_pos/session4_shop_engine.py` |

## ChocoPOS File Map

```
choco_pos/
├── catalog.json             ← product inventory (Sessions 3 & 4 read/write this)
├── orders.json              ← order history (created on first sale)
├── session1_receipt.py      ← Session 1: vars, loops, if/else, list comprehension
├── session2_utils.py        ← Session 2: custom module (imported by session2_menu.py)
├── session2_menu.py         ← Session 2: functions, *args/**kwargs, lambda, stdlib
├── session3_tracker.py      ← Session 3: JSON, file I/O, exceptions, dict methods
├── session4_shop_engine.py  ← Session 4: full OOP class hierarchy
└── receipts/                ← .txt receipt files written by Sessions 3 & 4
```

## Session Progression Story

Use these transitions to connect each session to the next:

| Transition | The problem | The solution |
|---|---|---|
| S1 → S2 | "The code is one big blob — hard to reuse or test" | Wrap everything in named functions |
| S2 → S3 | "The cart disappears after every run — no memory" | Load and save to JSON files |
| S3 → S4 | "Functions and data are separate — hard to reason about" | Bundle them into classes |
