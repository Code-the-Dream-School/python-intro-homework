students = [
    {"name": "Jazmine", "score": 88, "subject": "Python"},
    {"name": "Luis",    "score": 74, "subject": "Data"},
    {"name": "Sara",    "score": 91, "subject": "Python"},
    {"name": "Marcus",  "score": 68, "subject": "Web"},
    {"name": "Priya",   "score": 95, "subject": "Data"},
    {"name": "Devon",   "score": 72, "subject": "Python"},
    {"name": "Mia",     "score": 83, "subject": "Web"},
    {"name": "Eli",     "score": 79, "subject": "Data"},
]

highest_score = 0
top_scorer = ""

for student in students:
	if student["score"] > highest_score:
		highest_score = student["score"]
		top_scorer = student["name"]

print(f"Top scorer: {top_scorer} with {highest_score} points")

total_score = 0

for student in students:
	total_score = total_score + student["score"]

average_score = total_score / 8
print(f"Average score: {average_score}")

subjects = set()

for student in students:
	subjects.add(student["subject"])

above_75 = []

for student in students:
	if student["score"] > 75:
		above_75.append(student)
print("Students who scored above 75:")
for student in above_75:
	print(f"{student["name"]} : {student["score"]}")



