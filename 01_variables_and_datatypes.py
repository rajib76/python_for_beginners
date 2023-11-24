# Let us learn this by taking an examples
# Lets say we have setup a shop to sell chocolates
# To sell the chocolates, we need to capture different
# attributes of the chocolate like
# Name - The name of the chocolate
# Color - Our chocolate comes in red, green and blue
# Shape - Our chocolate shape is either square or cube
# unit_price - Price of each chocolate
# Discount- The discount that we will provide to a customer
# Dark or not - The type of the chocolate whether it is DARK or NOT

name = "Chocolate Fantasy"
number_of_chocolates_in_stock = 10
color = "RED"
shape = "round"
unit_price = 4.978656
discount = 0.50
dark_chocolate = True

# 1. Printing the variable values
# print("The name of the chocolate is ", name)
# print("The datatype of chocolate is", type(name))
#
# print("The type of the chocolate is ", dark_chocolate)
# print("The datatype of chocolate type is", type(dark_chocolate))
#
# print("The discount on the chocolate is ", discount)
# print("The datatype of chocolate discount is", type(discount))
#
# print("The number of chocolates are ", number_of_chocolates_in_stock)
# print("The datatype of number is", type(number_of_chocolates_in_stock))


# An f-string is a feature introduced in Python 3.6 that allows to embed
# expressions inside string literals using curly braces
# F-strings are prefixed with an 'f' character before the opening quotation mark
# and allow you to create strings with dynamic content by evaluating
# expressions and variables within the string.

# 2. Use of fsting

# print(f"The name of the chocolate is {name}")
# print("The name of the chocolate is {name}".format(name=name))
#
# 3. Use of format splitter
# using a format specifier
# : inidcates the start of the specifier
# f: Format as a floating-point number (a number with a decimal point).
# .2: Display exactly 2 decimal places

# print(f"The unit_price of the chocolate is {unit_price:.3f}")
#
# 4. Boolean variable
# Boolean
# print(f"The type of chocolate is {dark_chocolate}")
#
# if dark_chocolate:
#     print("The chocolate is dark")
# else:
#     print("The chocolate is not dark")

# I want to by 3 choclates, what will be the price of three chocolates

# 5. Operation with variables
# price = unit_price*3
# print(f"Price of 3 chocolates is {price:.2f}")

# How many chocolates can I get with 11 dollars
# float divison vs integer division
# no_of_chocolates = 11/unit_price
# no_of_chocolates = 11//unit_price
# print("number of chocolates that you can get with 11 dollars", no_of_chocolates)

# 6. Variable datatypes
# Lets print the data type of each variables

# print("datatype of name is " ,type(name))
# print("datatype of color is " ,type(color))
# print("datatype of shape is " ,type(shape))
# print("datatype of unit_price is " ,type(unit_price))
# print("datatype of discount is " ,type(discount))
# print("datatype of dark_chocolate is " ,type(dark_chocolate))
#
#
# # 7. Data type conversion
# # Lets now talk about type conversion
# # Implicit
#
# num_int = 5
# num_float = 2.5
#
# result = num_int + num_float  # Implicit conversion of num_int to float
# print(result)
# print(type(result))
#
# num_float = 3.75
# num_int = int(num_float)  # Explicitly converting a float to an integer
#
# print(num_int)


first_number = input("Enter the first number\n")
print("first number entered is ", first_number)

second_number = input("Enter the second number\n")
print("second number entered is ", second_number)

print(type(first_number))
print(type(second_number))

sum_of_number = int(first_number) + int(second_number)

print("The result is ",sum_of_number )






