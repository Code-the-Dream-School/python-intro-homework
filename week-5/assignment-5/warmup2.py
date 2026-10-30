number=input("Enter a positive integer: ")
while str.isdigit(number) == False  or int(number) == 0:
    #print(f"Got it {number}")    
    print("That's not a positive integer. Try again.")
    number=input("Enter a positive integer: ")
print(f"Got it {number}")
