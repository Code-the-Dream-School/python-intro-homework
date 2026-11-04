# Hardcoded student dictionary
student = {
    "name": "Leopold",
    "grade": "Sophomore",
    "subjects": ["Python", "Data Analytics", "Cloud Computing"]
}

# 1. Print each key-value pair using .items() in a for loop
for key, value in student.items():
    print(f"{key}: {value}")

# 2. Add a new key "graduated" with the value False
student["graduated"] = False

# 3. Print the updated dictionary
print("\nUpdated Dictionary:")
print(student)