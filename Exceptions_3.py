import json
try:
    with open("expenses.json","r") as file:
        expenses = json.load(file)
except FileNotFoundError:
    print("error: expenses.json was not found")
except json.JSONDecodeError:
    print("error: expenses.json contains invalid JSON.")
else:
    print("Expenses loaded sucessfully")
    print(expenses)
