# Author : Rajib Deb
# Date : 2-Dec-2023
# Purpose : This will have examples of python functions
# We will create a function that converts an upper case string to lower case.

global my_variable


def show_global_variable_example01():
    my_variable="test01"
    print(my_variable)

def show_global_variable_example02():
    my_variable = "test02"
    print(my_variable)

def upper_to_lower_case(input_str: str):
    lower_case_converted_string = input_str.lower()
    return lower_case_converted_string


def lower_to_upper_case(input_str: str):
    upper_case_converted_string = input_str.upper()
    return upper_case_converted_string


def substring_the_text(input_str: str):
    # TODO : ADD THE APPROPRIATE LOGIC
    pass


def split_the_text(input_str: str):
    # TODO : ADD THE APPROPRIATE LOGIC
    pass


def string_operations(in_str: str, op_type: str = "upper_to_lower"):
    # HOME WORK:
    # ADD OTHER OPERATIONS TYPE AS BELOW
    # 1. GIVEN A STRING, PRINT THE FIRST TWO LETTERS OF THE STRING
    # 2. GIVEN A STRING, SPLIT IT BASED ON A DELIMITER
    # EXAMPLE: RAJIB DEB
    # OUTPUT: RAJIB, DEB
    # HINT: USE split() and then concatenate the split parts with "," in between
    global op_result
    if op_type == "upper_to_lower":
        op_result = upper_to_lower_case(in_str)
    elif op_type == "lower_to_upper":
        op_result = lower_to_upper_case(in_str)

    return op_result


if __name__ == "__main__":
    show_global_variable_example01()
    show_global_variable_example02()
