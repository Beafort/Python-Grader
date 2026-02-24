

import numpy

def open_file(name):
    try:
        f = open(name, "r")
        print("Successfully opened " + name)
        return f
    except FileNotFoundError:
        print("Error: File cannot be found")
    except Exception as e:
        print("Unexpected error:", e)

def main():
    file_name = input("Enter file name: ")
    f = open_file(file_name)
    content = f.read()

    print(content);


if __name__ == "__main__":
    main()