# Lists
list_of_appl_product = ["IPAD","MACBOOK","IPHONE"]

# Iterate over the list and print
for product in list_of_appl_product:
    print(product)

# Print one item from the list
print(list_of_appl_product[2])

# Add an item
list_of_appl_product.append("kindle")

# Print the items
for product in list_of_appl_product:
    print(product)

# Tuples

x_y_coordinate = (1,2)

print("X coordinate :", x_y_coordinate[0])
print("Y coordinate :", x_y_coordinate[1])

# Dictionary

message= {"content":"This the the content I generated", "role":"assistant"}

print("Initial message content")
print(message["content"])
print(message["role"])

# Modify the value of content
message["content"] = "this is my 2nd output"

print("Modified message content")
print(message["content"])
print(message["role"])

# Extending a list

fruit_list = ["apple", "banana", "cherry"]
# fruit_list.extend(["kiwi","mango"])

print(fruit_list[-2])


# Dictionary operations

message= {"content":"This the the content I generated", "role":"assistant"}

message["create_date"]="12/08/2023"
print(message)

message["content"] = "New content"
print(message)

# Remove a key
message.pop("role")

print(message)

# Sets
my_set = {1,2,3}
vowels = ('a', 'e', 'i', 'o', 'u')
fSet = frozenset(vowels)
print(fSet)

greeting = " hello "
name = "rajib"

# Concatenate two strings
# Remember you cannot concatenate string and non strings
print(greeting+" "+name)
print(len(greeting))

print(greeting)
print(greeting.rstrip())

# Split
sentence = "rajib|deb|california"
splits = sentence.split("|")
print(splits)

# Join
joined_sentence = " ".join(splits)
print(joined_sentence)

# String Functions
sentence = "I LOVE PYTHON AND I ALSO LOVE JAVA"

# Replace Python with Java
sentece_modified = sentence.replace("PYTHON", "JAVA")
# Count how many times java
print(sentence.count("LOVE"))

# Check if the sentence starts with JAVA
ends_with = sentence.endswith("JAVA")
print(ends_with)













