#Demonstrate variable scope with two short examples in one file:
#Define a variable inside a function. Try to access it outside the function and show the NameError — paste the error in a comment, then remove or comment out the line that causes it.
#Show how return solves the problem: return the value from the function and assign it to a variable in the outer scope. Print it to confirm it worked.
def add_numbers(a, b):
    result = a + b #variable defined inside the function
    return result
#print(result) uncommenting this line will cause a NameError because 'result' is not defined.
# Example usage
sum_result = add_numbers(5, 3) #assigning it to a variable in the outer scope
print(sum_result)
