# Mini Project - Day Planner

day = input("What day is it? ").lower()
time_of_day = input("What time of day? ").lower()

if day == "monday":
    if time_of_day == "morning":
        print("Suggestion: Go for an early morning walk!")
    elif time_of_day == "afternoon":
        print("Suggestion: Make yourself a yummy snack!")
    elif time_of_day == "evening":
        print("Suggestion: Make yourself a healthy dinner!")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "saturday":
    if time_of_day == "morning":
        print("Suggestion: Make a nice cup of coffee to start your day!")
    elif time_of_day == "afternoon":
        print("Suggestion: Spend your afternoon outdoors!")
    elif time_of_day == "evening":
        print("Suggestion: Have dinner or watch a movie!")
    else:
        print("Sorry, I don't recognize that time of day.")

elif day == "sunday":
    if time_of_day == "morning":
        print("Suggestion: Visit a local farmers market!")
    elif time_of_day == "afternoon":
        print("Suggestion: Visit family or friends!")
    elif time_of_day == "evening":
        print("Suggestion: Movie night!")
    else:
        print("Sorry, I don't recognize that time of day.")

else:
    print("Sorry, I don't recognize that day. Try Monday, Saturday, or Sunday.")