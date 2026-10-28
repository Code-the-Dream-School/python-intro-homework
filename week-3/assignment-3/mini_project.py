dayOfWeek = input("Enter a day of the week: ").lower().strip()
timeOfDay = input("Enter time of day: ").lower().strip()

if dayOfWeek == "monday":
    if timeOfDay == "morning":
        print("Go for a jog!")

    elif timeOfDay == "noon":
        print("Go and eat lunch!")

    elif timeOfDay == "afternoon":
        print("Eat dinner!")

    else:
        print("Not a time of day!")

elif dayOfWeek == "tuesday":
    if timeOfDay == "morning":
        print("Go to the gym!")

    elif timeOfDay == "noon":
        print("Go to work!")

    elif timeOfDay == "afternoon":
        print("Study Study Study!")

    else:
        print("Not a time of day!")

elif dayOfWeek == "friday":
    if timeOfDay == "morning":
        print("Sleep!")

    elif timeOfDay == "noon":
        print("Sleep!")

    elif timeOfDay == "afternoon":
        print("Work!")

    else:
        print("Not a time of day!")

else:
    print("Not a day of the week!")