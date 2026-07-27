# Mini Project - Day Planner

day = input("What day is it? ").strip().lower()
time_of_day = input("What time of day? ").strip().lower()

if day == "monday":
    if time_of_day == "morning":
        print("Suggestion: Go for an early morning walk!")
    elif time_of_day == "afternoon":
        print("Suggestion: Practice Python coding!")
    elif time_of_day == "evening":
        print("Suggestion: Make a healthy dinner!")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "tuesday":
    if time_of_day == "morning":
        print("Suggestion: Start your day with a good breakfast!")
    elif time_of_day == "afternoon":
        print("Suggestion: Take a break and enjoy some fresh air!")
    elif time_of_day == "evening":
        print("Suggestion: Read a book and relax!")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "wednesday":
    if time_of_day == "morning":
        print("Suggestion: Plan your goals for the day!")
    elif time_of_day == "afternoon":
        print("Suggestion: Finish an important task!")
    elif time_of_day == "evening":
        print("Suggestion: Enjoy a relaxing evening!")
    else:
        print("Sorry, I don't recognize that time of day.")

else:
    print("Sorry, I don't recognize that day. Try Monday, Tuesday, or Wednesday.")