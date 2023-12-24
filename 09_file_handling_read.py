def read_file(file_loc):
    file = open(file_loc, "r")
    content = file.read()
    return content


def read_lines_from_file_in_a_list(file_loc):
    file = open(file_loc, "r")
    lines = file.readlines()
    return lines


def read_line_from_file(file_loc):
    file = open(file_loc, "r")
    count = 0
    while True:
        line = file.readline()  # Read one line at a time
        if not line:
            break  # Exit the loop if the end of the file is reached
        else:
            count = count + 1
            print(f"reading line... {count}")
            print(line.strip())  # Process the line (strip removes trailing newline characters)
    return "done"

def file_read_using_with(file_loc):
    with open(file_loc, "r") as f:
        content = f.read()

    return content

if __name__ == "__main__":
    file_loc = "./data/my_file.txt"
    # content = read_file(file_loc)
    # print(content)

    # status = read_line_from_file(file_loc)
    # print(status)
    # #
    lines = read_lines_from_file_in_a_list(file_loc)
    print(lines)
    for line in lines:
        print(line)
