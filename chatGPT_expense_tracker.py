#!/usr/bin/env python3

# Importing datetime module to work with dates
import datetime

# Function to input expenses
def input_expense():
	expense_date = input("Enter the date of the expense (YYYY-MM-DD): ")
	category = input("Enter the category of the expense: ")
	amount = float(input("Enter the amount spent (£): "))
	return {'date': expense_date, 'category': category, 'amount': amount}

# Function to display summary of expenses
def display_summary(expenses):
	print("\nExpense Summary:")
	total_spent = 0
	categories = {}
	for expense in expenses:
		total_spent += expense['amount']
		if expense['category'] in categories:
			categories[expense['category']] += expense['amount']
		else:
			categories[expense['category']] = expense['amount']
	print("Total spent: £", total_spent)
	print("\nCategory-wise spending:")
	for category, amount in categories.items():
		print(category + ": £", amount)
		
# Main function
def main():
	expenses = []
	while True:
		choice = input("\nEnter '1' to input an expense, '2' to display summary, or 'q' to quit: ")
		if choice == '1':
			expense = input_expense()
			expenses.append(expense)
		elif choice == '2':
			display_summary(expenses)
		elif choice.lower() == 'q':
			break
		else:
			print("Invalid choice. Please try again.")
			
# Run the program
if __name__ == "__main__":
	main()
	