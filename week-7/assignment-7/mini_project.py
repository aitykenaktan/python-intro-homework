import os
import csv
from datetime import datetime

path = os.path.join("..", "data", "expenses.csv")

if not os.path.exists(path):
    print("Error: expenses.csv not found.")
else:
    with open(path, "r") as file:
        expenses = list(csv.DictReader(file))

    for expense in expenses:
        expense["amount"] = float(expense["amount"])

    food_expenses = []

    for expense in expenses:
        if expense["category"] == "Food":
            food_expenses.append(expense)

    total = 0

    for expense in food_expenses:
        total += expense["amount"]

    today = datetime.now().strftime("%B %d, %Y")

    with open("food_report.txt", "w") as report:
        report.write(f"Food Expense Report — generated {today}\n")

        for expense in food_expenses:
            report.write(f"{expense['date']}: ${expense['amount']:.2f}\n")

        report.write(f"Total: ${total:.2f}\n")

    print("Food report created successfully.")