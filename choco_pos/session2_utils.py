# ============================================================
#  ChocoPOS — Session 2 Custom Module: session2_utils.py
#  Reusable formatting helpers imported by session2_menu.py
# ============================================================
#
#  This file is a custom module — it demonstrates how to split
#  reusable code out of a main script and import it.
# ============================================================

BORDER_WIDTH = 46


def make_border(char: str = "=", width: int = BORDER_WIDTH) -> str:
    return char * width


def format_currency(amount: float) -> str:
    return f"${amount:.2f}"


def format_receipt_row(label: str, value: str, width: int = BORDER_WIDTH) -> str:
    """Left-align label, right-align value within a fixed width."""
    padding = width - len(label) - len(value) - 4
    return f"  {label}{' ' * padding}{value}"


def print_header(shop_name: str, timestamp: str):
    print(make_border())
    print(f"  {shop_name.upper()}")
    print(f"  {timestamp}")
    print(make_border("-"))
