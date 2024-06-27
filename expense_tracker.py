import csv
import os

# Constants
DATA_FILE = 'expenses.csv'
CATEGORIES = ['Food', 'Utilities', 'Transportation', 'Entertainment', 'Miscellaneous']

# Function to initialize the CSV file if it doesn't exist
def initialize_csv():
    if not os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Amount', 'Category', 'Description'])

# Function to add a new expense to CSV
def add_expense(amount, category, description):
    with open(DATA_FILE, 'a', newline='') as f:
        writer = csv.writer(f)
        writer.writerow([amount, category, description])
    print("Expense added successfully!")

# Function to display summary of expenses
def display_summary():
    total_spent = 0
    category_spending = {category: 0 for category in CATEGORIES}

    with open(DATA_FILE, 'r', newline='') as f:
        reader = csv.DictReader(f)
        for row in reader:
            amount = float(row['Amount'])
            category = row['Category']
            total_spent += amount
            if category in category_spending:
                category_spending[category] += amount
    
    if total_spent == 0:
        print("No expenses recorded yet.")
    else:
        print(f"\nTotal money spent: ${total_spent:.2f}")
        print("\nCategory-wise spending:")
        for category, amount in category_spending.items():
            print(f"{category}: ${amount:.2f}")

# Function to select expense category
def select_category():
    print("\nSelect a category:")
    for i, category in enumerate(CATEGORIES, start=1):
        print(f"{i}. {category}")
    choice = int(input("Enter category number: "))
    return CATEGORIES[choice - 1]

# Main menu function
def main_menu():
    initialize_csv()
    
    while True:
        print("\nExpense Tracker Menu:")
        print("1. Add Expense")
        print("2. View Expense Summary")
        print("3. Exit")
        choice = input("Enter your choice (1-3): ")

        if choice == '1':
            amount = float(input("Enter the amount spent: "))
            category = select_category()
            description = input("Enter a short description: ")
            add_expense(amount, category, description)
        elif choice == '2':
            display_summary()
        elif choice == '3':
            print("Exiting Expense Tracker. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

# Entry point of the program
if __name__ == "__main__":
    main_menu()
