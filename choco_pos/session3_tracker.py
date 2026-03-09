# ============================================================
#  ChocoPOS — SESSION 3: The Inventory & Sales Tracker
#  Chocolate Fantasy | Persistent Catalog + Order History
# ============================================================
#
#  NEW CONCEPTS ADDED THIS SESSION:
#    dict methods (keys, values, items, get, pop),
#    list methods (append, sort, sorted), enumerate(), zip(),
#    nested data structures (list of dicts, dict of dicts),
#    try/except/else/finally, raise, common exceptions,
#    file reading/writing (with, read, readlines, write),
#    JSON (json.load, json.dump, json.loads, json.dumps)
#
#  WHAT'S NEW vs SESSION 2:
#    - Catalog loaded from catalog.json (survives restarts)
#    - Stock levels tracked and saved after every order
#    - Orders persisted to orders.json
#    - Receipts written as .txt files
#    - Out-of-stock and bad input handled with exceptions
#    - Sales report generated from saved order history
# ============================================================

import json
import os
import datetime

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
CATALOG_FILE = os.path.join(BASE_DIR, "catalog.json")
ORDERS_FILE  = os.path.join(BASE_DIR, "orders.json")
RECEIPTS_DIR = os.path.join(BASE_DIR, "receipts")
SHOP_NAME    = "Chocolate Fantasy"


# ============================================================
# PART 1 — Catalog I/O (JSON)
# ============================================================

def load_catalog() -> dict:
    """Load product catalog from JSON. Raises on missing or corrupted file."""
    try:
        with open(CATALOG_FILE, "r") as f:
            catalog = json.load(f)
    except FileNotFoundError:
        raise FileNotFoundError(f"Catalog not found at: {CATALOG_FILE}")
    except json.JSONDecodeError:
        raise ValueError("catalog.json is corrupted. Please restore it.")
    return catalog


def save_catalog(catalog: dict):
    """Persist the catalog (with updated stock) back to JSON."""
    with open(CATALOG_FILE, "w") as f:
        json.dump(catalog, f, indent=4)


# ============================================================
# PART 2 — Order I/O (JSON + txt receipts)
# ============================================================

