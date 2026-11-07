# Warmup 3: Set Operations
list_a = ["Python", "JavaScript", "Java", "Go", "Ruby"]
list_b = ["Python", "C++", "Go", "Rust", "Swift"]

set_a = set(list_a)
set_b = set(list_b)

print("Union:        ", set_a | set_b)   # everything, no duplicates
print("Intersection: ", set_a & set_b)   # in both
print("Difference:   ", set_a - set_b)   # only in the first
