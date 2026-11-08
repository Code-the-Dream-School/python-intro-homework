student = {
    "name": "Valentina",
    "grade": 90,
    "subjects": ["Python", "Mathematics", "English"]
}

for key, value in student.items():
    print(key, value)

student["graduated"] = False
print(student)
