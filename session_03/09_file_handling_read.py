import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def read_file(file_loc):
    # Method 1: read entire file as a single string
    file = open(file_loc, "r")
    content = file.read()
    file.close()
    return content


def read_lines_from_file_in_a_list(file_loc):
    # Method 2: read all lines at once into a list
    file = open(file_loc, "r")
    lines = file.readlines()
    file.close()
    return lines


def read_line_from_file(file_loc):
    # Method 3: read one line at a time — memory-efficient for large files
    file = open(file_loc, "r")
    count = 0
    while True:
        line = file.readline()
        if not line:
            break   # readline() returns "" at end of file
        count = count + 1
        print(f"reading line... {count}")
        print(line.strip())   # strip() removes the trailing newline character
    file.close()
    return "done"


def file_read_using_with(file_loc):
    # Method 4: context manager — automatically closes the file, even on error
    with open(file_loc, "r") as f:
        content = f.read()
    return content


if __name__ == "__main__":
    file_loc = os.path.join(BASE_DIR, "data", "my_file.txt")

    # Method 1: entire file as one string
    print("--- read() ---")
    content = read_file(file_loc)
    print(content)

    # Method 2: all lines into a list
    print("--- readlines() ---")
    lines = read_lines_from_file_in_a_list(file_loc)
    for line in lines:
        print(line.strip())

    # Method 3: one line at a time
    print("--- readline() loop ---")
    status = read_line_from_file(file_loc)
    print(status)

    # Method 4: with statement (recommended)
    print("--- with open() ---")
    content = file_read_using_with(file_loc)
    print(content)
