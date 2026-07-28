#Warmup 2 Dictonary Operations

students = {
    "name": "Khalilah",
    "grade": "A",
    "subjects": {"English, Math, Computer Science"}
}
for student in students.values():
    print(student)

students["graduated"] ="False"

for student in students.values():
    print(student)