with open("week-7/data/notes.txt", "r") as file:
    for number, line in enumerate(file, start=1):
        print(f"{number}: {line.strip()}")