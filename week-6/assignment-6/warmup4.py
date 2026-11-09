def is_valid_score(score):
    while True:
        if score >= range(0,101):
            score = True
        else:
            score = False
user_score = int(input("Enter a score: "))      
if user_score >= range(0, 101):
        print("Valid score")
else:
        print("Invalid score.")
        