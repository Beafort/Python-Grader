import numpy

def open_file(name):
    try:
        f = open("Data Files/" + name, "r")
        print("Successfully opened " + name)
        return f
    except FileNotFoundError:
        print("Error: File cannot be found")
    except Exception as e:
        print("Unexpected error:", e)
        

def check_student_id(id: str) -> bool: 
    
    if id[0] != 'N' or len(id) != 9:
        return False
    else: 
        return True
    
        
def analyze(content : str):
    print("**** ANALYZING ***")
    lines = content.splitlines()
    invalid_count = 0
    for line in lines: 
        # error list 
        errors: list[str] = []

        data = line.split(",")
        student_id = data[0]

        # validity check
        if not check_student_id(student_id):
            errors.append("N# is invalid")

        if len(data) != 26:
            errors.append("line does not contain exactly 26 values")

        #print errors if any
        if len(errors) != 0:
            invalid_count += 1
            print("Invalid line of data:", end=" ")

            for error in errors:
                print(error, end=" | ")
            print()
            print(line)
            print()
            continue

    if invalid_count == 0:
        print("No errors found! :D")
    
    return lines, invalid_count



def main():
    file_name = input("Enter file name: ")
    f = open_file(file_name)
    content = f.read()

    
    lines, invalid_count = analyze(content)
    




if __name__ == "__main__":
    main()