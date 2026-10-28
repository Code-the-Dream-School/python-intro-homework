age = int(input("Enter your age: "))

if age < 0:
    print("Next time use a real number...")

elif age > 0 and age < 12:
    catagory = "child"

elif age > 13 and age < 17:
    catagory = "teen"

elif age > 18 and age < 64:
    catagory = "adult"

else:
    catagory = "senior"

print(f"You are a: {catagory}")