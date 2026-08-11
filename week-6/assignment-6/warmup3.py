def greet(name):
    message = f"Bonjour, {name}!"
    return message

#print(name)
#      ^^^^
#NameError: name 'name' is not defined

my_name = greet("Khalilah")
print(my_name)