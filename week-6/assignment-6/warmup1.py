def greet(name, greeting="Hello"):
    print(f"{greeting}, {name}!")


# 1. Using only a name argument
greet("Alex")

# 2. Using a name and custom greeting
greet("Alex", "Good morning")

# 3. Passing greeting as a keyword argument
greet("Alex", greeting="Hello")