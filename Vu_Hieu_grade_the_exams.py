import numpy

from utils import open_file, analyze, grade

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