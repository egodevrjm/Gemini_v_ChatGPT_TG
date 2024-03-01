import datetime

# A simple class to represent an expense
class Expense:
    def __init__(self, date, category, description, amount):
        self.date = date
        self.category = category
        self.description = description
        self.amount = amount

# Initialize an empty list to store expenses
expenses = []

def add_expense():
    """Gets expense details from the user and adds them to the list"""

    date_str = input("Enter the date of the expense (YYYY-MM-DD): ")
    date = datetime.datetime.strptime(date_str, '%Y-%m-%d').date()  # Convert to a date object
    category = input("Enter the category (e.g., Groceries, Entertainment): ")
    description = input("Enter a description (optional): ")
    amount = float(input("Enter the amount: "))

    expenses.append(Expense(date, category, description, amount))
    print("Expense added successfully!")

def view_expenses():
    """Displays all recorded expenses"""

    if not expenses:
        print("No expenses recorded yet.")
        return

    print("\n--- Recorded Expenses ---")
    for expense in expenses:
        print(f"Date: {expense.date}, Category: {expense.category}, Description: {expense.description}, Amount: ${expense.amount:.2f}")

def expenses_by_category():
    """Summarizes expenses grouped by category"""

    category_wise = {}
    for expense in expenses:
        if expense.category in category_wise:
            category_wise[expense.category] += expense.amount
        else:
            category_wise[expense.category] = expense.amount

    print("\n--- Expenses by Category ---")
    for category, total in category_wise.items():
        print(f"{category}: ${total:.2f}")

def expenses_by_period():
    """Calculates total expenses for a specified period"""

    start_date_str = input("Enter the start date (YYYY-MM-DD): ")
    end_date_str = input("Enter the end date (YYYY-MM-DD): ")
    start_date = datetime.datetime.strptime(start_date_str, '%Y-%m-%d').date()
    end_date = datetime.datetime.strptime(end_date_str, '%Y-%m-%d').date()

    total_in_period = 0.0
    for expense in expenses:
        if start_date <= expense.date <= end_date:
            total_in_period += expense.amount

    print(f"\nTotal expenses between {start_date} and {end_date}: ${total_in_period:.2f}")


# Main menu loop
while True:
    print("\n--- Expense Tracker Menu ---")
    print("1. Add Expense")
    print("2. View Expenses")
    print("3. Expenses by Category")
    print("4. Expenses by Period")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == '1':
        add_expense()
    elif choice == '2':
        view_expenses()
    elif choice == '3':
        expenses_by_category()
    elif choice == '4':
        expenses_by_period()
    elif choice == '5':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
