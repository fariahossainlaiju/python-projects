
import json

print("=== Personal Expense Tracker ===")

try:
    with open("expenses.json", "r") as file:
        expenses = json.load(file)

    if not isinstance(expenses, list):
        expenses = []

except (FileNotFoundError, json.JSONDecodeError):
    expenses = []


def save_expenses():
    with open("expenses.json", "w") as file:
        json.dump(expenses, file, indent=4)


def add_expense():
    category = input("Enter expense category: ")

    try:
        amount = float(input("Enter amount: "))
    except ValueError:
        print("Please enter a valid number.")
        return

    expense = {
        "category": category,
        "amount": amount
    }

    expenses.append(expense)
    save_expenses()

    print("Expense added successfully!")


def show_expenses():
    if not expenses:
        print("No expenses found.")
        return

    for expense in expenses:
        print(
            "Category:", expense["category"],
            "| Amount:", expense["amount"]
        )


def total_expense():
    total = sum(
        expense["amount"] for expense in expenses
    )
    print("Total expense:", total)


while True:
    print("\n=== MENU ===")
    print("1. Add expense")
    print("2. Show expenses")
    print("3. Total expense")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_expense()
    elif choice == "2":
        show_expenses()
    elif choice == "3":
        total_expense()
    elif choice == "4":
        print("Thank you!")
        break
    else:
        print("Invalid choice. Try again.")
