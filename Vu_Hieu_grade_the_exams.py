import numpy

from utils import open_file, analyze, grade, report


def main():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    key_list = answer_key.split(",")
    file_name = input("Enter file name: ")
    f = open_file(file_name)
    content = f.read()

    
    lines, invalid_count = analyze(content)
    
    
    
    
   
    
    grades = []
    for line in lines:
        data = line.split(",")
        grades.append(grade(data[1:], answer_key))

    print("*** Report ***")
    print("Number of valid lines:" , len(lines))
    print("Number of invalid lines:" , invalid_count)
    report(grades)
    


if __name__ == "__main__":
    main()