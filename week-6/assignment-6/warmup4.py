def is_valid_score(score):
    if score >= 0 and score <=100:
        return True
    else:
        return False

score_input = int(input("Enter a score: "))

score_result = is_valid_score(score_input)

if score_result == True:

    print("Valid score.")

else:
    print("Invalid score \u2014 must be between 0 and 100.")