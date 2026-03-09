# ============================================================
#  ChocoPOS — SESSION 1: The Receipt Printer
#  Chocolate Fantasy | Point of Sale Terminal
# ============================================================
#
#  CONCEPTS USED:
#    variables, data types, f-strings, format specifiers,
#    input(), if/elif/else, for loop, while loop, break,
#    continue, logical operators (and/or/not, in/not in),
#    list comprehension, string slicing
#
#  WHAT IT DOES:
#    Greets the customer, shows a menu, lets them add
#    chocolates to a cart, applies a tiered discount,
#    and prints a formatted receipt.
# ============================================================

SHOP_NAME  = "Chocolate Fantasy"
OWNER      = "Rajib"
CITY       = "California"
BORDER     = "=" * 42

# Menu: list of tuples — (name, price, is_dark)
MENU = [
    ("Dark Delight",  4.99, True),
    ("Milk Marvel",   3.49, False),
    ("White Wonder",  3.99, False),
    ("Mint Fusion",   5.10, True),
    ("Berry Bliss",   4.49, False),
]


def run_session():
    # --- Welcome banner using variables and f-strings ---
    print(BORDER)
    print(f"  Welcome to {SHOP_NAME}!")
    print(f"  Owner: {OWNER}  |  {CITY}")
    print(BORDER)

    # --- Customer name using input() ---
    customer_name = input("\nWhat is your name? ").strip()
    # String slicing: cap the display name at 15 characters so it fits the receipt
    display_name = customer_name[:15]
    print(f"\nHello, {display_name}! Let's get you some chocolate.")

    # --- Show menu using a for loop ---
    print("\n--- Today's Menu ---")
    for i, (name, price, is_dark) in enumerate(MENU, start=1):
        tag = "[DARK]" if is_dark else ""
        print(f"  {i}. {name:<16} ${price:.2f}  {tag}")

    # --- List comprehension: preview bulk prices ---
    bulk_prices = [f"${p * 0.9:.2f}" for _, p, _ in MENU]
    print(f"\n  Bulk prices (10% off, 3+ items): {bulk_prices}")

    # --- Shopping loop using while, break, continue, logical operators ---
    cart  = []
    total = 0.0

    while True:
        print(f"\n  Cart: {len(cart)} item(s)  |  Running total: ${total:.2f}")
        choice = input("  Item number to add, or 'done' to checkout: ").strip()

        if choice.lower() == "done":
            break

        # continue: skip non-numeric input
        if not choice.isdigit():
            print("  Please enter a number.")
            continue

        item_num = int(choice)
        if item_num < 1 or item_num > len(MENU):
            print(f"  Choose between 1 and {len(MENU)}.")
            continue

        name, price, is_dark = MENU[item_num - 1]

        # Logical operators: warn about dark chocolate
        if is_dark and display_name not in ["", " "]:
            print(f"  {name} is a rich dark chocolate — bold choice!")

        # not in: avoid adding an item that is already 3 times in cart
        existing_count = sum(1 for n, _ in cart if n == name)
        if existing_count >= 3:
            print(f"  You already have 3x {name}. Are you sure?")
            confirm = input("  Add anyway? (yes/no): ").strip().lower()
            if confirm not in ["yes", "y"]:
                continue

        cart.append((name, price))
        total += price
        print(f"  Added: {name}  (${price:.2f})")

    # --- Checkout ---
    if not cart:
        print("\nNo items added. Come back soon!")
        return

    # Tiered discount using if/elif/else
    if len(cart) >= 5:
        discount_pct = 0.15
        tier_label   = "Gold (15%)"
    elif len(cart) >= 3:
        discount_pct = 0.10
        tier_label   = "Loyalty (10%)"
    else:
        discount_pct = 0.0
        tier_label   = None

    discount_amount = total * discount_pct
    final_total     = total - discount_amount

    # --- Print receipt ---
    print(f"\n{BORDER}")
    print(f"  {SHOP_NAME.upper()}")
    print(f"  Customer: {display_name}")
    print(f"  {'─' * 38}")
    for name, price in cart:
        print(f"  {name:<22}  ${price:.2f}")
    print(f"  {'─' * 38}")
    if tier_label:
        print(f"  Subtotal:                 ${total:.2f}")
        print(f"  Discount — {tier_label}:  -${discount_amount:.2f}")
    print(f"  TOTAL:                    ${final_total:.2f}")
    print(BORDER)
    print(f"  Thank you, {display_name}! Enjoy your chocolates!")
    print(BORDER)


if __name__ == "__main__":
    # Outer loop: allow multiple orders in one session
    while True:
        run_session()
        again = input("\nPlace another order? (yes/no): ").strip().lower()
        if again not in ["yes", "y"]:
            break

    print(f"\nGoodbye! See you at {SHOP_NAME}!")
