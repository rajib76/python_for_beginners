import json
import os

# JSON — JavaScript Object Notation
# A universal text format for storing and exchanging structured data
# Python dicts/lists map directly to JSON objects/arrays
# Used everywhere: REST APIs, config files, data storage

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# ============================================================
# PART 1 — WRITING a Python dict to a JSON file
# ============================================================

student_data = {
    "name": "Rajib",
    "age": 30,
    "courses": ["Python", "Data Science", "Machine Learning"],
    "address": {
        "city": "California",
        "zip": "90001"
    },
    "active": True
}

write_path = os.path.join(BASE_DIR, "data", "student.json")

with open(write_path, "w") as f:
    json.dump(student_data, f, indent=4)   # indent=4 makes it human-readable

print("Data written to student.json")

# ============================================================
# PART 2 — READING a JSON file back into Python
# ============================================================

with open(write_path, "r") as f:
    loaded_data = json.load(f)

print(type(loaded_data))                       # <class 'dict'>
print(loaded_data["name"])                     # Rajib
print(loaded_data["courses"])                  # ['Python', 'Data Science', ...]
print(loaded_data["courses"][0])               # Python
print(loaded_data["address"]["city"])          # California

# Iterate the courses list inside the dict
for course in loaded_data["courses"]:
    print(f"  - {course}")

# ============================================================
# PART 3 — JSON as a STRING (no file involved)
# ============================================================

# json.dumps() — Python object → JSON string
json_string = json.dumps(student_data, indent=4)
print(json_string)
print(type(json_string))    # <class 'str'>

# json.loads() — JSON string → Python object
parsed = json.loads(json_string)
print(parsed["name"])       # Rajib
print(type(parsed))         # <class 'dict'>

# ============================================================
# PART 4 — Writing a LIST of dicts to JSON (common pattern)
# ============================================================

employees = [
    {"id": 1, "name": "Alice",   "department": "Engineering"},
    {"id": 2, "name": "Bob",     "department": "Marketing"},
    {"id": 3, "name": "Charlie", "department": "Engineering"},
]

employees_path = os.path.join(BASE_DIR, "data", "employees.json")

with open(employees_path, "w") as f:
    json.dump(employees, f, indent=4)

# Read it back
with open(employees_path, "r") as f:
    loaded_employees = json.load(f)

for emp in loaded_employees:
    print(f"ID: {emp['id']} | {emp['name']} | {emp['department']}")

# ============================================================
# Why JSON matters for Python developers
# ============================================================
# When you call any web API (weather, ChatGPT, payment, maps etc.)
# the response arrives as a JSON string.
# json.loads() converts it into a Python dict you can work with.
#
# json.dumps()  — Python → JSON string    (serialize)
# json.loads()  — JSON string → Python    (deserialize)
# json.dump()   — Python → JSON file      (write file)
# json.load()   — JSON file → Python      (read file)
