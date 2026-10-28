list1 = ["C++", "C", "Ruby", "Javascript"]
list2 = ["Python", "C++", "Java", "Javascript"]

set1 = set(list1)
set2 = set(list2)

print(set1.union(set2))
print(set1.intersection(set2))
print(set1.difference(set2))