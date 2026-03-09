# Advanced operations on Dictionaries and Lists
# Covers: dict methods, enumerate, zip, sorting, nested structures, dict.get()

# ============================================================
# PART 1 — DICTIONARY METHODS
# ============================================================

student = {
    "name": "Rajib",
    "age": 30,
    "city": "California",
    "grade": "A"
}

# .keys() — returns all keys
print("Keys:", list(student.keys()))
for key in student.keys():
    print(key)

# .values() — returns all values
print("Values:", list(student.values()))
for value in student.values():
    print(value)

# .items() — returns all key-value pairs as tuples
# This is the most commonly used in for loops
print("Items:", list(student.items()))
for key, value in student.items():
    print(f"{key} = {value}")

# .get() — safely read a value without crashing if the key doesn't exist
print(student.get("name"))           # Rajib
print(student.get("phone"))          # None — key missing, no error raised
print(student.get("phone", "N/A"))   # N/A — provide a default value

# Compare: student["phone"] would raise a KeyError — crash!
# student.get("phone") is the safe alternative

# ============================================================
# PART 2 — enumerate()
# ============================================================
# Gives you BOTH the index AND the value while looping
# Avoids needing range(len(list))

fruits = ["apple", "banana", "cherry"]

# Without enumerate — old style
for i in range(len(fruits)):
    print(i, fruits[i])

# With enumerate — cleaner, more Pythonic
for index, fruit in enumerate(fruits):
    print(f"{index}: {fruit}")

# Start counting from 1 instead of 0
for index, fruit in enumerate(fruits, start=1):
    print(f"{index}. {fruit}")

# ============================================================
# PART 3 — zip()
# ============================================================
# Pairs up elements from two (or more) lists by position

names  = ["Alice", "Bob", "Charlie"]
scores = [85, 92, 78]
grades = ["B", "A", "C"]

# Iterate over two lists at the same time
for name, score in zip(names, scores):
    print(f"{name}: {score}")

# Iterate over three lists at once
for name, score, grade in zip(names, scores, grades):
    print(f"{name} scored {score} — Grade {grade}")

# Build a dictionary from two lists
student_scores = dict(zip(names, scores))
print(student_scores)
# {'Alice': 85, 'Bob': 92, 'Charlie': 78}

# ============================================================
# PART 4 — SORTING
# ============================================================

numbers = [3, 1, 4, 1, 5, 9, 2, 6]

# .sort() — modifies the list IN PLACE, returns None
numbers.sort()
print(numbers)               # [1, 1, 2, 3, 4, 5, 6, 9]

numbers.sort(reverse=True)
print(numbers)               # [9, 6, 5, 4, 3, 2, 1, 1]

# sorted() — returns a NEW sorted list, original is UNCHANGED
original = [3, 1, 4, 1, 5]
sorted_list = sorted(original)
print(original)              # [3, 1, 4, 1, 5] — unchanged
print(sorted_list)           # [1, 1, 3, 4, 5]

# Sort strings alphabetically
words = ["banana", "apple", "cherry", "date"]
words.sort()
print(words)                 # ['apple', 'banana', 'cherry', 'date']

# Sort by a custom key (sort by string length)
words_by_length = sorted(words, key=len)
print(words_by_length)       # ['date', 'apple', 'banana', 'cherry']

# ============================================================
# PART 5 — NESTED DATA STRUCTURES
# ============================================================
# Lists of dictionaries — the most common structure in real applications
# (API responses, database rows, CSV data all look like this)

employees = [
    {"name": "Alice",   "department": "Engineering", "salary": 90000},
    {"name": "Bob",     "department": "Marketing",   "salary": 75000},
    {"name": "Charlie", "department": "Engineering", "salary": 95000},
    {"name": "Diana",   "department": "Marketing",   "salary": 80000},
]

# Access a specific field
print(employees[0]["name"])       # Alice

# Iterate and display
for employee in employees:
    print(f"{employee['name']} — {employee['department']} — ${employee['salary']}")

# Filter: only Engineering employees
engineers = [e for e in employees if e["department"] == "Engineering"]
print(engineers)

# Sort employees by salary
by_salary = sorted(employees, key=lambda e: e["salary"])
for emp in by_salary:
    print(f"{emp['name']}: ${emp['salary']}")

# Dictionary of lists
course_students = {
    "Python":      ["Alice", "Bob"],
    "Data Science": ["Charlie", "Diana", "Eve"],
    "Machine Learning": ["Alice", "Charlie"],
}

for course, student_list in course_students.items():
    print(f"{course}: {', '.join(student_list)}")
