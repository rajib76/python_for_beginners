# Functions and Modules — string operation examples
# Demonstrates: function definition, type hints, return values,
# default parameters, and global vs local scope

my_variable = "global"   # module-level (global) variable


def show_global_variable_example01():
    my_variable = "test01"   # local — this is a NEW variable, does NOT change the global
    print(my_variable)       # test01


def show_global_variable_example02():
    my_variable = "test02"   # also local — separate from example01's local variable
    print(my_variable)       # test02


def upper_to_lower_case(input_str: str):
    return input_str.lower()


def lower_to_upper_case(input_str: str):
    return input_str.upper()


def string_operations(in_str: str, op_type: str = "upper_to_lower"):
    # op_type has a default value — caller does not have to provide it
    if op_type == "upper_to_lower":
        return upper_to_lower_case(in_str)
    elif op_type == "lower_to_upper":
        return lower_to_upper_case(in_str)


if __name__ == "__main__":
    # --- Global vs local scope ---
    print("global before calls:", my_variable)   # global
    show_global_variable_example01()             # test01
    show_global_variable_example02()             # test02
    print("global after calls:", my_variable)    # still "global" — unchanged

    # --- String operations using default parameter ---
    result = string_operations("HELLO WORLD")
    print(result)   # hello world  (default op_type = "upper_to_lower")

    # --- String operations with explicit parameter ---
    result = string_operations("hello world", op_type="lower_to_upper")
    print(result)   # HELLO WORLD
