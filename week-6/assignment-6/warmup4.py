# Write a function is_valid_score(score) that returns True if score is an
# integer between 0 and 100 (inclusive), and False otherwise. Then use
# input() to ask the user for a score and convert it to an integer with
# int() before you check it. Call your function inside an if statement and
# print either "Valid score." or "Invalid score — must be between 0 and 100.".

def is_valid_score(score):
    if score >= int(0) and score <= int(100):
        return(True)
    else:
        return(False)

Result = float(input("What is the student's score?: "))
Grade = int(Result)

Validity_Check = is_valid_score(Grade)

if Validity_Check == True:
    print("That is a valid score")
else:
    print("That is a invalid score, please input a score between 0 and 100")