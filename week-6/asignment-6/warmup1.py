#Write a function greet(name, greeting="Hello") that prints a greeting. Call it three different ways:

def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")

# Call the function three different ways
greet("Alice")  # Uses the default greeting
greet("Bob", "Have a great day")  # Uses a custom greeting
greet("Charlie", greeting="Hi")  # Passes the greeting as a keyword argument