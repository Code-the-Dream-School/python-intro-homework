import csv

with open('/Users/melaniesutton/Documents/CodeTheDream/python-intro-homework/week-7/data/students.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)