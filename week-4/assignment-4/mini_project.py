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

topScore = -1
name = " "
total = 0
count = 0
listOfSubjects = []
listOfHighScorers = []


for student in students:
    total += student["score"]
    count += 1
    listOfSubjects.append(student["subject"])

    if student["score"] > topScore:
        topScore = student["score"]
        name = student["name"]

for student in students:
    if student["score"] > 75:
        listOfHighScorers.append(student["name"])
print("=====-=================-==============-==============-========")
print(f"Top Scorer: {name} ({topScore})")
print("Class Average:", total/count)
print("Subjects Offered: ", set(listOfSubjects))
print("High Scorers: " ,listOfHighScorers)
