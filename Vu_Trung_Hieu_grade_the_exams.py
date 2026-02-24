import numpy

from utils import open_file, analyze, grade, report, write_to_file


def main():
    answer_key = "B,A,D,D,C,B,D,A,C,C,D,B,A,B,A,C,B,D,A,C,A,A,B,D,D"
    key_list = answer_key.split(",")
    file_name = input("Enter file name: ")
    f = open_file(file_name + ".txt")
    content = f.read()

    
    lines, invalid_count = analyze(content)
    
    
    
    
   
    
    grades = []
    ids = []
    for line in lines:
        data = line.split(",")
        grades.append(grade(data[1:], key_list))
        ids.append(data[0])
    print("*** Report ***")
    print("Number of valid lines:" , len(lines))
    print("Number of invalid lines:" , invalid_count)
    report(grades)
    write_to_file(ids,grades,file_name)


if __name__ == "__main__":
    main()