def load_orders() -> list:
    """Load order history. Returns empty list if no orders yet."""
    try:
        with open(ORDERS_FILE, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return []     # first run — perfectly fine


def save_order(order: dict):
    """Append one order to the order history JSON file."""
    orders = load_orders()
    orders.append(order)
    with open(ORDERS_FILE, "w") as f:
        json.dump(orders, f, indent=4)


def write_receipt(order: dict) -> str:
    """Write a receipt .txt file for the order. Returns the file path."""
    os.makedirs(RECEIPTS_DIR, exist_ok=True)
    safe_ts   = order["timestamp"].replace(":", "-").replace(" ", "_")
    file_path = os.path.join(RECEIPTS_DIR, f"receipt_{safe_ts}.txt")

    with open(file_path, "w") as f:
        f.write(f"{'=' * 42}\n")
        f.write(f"  {SHOP_NAME} — Receipt\n")
        f.write(f"  Customer : {order['customer']}\n")
        f.write(f"  Date     : {order['timestamp']}\n")
        f.write(f"  {'─' * 38}\n")
        for item in order["items"]:
            line_total = item["price"] * item["qty"]
            f.write(f"  {item['name']:<18} x{item['qty']}   ${line_total:.2f}\n")
        f.write(f"  {'─' * 38}\n")
        f.write(f"  TOTAL: ${order['total']:.2f}\n")
        f.write(f"{'=' * 42}\n")

    return file_path


# ============================================================
# PART 3 — Display
# ============================================================

def display_menu(catalog: dict) -> list:
    """
    Show only in-stock items sorted by price.
    Returns a list of (name, details) tuples for index-based selection.
    Uses: dict.items(), sorted() with lambda, enumerate()
    """
    # dict comprehension + .items() to filter in-stock only
    available = [(name, details)
                 for name, details in catalog.items()
                 if details["stock"] > 0]

    # Sort by price using a lambda key
    available = sorted(available, key=lambda x: x[1]["price"])

    if not available:
        print("\n  Sorry — we are completely out of stock today!")
        return []

    print("\n  --- Available Products ---")
    # enumerate() gives us both index and value
    for i, (name, details) in enumerate(available, start=1):
        tag = "[DARK]" if details.get("is_dark") else ""
        print(f"  {i}. {name:<18} ${details['price']:.2f}  "
              f"Stock: {details['stock']}  {tag}")

    return available


def display_sales_report():
    """
    Read orders.json and print a sales summary.
    Uses: list of dicts, dict.get(), sorted(), zip()
    """
    orders = load_orders()
    if not orders:
        print("\n  No orders on record yet.")
        return

    total_revenue = sum(order["total"] for order in orders)

    # Build a sales tally using dict.get() with a default of 0
    units_sold = {}
    for order in orders:
        for item in order["items"]:
            name = item["name"]
            units_sold[name] = units_sold.get(name, 0) + item["qty"]

    # Sort by units sold descending
    ranked = sorted(units_sold.items(), key=lambda x: x[1], reverse=True)

    # Pair rank numbers with results using zip()
    ranks   = range(1, len(ranked) + 1)
    product_names = [name for name, _ in ranked]
    qtys          = [qty  for _, qty  in ranked]

    print(f"\n  --- Sales Report ---")
    print(f"  Total orders : {len(orders)}")
    print(f"  Total revenue: ${total_revenue:.2f}")
    print(f"\n  Units sold:")
    for rank, name, qty in zip(ranks, product_names, qtys):
        print(f"    {rank}. {name:<18} {qty} unit(s)")


# ============================================================
# PART 4 — Order flow
# ============================================================

def take_order(catalog: dict) -> dict | None:
    """
    Interactive order flow with full exception handling.
    Uses: try/except/else/finally, raise, ValueError, IndexError, KeyError
    """
    available = display_menu(catalog)
    if not available:
        return None

    customer = input("\n  Customer name: ").strip()
    if not customer:
        raise ValueError("Customer name cannot be empty.")

    cart = {}   # { product_name: {"price": float, "qty": int} }

    while True:
        choice = input("  Item number to add (or 'done'): ").strip()
        if choice.lower() == "done":
            break

        try:
            idx = int(choice) - 1
            if not (0 <= idx < len(available)):
                raise IndexError("Selection out of range.")
        except (ValueError, IndexError):
            print("  Please enter a valid item number.")
            continue

        name, details = available[idx]

        try:
            qty = int(input(f"  How many {name}? ").strip())
            if qty <= 0:
                raise ValueError("Quantity must be at least 1.")
            if qty > details["stock"]:
                raise ValueError(f"Only {details['stock']} unit(s) of {name} in stock.")
        except ValueError as e:
            print(f"  Error: {e}")
            continue
        else:
            # else block: runs only if NO exception was raised in try
            if name in cart:
                cart[name]["qty"] += qty
            else:
                cart[name] = {"price": details["price"], "qty": qty}
            details["stock"] -= qty
            print(f"  Added {qty}x {name}.")

    if not cart:
        return None

    timestamp = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    total     = sum(v["price"] * v["qty"] for v in cart.values())

    return {
        "customer"  : customer,
        "timestamp" : timestamp,
        "items"     : [{"name": k, "price": v["price"], "qty": v["qty"]}
                       for k, v in cart.items()],
        "total"     : round(total, 2),
    }


# ============================================================
# PART 5 — Main loop
# ============================================================

if __name__ == "__main__":
    print("=" * 42)
    print(f"  {SHOP_NAME} — Inventory & Sales Tracker")
    print("=" * 42)

    # Load catalog — crash with a clean message if file is missing
    try:
        catalog = load_catalog()
    except (FileNotFoundError, ValueError) as e:
        print(f"\n  Startup error: {e}")
        exit(1)

    while True:
        print("\n  [O] New order   [R] Sales report   [Q] Quit")
        action = input("  > ").strip().upper()

        if action == "Q":
            save_catalog(catalog)
            print("  Catalog saved. Goodbye!")
            break

        elif action == "O":
            try:
                order = take_order(catalog)
                if order:
                    save_order(order)
                    receipt_path = write_receipt(order)
                    print(f"\n  Order saved!  Total: ${order['total']:.2f}")
                    print(f"  Receipt: {receipt_path}")
                else:
                    print("  No order placed.")
            except ValueError as e:
                print(f"  Order error: {e}")
            finally:
                # finally: ALWAYS save stock changes, even if an error occurred
                save_catalog(catalog)

        elif action == "R":
            display_sales_report()

        else:
            print("  Unknown option. Please choose O, R, or Q.")
