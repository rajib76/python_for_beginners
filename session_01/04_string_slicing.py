# String Slicing and Indexing
# A string is a sequence of characters — each character has a position (index)

name = "Python"

# Positive index:  P  y  t  h  o  n
#                  0  1  2  3  4  5
# Negative index: -6 -5 -4 -3 -2 -1

# ---- Accessing a single character ----
print(name[0])       # P  — first character
print(name[5])       # n  — last character by positive index
print(name[-1])      # n  — last character by negative index
print(name[-2])      # o  — second to last

# ---- Slicing: string[start:stop] ----
# start is INCLUSIVE, stop is EXCLUSIVE
print(name[0:3])     # Pyt   — index 0, 1, 2
print(name[2:5])     # tho   — index 2, 3, 4
print(name[:3])      # Pyt   — from beginning up to (not including) index 3
print(name[3:])      # hon   — from index 3 to the end
print(name[:])       # Python — the entire string

# ---- Slicing with a step: string[start:stop:step] ----
print(name[::2])     # Pto   — every 2nd character
print(name[::1])     # Python — step of 1 (default)
print(name[::-1])    # nohtyP — step of -1 reverses the string

# ---- Practical examples ----

# Get username from an email address
email = "rajib@example.com"
at_position = email.index("@")          # find where @ is
username = email[:at_position]           # everything before @
domain = email[at_position + 1:]         # everything after @
print(f"Username: {username}")           # rajib
print(f"Domain:   {domain}")             # example.com

# Get the file extension from a filename
filename = "report_2024.pdf"
dot_position = filename.index(".")
extension = filename[dot_position + 1:]  # pdf
file_base = filename[:dot_position]      # report_2024
print(f"Base name: {file_base}")
print(f"Extension: {extension}")

# Check first and last characters
product_code = "A-10234-Z"
print(f"Starts with: {product_code[0]}")   # A
print(f"Ends with:   {product_code[-1]}")  # Z

# Reverse a string to check if it is a palindrome
word = "racecar"
reversed_word = word[::-1]
if word == reversed_word:
    print(f"{word} is a palindrome")
else:
    print(f"{word} is not a palindrome")

# ---- len() ----
# Get the total number of characters in a string
print(f"Length of '{name}': {len(name)}")  # 6

# Last valid index is always len(string) - 1
print(name[len(name) - 1])   # n — same as name[-1]
