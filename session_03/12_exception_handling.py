# Exception Handling — dealing with errors gracefully
# When an error occurs at runtime Python raises an "exception"
# Without handling it, the program crashes
# With try/except we catch it and decide what to do

# ============================================================
# PART 1 — BASIC try / except
# ============================================================

# Without handling — this would crash:
# result = 10 / 0    # ZeroDivisionError

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")

# Catching the error message with 'as'
try:
    number = int("hello")     # cannot convert "hello" to an integer
except ValueError as e:
    print(f"ValueError: {e}")

# ============================================================
# PART 2 — MULTIPLE except BLOCKS
# ============================================================
# Handle different error types differently
# Always put specific exceptions BEFORE the general Exception

def safe_divide(a, b):
    try:
        result = a / b
        return result
    except ZeroDivisionError:
        print("Error: Cannot divide by zero")
        return None
    except TypeError:
        print("Error: Both arguments must be numbers")
        return None
    except Exception as e:
        print(f"Unexpected error: {e}")
        return None

print(safe_divide(10, 2))     # 5.0
print(safe_divide(10, 0))     # Error message, returns None
print(safe_divide(10, "a"))   # Error message, returns None

# ============================================================
# PART 3 — else BLOCK
# ============================================================
# The else block runs ONLY if NO exception was raised in the try block

try:
    number = int("42")
except ValueError:
    print("That was not a valid number")
else:
    # This only runs if int("42") succeeded
    print(f"Successfully converted: {number}")

# ============================================================
# PART 4 — finally BLOCK
# ============================================================
# The finally block ALWAYS runs — with or without an exception
# Use it to clean up resources (close files, database connections, etc.)

print("\n--- Example with finally ---")
try:
    result = 10 / 2
    print(f"Result: {result}")
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("This always runs regardless of success or failure")

print("\n--- Example with finally when exception occurs ---")
try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero")
finally:
    print("Cleanup code here — always executes")

# ============================================================
# PART 5 — RAISING your own exceptions
# ============================================================
# Use raise to throw an exception intentionally when data is invalid

def set_age(age):
    if not isinstance(age, int):
        raise TypeError(f"Age must be an integer, got {type(age).__name__}")
    if age < 0:
        raise ValueError(f"Age cannot be negative: {age}")
    if age > 150:
        raise ValueError(f"Age {age} is unrealistic")
    return age

try:
    set_age(-5)
except ValueError as e:
    print(f"Invalid age: {e}")

try:
    set_age("thirty")
except TypeError as e:
    print(f"Wrong type: {e}")

try:
    valid_age = set_age(25)
    print(f"Age set successfully: {valid_age}")
except (ValueError, TypeError) as e:
    print(f"Error: {e}")

# ============================================================
# PART 6 — COMMON BUILT-IN EXCEPTIONS
# ============================================================

print("\n--- IndexError ---")
my_list = [1, 2, 3]
try:
    print(my_list[10])
except IndexError as e:
    print(f"IndexError: {e}")

print("\n--- KeyError ---")
my_dict = {"name": "Rajib"}
try:
    print(my_dict["age"])
except KeyError as e:
    print(f"KeyError: {e}")

print("\n--- AttributeError ---")
text = "hello"
try:
    text.non_existent_method()
except AttributeError as e:
    print(f"AttributeError: {e}")

print("\n--- NameError ---")
try:
    print(undefined_variable)
except NameError as e:
    print(f"NameError: {e}")

# ============================================================
# Quick Reference — Common Exceptions
# ============================================================
# ValueError        — wrong value:   int("hello")
# TypeError         — wrong type:    "a" + 1
# ZeroDivisionError — divide by zero: 1 / 0
# FileNotFoundError — missing file:  open("no_file.txt")
# IndexError        — list out of range: [1,2,3][10]
# KeyError          — missing dict key: {}["missing"]
# AttributeError    — bad attribute:  "str".no_method()
# NameError         — undefined var:  print(x) when x not defined
