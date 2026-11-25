import os

print(os.getcwd())

if os.path.exists("/Users/melaniesutton/Documents/CodeTheDream/python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")
