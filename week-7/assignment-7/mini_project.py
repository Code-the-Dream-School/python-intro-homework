import os
import csv
from datetime import date

with open("/Users/melaniesutton/Documents/CodeTheDream/python-intro-homework/week-7/data/expenses.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

records = []
with open("/Users/melaniesutton/Documents/CodeTheDream/python-intro-homework/week-7/data/expenses.csv", 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        records.appcdend(row)

for item in records:
    item['amount'] = float(item['amount'])

if os.path.exists("/Users/melaniesutton/Documents/CodeTheDream/python-intro-homework/week-7/data/expenses.csv"):
    print("expenses.csv found.")
else:
    print("expenses.csv not found.")

food = [item for item in records if item['category'] == 'Food']
print("This is food.", food)

total = 0 
for item in food:
    total = total + item['amount']
print("Total:", total)

# Generate today's date
today = date.today().strftime("%B %d, %Y")
#write in the file
with open("food_report.txt", "w") as report:
    report.write(f"Food Expense Report — generated {today}\n")
    print("We are here")

    for item in food:
        report.write(
            f'{item["date"]}: ${item["amount"]:.2f}\n'
        )

    report.write(f"Total: ${total:.2f}\n")

from datetime import datetime
now = datetime.now()
#print(now.strftime("Food Expense Report - generated %B %d, %Y"))  
print("Current working directory:", os.getcwd())
print("Report location:", os.path.abspath("food_report.txt"))