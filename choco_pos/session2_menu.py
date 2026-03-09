# ============================================================
#  ChocoPOS — SESSION 2: The Smart Menu System
#  Chocolate Fantasy | Multi-product Menu with Business Logic
# ============================================================
#
#  NEW CONCEPTS ADDED THIS SESSION:
#    functions (def, return, type hints, default params),
#    global vs local scope, *args, **kwargs,
#    lambda, map(), filter(), sorted() with key=,
#    random (choice, shuffle), datetime (now, strftime),
#    math (ceil), custom module import (session2_utils)
#
#  WHAT'S NEW vs SESSION 1:
#    - Every behaviour is now wrapped in a named function
#    - A daily special is picked randomly each time the shop opens
#    - The menu can be sorted by price or name
#    - Receipts carry a timestamp
#    - A loyalty tier is calculated using math
# ============================================================

import random
import datetime
import math
import sys
import os

# Import our custom module (same folder)
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
import session2_utils as utils

# --- Module-level globals (demonstrate global scope) ---
SHOP_NAME    = "Chocolate Fantasy"
TAX_RATE     = 0.08   # shared constant — functions read this but do not reassign it

MENU = [
    {"name": "Dark Delight",  "price": 4.99, "is_dark": True},
    {"name": "Milk Marvel",   "price": 3.49, "is_dark": False},
    {"name": "White Wonder",  "price": 3.99, "is_dark": False},
    {"name": "Mint Fusion",   "price": 5.10, "is_dark": True},
    {"name": "Berry Bliss",   "price": 4.49, "is_dark": False},
]


# ---- Functions ----

def get_timestamp() -> str:
    """Return a formatted current date-time string."""
    return datetime.datetime.now().strftime("%A, %B %d %Y  —  %H:%M")


def get_daily_special(menu: list) -> dict:
    """Pick one random item as today's special using random.choice."""
    shuffled = menu[:]
    random.shuffle(shuffled)           # shuffle first for extra randomness
    special = random.choice(shuffled)
    return special


def display_menu(menu: list, sort_by: str = "name", budget: float = None) -> list:
    """
    Show the menu, optionally sorted and filtered by budget.
    Demonstrates: sorted() with key=lambda, filter(), map(), zip()
    """
    # lambda as the sort key
    sorted_menu = sorted(menu, key=lambda item: item[sort_by])

    # filter: only show items within budget if one is given
    if budget is not None:
        sorted_menu = list(filter(lambda item: item["price"] <= budget, sorted_menu))

    # map: pre-format all prices as strings
    formatted_prices = list(map(lambda item: utils.format_currency(item["price"]), sorted_menu))

    print(f"\n  {'#':<4} {'Product':<18} {'Price':<8}")
    print(f"  {'─' * 34}")

    # zip: iterate items and their pre-formatted prices together
    for i, (item, price_str) in enumerate(zip(sorted_menu, formatted_prices), start=1):
        star = " ★ SPECIAL" if item.get("is_special") else ""
        print(f"  {i:<4} {item['name']:<18} {price_str}{star}")

    return sorted_menu


def calculate_total(*items, discount_rate: float = 0.0, apply_tax: bool = True) -> tuple:
    """
    Accept any number of (name, price) tuples via *args.
    Returns (subtotal, discount, tax, total).
    math.ceil is used to round up to the nearest cent.
    """
    subtotal = sum(price for _, price in items)
    discount = subtotal * discount_rate
    after_discount = subtotal - discount
    tax   = after_discount * TAX_RATE if apply_tax else 0.0
    total = math.ceil((after_discount + tax) * 100) / 100   # never shortchange the shop
    return subtotal, discount, tax, total


def build_receipt(customer: str, timestamp: str, **line_items) -> str:
    """
    Build a receipt string from arbitrary **kwargs.
    Each kwarg becomes a labelled row on the receipt.
    """
    lines = [
        utils.make_border(),
        f"  {SHOP_NAME.upper()} — RECEIPT",
        f"  Customer : {customer}",
        f"  Date     : {timestamp}",
        utils.make_border("-"),
    ]
    for label, value in line_items.items():
        formatted_label = label.replace("_", " ").title()
        lines.append(utils.format_receipt_row(formatted_label, str(value)))
    lines.append(utils.make_border())
    return "\n".join(lines)


def get_loyalty_tier(total_spent: float) -> str:
    """
    Gamified tier using math.sqrt.
    Local variable 'score' only exists inside this function — not global.
    """
    score = math.floor(math.sqrt(total_spent * 10))  # local variable
    if score >= 10:
        return "GOLD  🏆"
    elif score >= 6:
        return "SILVER ⭐"
    else:
        return "BRONZE 🍫"


# ---- Main ----

if __name__ == "__main__":
    # Header using custom module and datetime
    utils.print_header(SHOP_NAME, get_timestamp())

    # Daily special using random
    special = get_daily_special(MENU)
    special["is_special"] = True
    print(f"\n  TODAY'S SPECIAL: {special['name']} — 20% OFF!")

    # Display menu sorted by price (default param demo)
    sorted_menu = display_menu(MENU, sort_by="price")

    customer = input("\n  Your name: ").strip()

    # Optional budget filter (default param: budget=None means no filter)
    budget_input = input("  Max price per item (Enter to skip): ").strip()
    if budget_input:
        try:
            budget = float(budget_input)
            print(f"\n  Showing items up to {utils.format_currency(budget)}:")
            sorted_menu = display_menu(MENU, sort_by="price", budget=budget)
        except ValueError:
            print("  Invalid budget — showing full menu.")

    # Shopping
    cart = []
    while True:
        choice = input("\n  Add item number (or 'done'): ").strip()
        if choice.lower() == "done":
            break
        if not choice.isdigit() or not (1 <= int(choice) <= len(sorted_menu)):
            print("  Invalid choice.")
            continue
        item = sorted_menu[int(choice) - 1]
        # Apply 20% if it is today's special
        price = item["price"] * 0.80 if item.get("is_special") else item["price"]
        cart.append((item["name"], price))
        print(f"  Added: {item['name']}  ({utils.format_currency(price)})")

    if not cart:
        print("\n  No items ordered. Come back soon!")
    else:
        discount_rate = 0.10 if len(cart) >= 3 else 0.0
        subtotal, discount, tax, total = calculate_total(*cart, discount_rate=discount_rate)

        # build_receipt uses **kwargs — each named argument becomes a receipt row
        receipt = build_receipt(
            customer    = customer,
            timestamp   = get_timestamp(),
            subtotal    = utils.format_currency(subtotal),
            discount    = f"-{utils.format_currency(discount)}" if discount else "—",
            tax         = utils.format_currency(tax),
            total       = utils.format_currency(total),
        )
        print("\n" + receipt)

        tier = get_loyalty_tier(total)
        print(f"\n  Loyalty Tier: {tier}")
        print(f"  Thank you, {customer}! See you at {SHOP_NAME}!")
