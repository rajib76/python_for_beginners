# ============================================================
#  ChocoPOS — SESSION 4: The Full OOP Shop Engine
#  Chocolate Fantasy | Complete Object-Oriented Refactor
# ============================================================
#
#  NEW CONCEPTS ADDED THIS SESSION:
#    class, __init__, instance attributes, class attributes,
#    methods, private methods (__), inheritance, super(),
#    ABC + @abstractmethod, polymorphism, method overriding,
#    __str__, __repr__, __eq__, __len__,
#    @property + setter, @classmethod, @staticmethod
#
#  WHAT'S NEW vs SESSION 3:
#    - All data and behaviour is now bundled into classes
#    - Product is an abstract base class — every chocolate type
#      must implement describe()
#    - ChocolateProduct and SpecialProduct are concrete subclasses
#    - ShoppingCart manages items and total calculation
#    - ChocoShop orchestrates everything and inherits from BaseShop
#    - Same catalog.json and orders.json from Session 3 still work
# ============================================================

import json
import os
import datetime
from abc import ABC, abstractmethod

BASE_DIR     = os.path.dirname(os.path.abspath(__file__))
CATALOG_FILE = os.path.join(BASE_DIR, "catalog.json")
ORDERS_FILE  = os.path.join(BASE_DIR, "orders.json")


# ============================================================
# Product hierarchy
# ============================================================

class Product(ABC):
    """
    Abstract Base Class — cannot be instantiated directly.
    Every product type MUST implement describe().
    """

    # Class attributes — shared across ALL Product instances
    tax_rate = 0.08
    currency = "USD"

    def __init__(self, name: str, price: float, stock: int):
        # Single underscore: "internal, use the property"
        self._name  = name
        self._price = price
        self._stock = stock

    # --- @property: access as attribute, no parentheses needed ---
    @property
    def name(self) -> str:
        return self._name

    @property
    def price(self) -> float:
        return self._price

    # --- @property setter: validate before storing ---
    @price.setter
    def price(self, value: float):
        if value < 0:
            raise ValueError(f"Price cannot be negative: {value}")
        self._price = value

    @property
    def stock(self) -> int:
        return self._stock

    @property
    def is_available(self) -> bool:
        return self._stock > 0

    def reduce_stock(self, qty: int = 1):
        if qty > self._stock:
            raise ValueError(
                f"Only {self._stock} unit(s) of '{self._name}' available, "
                f"but {qty} were requested."
            )
        self._stock -= qty

    # --- @abstractmethod: subclasses MUST provide their own version ---
    @abstractmethod
    def describe(self) -> str:
        pass

    # --- @classmethod: factory — create a Product from a JSON dict ---
    @classmethod
    def from_dict(cls, name: str, data: dict):
        return cls(name=name, price=data["price"], stock=data["stock"])

    # --- @staticmethod: utility that needs no self or cls ---
    @staticmethod
    def format_price(amount: float) -> str:
        return f"${amount:.2f}"

    def to_dict(self) -> dict:
        return {"price": self._price, "stock": self._stock, "is_dark": False}

    # --- Dunder methods ---
    def __str__(self) -> str:
        return (f"{self._name:<18} {self.format_price(self._price)}"
                f"  (stock: {self._stock})  {self.describe()}")

    def __repr__(self) -> str:
        return (f"{self.__class__.__name__}("
                f"name='{self._name}', price={self._price}, stock={self._stock})")

    def __eq__(self, other) -> bool:
        return isinstance(other, Product) and self._name == other._name


class ChocolateProduct(Product):
    """A standard chocolate bar — Dark or Milk/White."""

    def __init__(self, name: str, price: float, stock: int, is_dark: bool = False):
        super().__init__(name, price, stock)   # call parent __init__
        self._is_dark = is_dark

    @property
    def is_dark(self) -> bool:
        return self._is_dark

    def describe(self) -> str:
        return "[Dark Chocolate]" if self._is_dark else "[Milk/White Chocolate]"

    def to_dict(self) -> dict:
        return {"price": self._price, "stock": self._stock, "is_dark": self._is_dark}

    # Override the parent @classmethod to also read is_dark
    @classmethod
    def from_dict(cls, name: str, data: dict):
        return cls(
            name    = name,
            price   = data["price"],
            stock   = data["stock"],
            is_dark = data.get("is_dark", False),
        )


class SpecialProduct(ChocolateProduct):
    """
    A limited-edition seasonal chocolate with an extra discount.
    Inherits from ChocolateProduct which inherits from Product.
    """

    def __init__(self, name: str, price: float, stock: int,
                 is_dark: bool, discount_pct: float):
        super().__init__(name, price, stock, is_dark)
        self._discount_pct = discount_pct

    @property
    def discounted_price(self) -> float:
        return self._price * (1 - self._discount_pct)

    # Override describe() — polymorphism: same method name, different output
    def describe(self) -> str:
        base = super().describe()
        return (f"{base}  ★ SPECIAL "
                f"{int(self._discount_pct * 100)}% OFF "
                f"→ {self.format_price(self.discounted_price)}")


# ============================================================
# ShoppingCart
# ============================================================

