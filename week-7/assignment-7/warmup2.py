import csv

with open("week-7/data/students.csv", "r") as file:
    students = csv.DictReader(file)

    for student in students:
        print(student["name"], student["score"])