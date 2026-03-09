# Chocolate Shop — Variables and Data Types
# We run a shop that sells chocolates. Each attribute below is a different data type.

name = "Chocolate Fantasy"
number_of_chocolates_in_stock = 10
color = "RED"
shape = "round"
unit_price = 4.978656
discount = 0.50
dark_chocolate = True

# --- 1. Printing variable values and their types ---
print("The name of the chocolate is", name)
print("The datatype of name is", type(name))

print("The type of the chocolate is", dark_chocolate)
print("The datatype of dark_chocolate is", type(dark_chocolate))

print("The discount on the chocolate is", discount)
print("The datatype of discount is", type(discount))

print("The number of chocolates are", number_of_chocolates_in_stock)
print("The datatype of number is", type(number_of_chocolates_in_stock))

# --- 2. f-strings (Python 3.6+) ---
# Prefix a string with f and embed variables directly inside {}
print(f"The name of the chocolate is {name}")

# Older style using .format() — still valid but f-strings are preferred
print("The name of the chocolate is {name}".format(name=name))

# --- 3. Format specifiers ---
# {value:.2f} — : starts the specifier, f = float, .2 = 2 decimal places
print(f"The unit price of the chocolate is {unit_price:.3f}")
print(f"The unit price rounded to 2 places is {unit_price:.2f}")

# --- 4. Boolean variables ---
print(f"Is it dark chocolate? {dark_chocolate}")

if dark_chocolate:
    print("The chocolate is dark")
else:
    print("The chocolate is not dark")

# --- 5. Arithmetic with variables ---
price = unit_price * 3
print(f"Price of 3 chocolates is {price:.2f}")

# Float division vs integer (floor) division
no_of_chocolates_float = 11 / unit_price    # returns float — you can't buy 0.46 of a chocolate
no_of_chocolates_int = 11 // unit_price     # floor division — rounds down to whole number
print("With float division:", no_of_chocolates_float)
print("With floor division (how many you can actually buy):", no_of_chocolates_int)

# --- 6. Checking the data type of each variable ---
print("datatype of name is", type(name))
print("datatype of color is", type(color))
print("datatype of shape is", type(shape))
print("datatype of unit_price is", type(unit_price))
print("datatype of discount is", type(discount))
print("datatype of dark_chocolate is", type(dark_chocolate))

# --- 7. Type conversion ---
# Implicit: Python auto-promotes int to float when they are mixed in an expression
num_int = 5
num_float = 2.5
result = num_int + num_float
print(result)           # 7.5
print(type(result))     # <class 'float'>

# Explicit: force-convert a type manually
# int() truncates — it does NOT round
num_float = 3.75
num_int = int(num_float)
print(num_int)          # 3, not 4

# --- 8. input() — user input is ALWAYS returned as a string ---
# Even if the user types 5, you get the string "5", not the integer 5
# You must explicitly convert with int() before doing arithmetic

def add_two_numbers():
    first_number = input("Enter the first number\n")
    print("first number entered is", first_number)
    print("its type is", type(first_number))

    second_number = input("Enter the second number\n")
    print("second number entered is", second_number)
    print("its type is", type(second_number))

    sum_of_number = int(first_number) + int(second_number)
    print("The result is", sum_of_number)


if __name__ == "__main__":
    add_two_numbers()
