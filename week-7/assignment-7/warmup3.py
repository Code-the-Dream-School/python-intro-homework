
import os

print("Current directory:", os.getcwd())

file_path = os.path.join("week-7", "data", "expenses.csv")

if os.path.exists(file_path):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

print("File path:", file_path)
