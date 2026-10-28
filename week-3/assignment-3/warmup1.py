score = 89
grade = " "

if score <= 60 - 1:
    grade = "F"

elif score <= 69:
    grade = "D"

elif score <= 79:
    grade = "C"

elif score <= 89:
    grade = "B"

else:
    grade = "A"

print(f"Grade: {grade}")