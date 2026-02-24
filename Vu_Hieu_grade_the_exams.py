import numpy

from utils import open_file, analyze, grade, report


def main():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"

    file_name = input("Enter file name: ")
    f = open_file(file_name)
    content = f.read()

    
    lines, invalid_count = analyze(content)
    
    

    grades = []
    for line in lines:
        grades.append(grade(line, answer_key))

    print("*** Report ***")
    print("Number of valid lines:" , len(lines))
    print("Number of invalid lines:" , invalid_count)
    report(grades)
    


if __name__ == "__main__":
    main()