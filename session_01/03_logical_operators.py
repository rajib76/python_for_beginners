# Logical Operators: and, or, not
# Used to combine or reverse conditions in if statements

# ---- and ----
# Both conditions must be True for the result to be True

age = 20
has_id = True

if age >= 18 and has_id:
    print("You can enter the club")
else:
    print("You cannot enter the club")

# ---- or ----
# At least one condition must be True for the result to be True

is_student = True
is_senior = False

if is_student or is_senior:
    print("You get a discount")
else:
    print("No discount available")

# ---- not ----
# Reverses a boolean — True becomes False, False becomes True

dark_chocolate = True

if not dark_chocolate:
    print("This is milk chocolate")
else:
    print("This is dark chocolate")

# ---- Combining multiple logical operators ----
# Use parentheses to control the order of evaluation

temperature = 25
is_raining = False
is_weekend = True

if (temperature > 20 and not is_raining) or is_weekend:
    print("Good day to go outside")
else:
    print("Stay home")

# ---- in and not in ----
# Check if a value exists inside a list, string, or dictionary

fruits = ["apple", "banana", "cherry"]

if "banana" in fruits:
    print("banana is in the list")

if "mango" not in fruits:
    print("mango is not in the list")

# Works with strings too
sentence = "Python is awesome"
if "Python" in sentence:
    print("The sentence mentions Python")

# Works with dictionary keys
person = {"name": "Rajib", "city": "California"}
if "name" in person:
    print("name key exists:", person["name"])

# ---- continue ----
# Skips the current iteration and moves to the next one
# compare with break which exits the loop entirely

print("\nSkipping even numbers using continue:")
for number in range(1, 11):
    if number % 2 == 0:
        continue          # skip even numbers, go to next iteration
    print(number)         # only odd numbers reach this line

print("\nCompare: break stops the loop entirely:")
for number in range(1, 11):
    if number == 5:
        break             # stop the loop completely when we hit 5
    print(number)

# ---- Truth table for quick reference ----
# True  and True  = True
# True  and False = False
# False and False = False
# True  or  False = True
# False or  False = False
# not True        = False
# not False       = True
