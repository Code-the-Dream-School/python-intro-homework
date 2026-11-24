languages1 = ["Python", "C", "SQL", "JavaScript"]
languages2 = ["Python", "C++", "Java", "SQL"]

set1 = set(languages1)
set2 = set(languages2)

print(set1 | set2)
print(set1 & set2)
print(set1 - set2)