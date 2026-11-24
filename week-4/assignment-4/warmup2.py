student = {
	"name": "Mowgli",
	"grade": 37,
	"subjects": ["History", "Music", "Art"]
}

for key, value in student.items():
	print(key,value)
student["graduated"] = False
print(student)