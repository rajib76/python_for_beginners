import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


def write_file(file_loc, content):
    # "w" mode — overwrites the entire file. Creates the file if it does not exist.
    file = open(file_loc, "w")
    file.write(content)
    file.close()


def append_file(file_loc, content):
    # "a" mode — adds to the end of the file. Creates the file if it does not exist.
    file = open(file_loc, "a")
    file.write(content)
    file.close()


def file_write_using_with(file_loc, content):
    # Context manager — automatically closes the file, even if an error occurs
    with open(file_loc, "w") as f:
        f.write(content)


if __name__ == "__main__":
    file_loc = os.path.join(BASE_DIR, "data", "my_file_03.txt")
    try:
        # Write (creates/overwrites the file)
        file_write_using_with(file_loc, "Hello, writing a file with the context manager.\n")
        print("File written successfully")

        # Append (adds a new line without erasing what is already there)
        append_file(file_loc, "This line was appended.\n")
        print("Line appended successfully")

    except FileNotFoundError as fe:
        print("Directory does not exist:", fe)
    except Exception as e:
        print("An unexpected error occurred:", e)
