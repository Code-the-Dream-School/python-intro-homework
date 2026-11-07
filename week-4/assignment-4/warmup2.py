# Warmup 2: Dictionary Operations
student = {
    "name": "Jazmine",
    "grade": 11,
    "subjects": ["Python", "Data", "Web"],
}

# .items() gives (key, value) pairs
for key, value in student.items():
    print(f"{key}: {value}")

# Add a new key
student["graduated"] = False

print()
print(student)
