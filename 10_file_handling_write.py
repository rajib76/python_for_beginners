def write_file(file_loc, content):
    file = open(file_loc, "w")
    file.write(content)


def append_file(file_loc, content):
    file = open(file_loc, "a")
    file.write(content)


def file_write_using_with(file_loc):
    with open(file_loc, "w") as f:
        f.write("Hello writting file with context manager")


if __name__ == "__main__":
    try:
        content = "learning python is fun"
        file_loc = "./data/my_file_03.txt"
        file_write_using_with(file_loc)
        # append_file(file_loc, "\n" + content)
    except FileNotFoundError as fe:
        print("file is not there")
        print(fe)

    except Exception as e:
        print("Exception occured, no file")
        print(e)
    # try:
    #     content = "hello, I am Rajib and writing hello workld"
    #     write_file("./data1/my_file_01",content)
    #     # append_file("./data/my_file_01", "\n"+content)
    # except FileNotFoundError as fe:
    #     print("Directory does not exist")
    #     print(fe)
    # except Exception as e:
    #     print("Error has happened")
    #     print(e)
