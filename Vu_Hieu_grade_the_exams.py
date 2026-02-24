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
        print("No errors found!")
    
    return lines, invalid_count


def grade(ans: str, key: str):
    ans_list = ans.split(",")
    ans_list = ans_list[1:]
    key_list = key.split(",")

    grade = 0

    for a, k in zip(ans_list, key_list):
        if a == k:
            grade += 4
        elif a == "":
            continue
        else:
            grade -= 1

    return grade


        

def main():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

    file_name = input("Enter file name: ")
    f = open_file(file_name)
    content = f.read()

    
    lines, invalid_count = analyze(content)
    
    if invalid_count != 0:
        return

    grades = []
    for line in lines:
        grades.append(grade(line, answer_key))
    print(grades)
    


if __name__ == "__main__":
    main()