import csv

def read_data(filename):
    data = []
    with open(filename, newline='') as csvfile:
        reader = csv.reader(csvfile, delimiter=',')
        for row in reader:
            data.append(row)
    return data

def process_data(data):
    header = data[0]
    students = []
    for row in data[1:]:
        student = {}
        for i in range(len(header)):
            student[header[i]] = row[i]
        students.append(student)
    return students

def print_result(students):
    for student in students:
        print("Name: {}  Age: {}  Gender: {}  Score: {}".format(student['name'], student['age'], student['gender'], student['score']))

if __name__ == '__main__':
    filename = '/Users/albertel/Documents/Git/Computer/python/own/try/csv_target.csv'
    data = read_data(filename)
    students = process_data(data)
    print_result(students)