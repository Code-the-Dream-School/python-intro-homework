# What the error message is: 
#  print(f"Hi, {name}") NameError: name 'name' is not defined
# What caused it: not defining the variable name before using it.
# How you fixed it: assigned a value to the variable name

name = input("What is your name? ")

print(f"Hi, {name}")