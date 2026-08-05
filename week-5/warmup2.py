while True: 
    user_input = input("Enter a positive integer: ")

    if user_input.isdigit() and int(user_input) > 0:
            print(f"Got it: {user_input}")
            break
        #elif int(user_input) <=0:
            #print("That's not a positive integer. Try again.")

    else:
        print("That's not a positive integer. Try again.")





