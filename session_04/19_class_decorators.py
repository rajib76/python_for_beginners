# Class Decorators: @property, @classmethod, @staticmethod
#
# These three decorators change how a method behaves:
# @property    — access a method AS IF it were a plain attribute (no parentheses)
# @classmethod — receives the CLASS itself (cls) instead of the instance (self)
# @staticmethod — receives neither class nor instance — just a plain utility function

# ============================================================
# PART 1 — @property
# ============================================================
# Lets you add logic to attribute access while keeping clean dot-notation syntax
# Also lets you VALIDATE data when someone sets a value

class Circle:
    def __init__(self, radius):
        self._radius = radius     # _radius: single underscore signals "internal use"

    # @property — getter
    # Accessed as circle.radius (no parentheses)
    @property
    def radius(self):
        return self._radius

    # @<name>.setter — runs when you do: circle.radius = value
    @radius.setter
    def radius(self, value):
        if value < 0:
            raise ValueError("Radius cannot be negative")
        self._radius = value

    # Read-only computed property — no setter, so it cannot be assigned
    @property
    def area(self):
        import math
        return math.pi * self._radius ** 2

    @property
    def circumference(self):
        import math
        return 2 * math.pi * self._radius

    def __str__(self):
        return f"Circle(radius={self._radius:.2f})"


c = Circle(5)
print(c.radius)           # 5         — looks like an attribute, calls the getter
print(c.area)             # 78.539... — computed on the fly, no parentheses
print(c.circumference)    # 31.415...

c.radius = 10             # triggers the setter, validates the value
print(c.radius)           # 10

try:
    c.radius = -3         # setter raises ValueError
except ValueError as e:
    print(e)

# ============================================================
# PART 2 — @classmethod
# ============================================================
# Receives the CLASS (cls) as the first argument, NOT the instance
# Primary use: alternative constructors — create an object from different input formats

class Temperature:
    def __init__(self, celsius):
        self.celsius = celsius

    # Alternative constructor — build from Fahrenheit
    @classmethod
    def from_fahrenheit(cls, fahrenheit):
        celsius = (fahrenheit - 32) * 5 / 9
        return cls(celsius)         # cls(...) is the same as Temperature(...)

    # Alternative constructor — build from Kelvin
    @classmethod
    def from_kelvin(cls, kelvin):
        celsius = kelvin - 273.15
        return cls(celsius)

    def __str__(self):
        return f"{self.celsius:.2f}°C"


# Standard constructor
t1 = Temperature(100)
print(t1)                               # 100.00°C

# Alternative constructors — created from different input
t2 = Temperature.from_fahrenheit(212)
print(t2)                               # 100.00°C — same thing

t3 = Temperature.from_kelvin(373.15)
print(t3)                               # 100.00°C — same thing

# ============================================================
# PART 3 — @staticmethod
# ============================================================
# Receives neither self nor cls
# A utility function that belongs inside this class logically
# but does NOT need any class or instance data

class MathHelper:
    @staticmethod
    def is_even(number):
        return number % 2 == 0

    @staticmethod
    def is_prime(number):
        if number < 2:
            return False
        for i in range(2, int(number ** 0.5) + 1):
            if number % i == 0:
                return False
        return True

    @staticmethod
    def clamp(value, minimum, maximum):
        """Clamp a value to stay within [minimum, maximum]."""
        return max(minimum, min(value, maximum))


# Called on the class directly — no instance needed
print(MathHelper.is_even(4))            # True
print(MathHelper.is_prime(17))          # True
print(MathHelper.clamp(150, 0, 100))    # 100

# ============================================================
# Summary
# ============================================================
# @property      → obj.attribute  (getter/setter with validation)
# @classmethod   → ClassName.method(...)  (alternative constructors, factory methods)
# @staticmethod  → ClassName.method(...)  (utility functions that need no self/cls)
