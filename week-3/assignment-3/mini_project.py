day = input("What day is it? ").lower()
time_of_day = input("What time of day? ").lower()

if day not in ["monday", "tuesday", "wednesday"]:
    print("Oops! I think you made up a new day. Try to enter a day everyone knows, like monday!")

else:
    if time_of_day not in ["morning", "afternoon", "evening"]:
        print("Whoops! That time doesn't exist, silly! Maybe try to enter morning or something...")

    else:
        if day == "monday" and time_of_day == "morning":
            print("Suggestion: Rise and Shine! Time to study Python!")

        elif day == "monday" and time_of_day == "afternoon":
            print("Suggestion: Good afternoon. Get some lunch and some fresh air!")

        elif day == "monday" and time_of_day == "evening":
            print("Suggestion: What are we watching? It's movie night!")

        elif day == "tuesday" and time_of_day == "morning":
            print("Suggestion: Good morning. Breakfast time.")

        elif day == "tuesday" and time_of_day == "afternoon":
            print("Suggestion: Pause, pick up a book, and read a little if you can.")

        elif day == "tuesday" and time_of_day == "evening":
            print("Suggestion: Let's call it an early night tonight!")

        elif day == "wednesday" and time_of_day == "morning":
            print("Suggestion: Early worm gets the hottest cup of coffee!")

        elif day == "wednesday" and time_of_day == "afternoon":
            print("Suggestion: Let's take a break from Python for a bit. See you in a bit!")

        elif day == "wednesday" and time_of_day == "evening":
            print("Suggestion: Maybe a game night?")