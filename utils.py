import pandas as pd
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
    # id format should be N######## where # is digit
    return (
        len(id) == 9 and
        id.startswith('N') and
        id[1:].isdigit()
    )
    
#check validity of lines
#return a list of valid ones and a count of invalid ones
def analyze(content : str):
    print("**** ANALYZING ***")
    lines = content.splitlines()
    invalid_count = 0
    valid_lines: list[str] = []
    for line in lines: 
        # error list to print later
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
        else:
            valid_lines.append(line)

    if invalid_count == 0:
        print("No errors found!")
    
    return valid_lines, invalid_count


def grade(ans: list, key: list):
    grade = 0

    for a, k in zip(ans, key):
        if a == k:
            grade += 4
        elif a == "":
            grade += 0
        else:
            grade -= 1

    return grade

def report(grades: list):
    # convert to pandas series
    pd_grade = pd.Series(grades)

    mean = pd_grade.mean()
    highest = pd_grade.max()
    lowest = pd_grade.min()
    median = pd_grade.median()
    score_range = highest - lowest

    print(f"Mean (average) score: {mean}")
    print(f"Highest score: {highest}")
    print(f"Lowest score: {lowest}")
    print(f"Range of scores: {score_range}")
    print(f"Median score: {int(median)}")

def write_to_file(ids: list[int], grades: list[int], name: str):
    df = pd.DataFrame({
        "id" : ids,
        "grades": grades
    })
    df.to_csv(name+"_grades.txt", header=None, index=None)