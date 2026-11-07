# Mini-Project: Student Roster Analyzer

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

# Track everything in a single pass through the list
top_score = students[0]["score"]   # start with the first student as the "best so far"
top_name = students[0]["name"]
total = 0
subjects = set()                   # a set automatically ignores duplicates
high_scorers = []

for student in students:
    # 1. Top scorer: if this score beats the best so far, update BOTH values
    if student["score"] > top_score:
        top_score = student["score"]
        top_name = student["name"]

    # 2. Running total for the average
    total += student["score"]

    # 3. Collect unique subjects
    subjects.add(student["subject"])

    # 4. High scorers: above 75
    if student["score"] > 75:
        high_scorers.append(student["name"])

average = total / len(students)

print(f"Top scorer:       {top_name} ({top_score})")
print(f"Class average:    {average}")
print(f"Subjects offered: {subjects}")
print(f"High scorers:     {high_scorers}")