class ShoppingCart:
    """Manages the items a customer wants to buy."""

    def __init__(self):
        self._items = []   # list of (Product, qty) tuples

    def add(self, product: Product, qty: int = 1):
        self.__validate(qty)        # private method call
        product.reduce_stock(qty)
        self._items.append((product, qty))

    def __validate(self, qty: int):
        """Private: raise before doing anything if qty is bad."""
        if not isinstance(qty, int) or qty < 1:
            raise ValueError(f"Quantity must be a positive integer, got: {qty!r}")

    @property
    def subtotal(self) -> float:
        return sum(
            (p.discounted_price if isinstance(p, SpecialProduct) else p.price) * q
            for p, q in self._items
        )

    @property
    def tax(self) -> float:
        return self.subtotal * Product.tax_rate   # uses class attribute

    @property
    def total(self) -> float:
        return self.subtotal + self.tax

    def __len__(self) -> int:
        return len(self._items)

    def __str__(self) -> str:
        if not self._items:
            return "  (cart is empty)"
        lines = ["  --- Your Cart ---"]
        for product, qty in self._items:
            unit = (product.discounted_price
                    if isinstance(product, SpecialProduct) else product.price)
            lines.append(f"  {product.name:<18} x{qty}  "
                         f"{Product.format_price(unit * qty)}")
        lines.append(f"  {'─' * 36}")
        lines.append(f"  Subtotal : {Product.format_price(self.subtotal)}")
        lines.append(f"  Tax (8%) : {Product.format_price(self.tax)}")
        lines.append(f"  TOTAL    : {Product.format_price(self.total)}")
        return "\n".join(lines)

    def to_order_dict(self, customer: str) -> dict:
        return {
            "customer"  : customer,
            "timestamp" : datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            "items"     : [{"name": p.name, "price": p.price, "qty": q}
                           for p, q in self._items],
            "total"     : round(self.total, 2),
        }


# ============================================================
# Shop hierarchy
# ============================================================

class BaseShop(ABC):
    """Abstract base — defines the interface all shops must follow."""

    def __init__(self, name: str, owner: str):
        self.name  = name
        self.owner = owner

    @abstractmethod
    def open(self):
        """Every shop subclass must implement how it opens."""
        pass

    def welcome(self):
        print("=" * 44)
        print(f"  {self.name}")
        print(f"  Owner: {self.owner}")
        print(f"  {datetime.datetime.now().strftime('%A, %B %d %Y')}")
        print("=" * 44)


class ChocoShop(BaseShop):
    """
    Concrete shop. Inherits welcome() from BaseShop,
    implements open(), and manages its own catalog privately.
    """

    def __init__(self, name: str, owner: str):
        super().__init__(name, owner)
        self._catalog: list[Product] = []
        self.__load_catalog()   # private — called internally, not exposed

    # --- Private methods ---

    def __load_catalog(self):
        """Load catalog.json and create ChocolateProduct objects."""
        try:
            with open(CATALOG_FILE, "r") as f:
                data = json.load(f)
            for product_name, details in data.items():
                self._catalog.append(
                    ChocolateProduct.from_dict(product_name, details)
                )
        except FileNotFoundError:
            print(f"  Warning: {CATALOG_FILE} not found. Starting empty.")

    def __save_catalog(self):
        """Persist current stock back to catalog.json."""
        data = {p.name: p.to_dict() for p in self._catalog}
        with open(CATALOG_FILE, "w") as f:
            json.dump(data, f, indent=4)

    def __save_order(self, order: dict):
        try:
            with open(ORDERS_FILE, "r") as f:
                orders = json.load(f)
        except FileNotFoundError:
            orders = []
        orders.append(order)
        with open(ORDERS_FILE, "w") as f:
            json.dump(orders, f, indent=4)

    # --- Internal helpers ---

    def _display_menu(self) -> list[Product]:
        """Show available products sorted by price."""
        available = sorted(
            [p for p in self._catalog if p.is_available],
            key=lambda p: p.price
        )
        print("\n  --- Menu ---")
        for i, product in enumerate(available, start=1):
            print(f"  {i}. {product}")
        return available

    # --- Public interface ---

    def open(self):
        """Run the shop terminal — inherited contract from BaseShop."""
        self.welcome()
        customer = input("\n  Customer name: ").strip()
        cart = ShoppingCart()

        while True:
            available = self._display_menu()
            if not available:
                print("\n  Out of stock today!")
                break

            print(f"\n  Items in cart: {len(cart)}")
            choice = input("  Add item number (or 'done'): ").strip()

            if choice.lower() == "done":
                break

            try:
                idx = int(choice) - 1
                if not (0 <= idx < len(available)):
                    raise IndexError("Invalid selection.")
                product = available[idx]
                qty = int(input(f"  Quantity of {product.name}: ").strip())
                cart.add(product, qty)
                print(f"  Added {qty}x {product.name}!")
            except (ValueError, IndexError) as e:
                print(f"  Error: {e}")

        if len(cart) > 0:
            print(f"\n{cart}")
            order = cart.to_order_dict(customer)
            self.__save_order(order)
            self.__save_catalog()
            print(f"\n  Order saved! Thank you, {customer}!")
        else:
            print("\n  No items ordered. Come back soon!")


# ============================================================
# Entry point
# ============================================================

if __name__ == "__main__":
    shop = ChocoShop(name="Chocolate Fantasy", owner="Rajib")
    shop.open()
