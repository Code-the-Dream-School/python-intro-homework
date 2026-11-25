with open('/Users/melaniesutton/Documents/CodeTheDream/python-intro-homework/week-7/data/notes.txt','r') as file:
    lines = file.readlines()

    for line in lines:
        print(line.strip())