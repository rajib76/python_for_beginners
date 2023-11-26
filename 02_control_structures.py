# Lets say we need to classify a group of people into adult and non-adults
# anyone whose age is more than 18 years is an adult rest are not adult

def determine_adult_or_not(age):
    if age > 18:
        print("You are adult")
    else:
        print("you are not an adult")


def determine_student_grade(marks):
    if marks <= 70:
        grade = "C"
    elif 70 < marks <= 80:
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
        user_input = input("Enter your input\n")
        print(user_input)
        if user_input.lower() == "exit":
            break


if __name__ == "__main__":
    # list comprehension

    squared_numbers = [x**2 for x in range(1,6)]
    print(squared_numbers)
    # matrix = [[1,2,3],[4,5,6],[7,8,9]]
    #
    # for item in matrix:
    #     for number in item:
    #         print(number)

    # get_user_input()
    # # print_numbers_from_0_to_9()
    # # item_list=["apple", "banana", "pears"]
    # # print_items_in_a_list(item_list)
    # # age = input("Enter the age to be checked\n")
    # # determine_adult_or_not(int(age))
    # # marks = 60
    # # determine_student_grade(marks)
    # # marks = 80
    # # determine_student_grade(marks)
    # # marks = 95
    # # determine_student_grade(marks)
