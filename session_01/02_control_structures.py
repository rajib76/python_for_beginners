# Control Structures: if/elif/else, for, while, break, continue, list comprehension

def determine_adult_or_not(age):
    if age > 18:
        print("You are adult")
    else:
        print("You are not an adult")


def determine_student_grade(marks):
    if marks <= 70:
        grade = "C"
    elif 70 < marks <= 80:    # chained comparison — unique to Python
        grade = "B"
    else:
        grade = "A"
    print(f"You obtained {marks} which gives you a grade {grade}")


def print_items_in_a_list(item_list):
    for item in item_list:
        print(item)


def print_numbers_from_0_to_9():
    for i in range(10):
        print(i)


def get_user_input():
    while True:
        user_input = input("Enter your input (type 'exit' to quit)\n")
        print(user_input)
        if user_input.lower() == "exit":
            break


if __name__ == "__main__":
    # --- if / elif / else ---
    age = int(input("Enter an age: "))
    determine_adult_or_not(age)

    determine_student_grade(60)
    determine_student_grade(75)
    determine_student_grade(95)

    # --- for loop over a list ---
    item_list = ["apple", "banana", "pears"]
    print_items_in_a_list(item_list)

    # --- for loop with range ---
    print_numbers_from_0_to_9()

    # --- Nested loops — iterating a 2D matrix ---
    matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    for row in matrix:
        for number in row:
            print(number)

    # --- while loop with break ---
    get_user_input()

    # --- List comprehension ---
    squared_numbers = [x**2 for x in range(1, 6)]
    print(squared_numbers)   # [1, 4, 9, 16, 25]
