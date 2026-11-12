# Warmup 2: Input Validation with a While Loop
while True:
    user_input = input("Enter a positive integer: ")
    # Check if input is a valid positive integer using str.isdigit()
    if user_input.isdigit() and int(user_input) > 0:
        val = int(user_input)
        print(f"Got it: {val}")
        break
    else:
        print("That's not a positive integer. Try again.")