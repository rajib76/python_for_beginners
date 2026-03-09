# *args and **kwargs — Variable-length function arguments
# Used when you don't know in advance how many arguments a function will receive

# ---- *args — any number of positional arguments ----
# Python packs them into a TUPLE inside the function

def add_all_numbers(*args):
    print(f"args received: {args}")   # it's a tuple
    total = 0
    for number in args:
        total = total + number
    return total

print(add_all_numbers(1, 2))            # 3
print(add_all_numbers(1, 2, 3))         # 6
print(add_all_numbers(1, 2, 3, 4, 5))  # 15
print(add_all_numbers())                # 0 — works with no arguments too

# ---- **kwargs — any number of keyword arguments ----
# Python packs them into a DICTIONARY inside the function

def print_person_details(**kwargs):
    print(f"kwargs received: {kwargs}")   # it's a dict
    for key, value in kwargs.items():
        print(f"  {key}: {value}")

print_person_details(name="Rajib", age=30, city="California")
# name: Rajib
# age: 30
# city: California

print_person_details(product="Chocolate", price=4.99, in_stock=True)

# ---- Mixing regular params, *args, and **kwargs ----
# Order MUST always be: regular params, then *args, then **kwargs

def describe_order(restaurant, *items, **options):
    print(f"Restaurant: {restaurant}")
    print("Items ordered:")
    for item in items:
        print(f"  - {item}")
    if options:
        print("Special options:")
        for option, value in options.items():
            print(f"  {option}: {value}")

describe_order(
    "Pizza Palace",
    "Margherita", "Coke", "Garlic Bread",
    delivery=True,
    extra_cheese=True
)

# ---- Unpacking with * and ** when CALLING a function ----
# You can also unpack a list/tuple with * or a dict with ** when calling

def greet(first_name, last_name, city):
    print(f"Hello {first_name} {last_name} from {city}!")

person_list = ["Rajib", "Deb", "California"]
person_dict = {"first_name": "Rajib", "last_name": "Deb", "city": "California"}

greet(*person_list)     # unpacks list into positional args
greet(**person_dict)    # unpacks dict into keyword args
