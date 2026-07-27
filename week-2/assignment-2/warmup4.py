# Deliberate bug: using a variable that doesn't exist 
# print(total)

# Error message:
# NameError: name 'total' is not defined
#
# What caused it:
# I tried to print a variable named 'total' before creating it.
#
# How I fixed it:
# I defined the variable (total = 10), and then printed it.

total = 10
print(total)
