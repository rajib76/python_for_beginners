# Data Structures: List, Tuple, Dictionary, Set, and String operations

# ============================================================
# LISTS — ordered, mutable, allows duplicates
# ============================================================

list_of_appl_product = ["IPAD", "MACBOOK", "IPHONE"]

# Iterate over the list
for product in list_of_appl_product:
    print(product)

# Access a single item by index (zero-based)
print(list_of_appl_product[2])   # IPHONE

# Add a single item
list_of_appl_product.append("APPLE WATCH")

# Add multiple items from another list
fruit_list = ["apple", "banana", "cherry"]
fruit_list.extend(["kiwi", "mango"])
print(fruit_list)

# Negative indexing — count from the end
print(fruit_list[-1])    # mango
print(fruit_list[-2])    # kiwi

# Iterate after appending
for product in list_of_appl_product:
    print(product)

# ============================================================
# TUPLES — ordered, immutable (cannot be changed after creation)
# ============================================================

x_y_coordinate = (1, 2)

print("X coordinate:", x_y_coordinate[0])
print("Y coordinate:", x_y_coordinate[1])

# ============================================================
# DICTIONARIES — key-value pairs, mutable, keys must be unique
# ============================================================

message = {"content": "This is the content I generated", "role": "assistant"}

# Read values
print("Initial content:", message["content"])
print("Role:", message["role"])

# Modify a value
message["content"] = "this is my 2nd output"
print("Modified content:", message["content"])

# Add a new key
message["create_date"] = "12/08/2023"
print("After adding key:", message)

# Remove a key
message.pop("role")
print("After removing role:", message)

# ============================================================
# SETS — unordered, no duplicates
# ============================================================

my_set = {1, 2, 3}
vowels = ('a', 'e', 'i', 'o', 'u')
frozen_vowels = frozenset(vowels)   # immutable version of a set
print(frozen_vowels)

# ============================================================
# STRINGS — sequences of characters, immutable
# ============================================================

greeting = " hello "
name = "rajib"

# Concatenation — both sides must be strings
print(greeting + " " + name)
print(len(greeting))     # 7 — includes the spaces

# Strip whitespace
print(greeting.strip())  # "hello" — removes both ends
print(greeting.rstrip()) # " hello" — removes right end only

# Split — breaks a string into a list on a delimiter
sentence = "rajib|deb|california"
splits = sentence.split("|")
print(splits)            # ['rajib', 'deb', 'california']

# Join — combines a list back into a string
joined_sentence = " ".join(splits)
print(joined_sentence)   # rajib deb california

# Replace — returns a NEW string, original is unchanged
sentence = "I LOVE PYTHON AND I ALSO LOVE JAVA"
sentence_modified = sentence.replace("PYTHON", "JAVA")
print(sentence_modified)  # I LOVE JAVA AND I ALSO LOVE JAVA

# Count occurrences
print(sentence.count("LOVE"))     # 2

# Check ending
print(sentence.endswith("JAVA"))  # True
