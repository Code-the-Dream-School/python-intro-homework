student = {"name": "Nehemiah", "grade": "Junior", "subjects": ["Math", "English", "Science", "History"]}

for key,value in student.items():
    print(f"{key} : {value}")

student["graduated"] = False

print(student)