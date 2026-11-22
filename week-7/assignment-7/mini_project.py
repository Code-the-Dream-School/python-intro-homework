
import csv
import os
from datetime import datetime

# 1. Define the file paths
file_path = "week-7/data/expenses.csv"
report_path = "week-7/assignment-7/food_report.txt"

# 2. Check if the CSV file exists
if not os.path.exists(file_path):
    print("Error: expenses.csv not found.")
    raise SystemExit

# 3. Read the CSV file
food_expenses = []
total = 0

with open(file_path, "r", newline="") as file:
    expenses = csv.DictReader(file)

    for expense in expenses:
        # 4. Convert the amount to a float
        amount = float(expense["amount"])

        # 5. Filter Food expenses
        if expense["category"] == "Food":
            food_expenses.append({
                "date": expense["date"],
                "amount": amount
            })
            total += amount

# 6. Get today's date
today = datetime.now().strftime("%B %d, %Y")

# 7. Write the report
with open(report_path, "w") as report:
    report.write(f"Food Expense Report - generated {today}\n")

    for expense in food_expenses:
        report.write(
            f"{expense['date']}: ${expense['amount']:.2f}\n"
        )

    report.write(f"Total: ${total:.2f}\n")

print("Report created successfully!")
print(f"Total Food Expenses: ${total:.2f}")
