
day = input("What day is it? ").strip().lower()
time = input("What time of day? ").strip().lower()

if day == "tuesday" and time == "morning":
    print("Suggestion: Practice Python before class.")

elif day == "tuesday" and time == "afternoon":
    print("Suggestion: Go for a walk in the park.")

elif day == "tuesday" and time == "evening":
    print("Suggestion: Read a good book.")

elif day == "thursday" and time == "morning":
    print("Suggestion: Do some yoga.")

elif day == "thursday" and time == "afternoon":
    print("Suggestion: Work on a coding project.")

elif day == "thursday" and time == "evening":
    print("Suggestion: Cook a delicious dinner.")

elif day == "saturday" and time == "morning":
    print("Suggestion: Go hiking in nature.")

elif day == "saturday" and time == "afternoon":
    print("Suggestion: Visit a museum.")

elif day == "saturday" and time == "evening":
    print("Suggestion: Watch a movie.")

else:
    print("Sorry, I don't recognize that day or time. Try Tuesday, Thursday, or Saturday and morning, afternoon, or evening.")

