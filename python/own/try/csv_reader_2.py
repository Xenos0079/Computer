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
    print('header: ', header)


if __name__ == '__main__':
    filename = '/Users/albertel/Documents/Git/Computer/python/own/try/csv_target_2.csv'
    data = read_data(filename)
    schedule = process_data(data)
    #print_result(students)