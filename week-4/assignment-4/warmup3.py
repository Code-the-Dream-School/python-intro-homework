# Two hardcoded lists of programming languages
list1 = ["Python", "JavaScript", "SQL", "HTML", "CSS"]
list2 = ["Python", "Java", "C++", "SQL", "Ruby"]

# Convert each to a set
set1 = set(list1)
set2 = set(list2)

# 1. The union (all languages from both lists, no duplicates)
print(f"Union: {set1 | set2}")

# 2. The intersection (languages in both lists)
print(f"Intersection: {set1 & set2}")

# 3. The difference (languages only in the first list)
print(f"Difference: {set1 - set2}")