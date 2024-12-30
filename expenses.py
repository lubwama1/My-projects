


import sqlite3
from datetime import datetime

# Database setup
DB_NAME = 'expenses_db'

def initialize_database():
    """Create the database and expenses table if not exists."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT, 
        description TEXT NOT NULL, 
        category TEXT NOT NULL, 
        amount REAL NOT NULL, 
        date TEXT NOT NULL
    )""")
    conn.commit()
    conn.close()

def add_expense(description, category, amount, date):
    """Add an expense to the database."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO expenses (description, category, amount, date) VALUES (?, ?, ?, ?)",
                   (description, category, amount, date))
    conn.commit()
    conn.close()

def view_expenses():
    """View all expenses."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM expenses")
    rows = cursor.fetchall()
    conn.close()
    if rows:
        print("\nAll Expenses")
        print("-" * 64)
        print(f"{'ID':<5} {'DESCRIPTION':<20} {'CATEGORY':<15} {'AMOUNT':<10} {'DATE'}")
        print("-" * 64)
        for row in rows:
            print(f"{row[0]:<5} {row[1]:<20} {row[2]:<15} {row[3]:<10.2f} {row[4]}")
        print("-" * 64)
    else:
        print("No available expenses. Please try to add expenses.")

def generate_report():
    """Generate a text report of total expenses."""
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()
    cursor.execute("SELECT category, SUM(amount) FROM expenses GROUP BY category")
    rows = cursor.fetchall()
    conn.close()
    report = "Expense Report\n"
    report += "_" * 40 + "\n"
    report += f"{'Category':<20} {'Total Amount':<10}\n"
    total = 0

    for row in rows:
        report += f"{row[0]:<20} ${row[1]:<10.2f}\n"
        total += row[1]

    report += "_" * 40 + "\n"
    report += f"Total Expenses: ${total:.2f}\n"

    # Save report to a file
    with open("expense_report.txt", "w") as file:
        file.write(report)
    print("\nReport generated and saved as expense_report.txt.")

def view_report(file_name, mode):
    """Open and display the file expense_report.txt."""
    try:
        with open(file_name, mode) as file:
            content = file.read()
            if content.strip():
                print("-" * 40)
                print(content.strip())
            else:
                print("No available report at the moment.\nPlease try to add expenses first.")
    except FileNotFoundError:
        print("Error: The specified file does not exist.")

def main():
    initialize_database()
    while True:
        print("\nPersonal Expense Tracker")
        print("1. Add Expenses")
        print("2. View Expenses")
        print("3. Generate Report")
        print("4. View Report")
        print("5. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            description = input("Enter description: ")
            category = input("Enter category: ")
            try:
                amount = float(input("Enter amount: "))
                date = input("Enter date (YYYY-MM-DD): ")
                datetime.strptime(date, "%Y-%m-%d")  # Validate date format
                add_expense(description, category, amount, date)
                print("Expense added successfully.")
            except ValueError:
                print("Invalid input. Please ensure the amount is a number and the date is in YYYY-MM-DD format.")
        elif choice == "2":
            view_expenses()
        elif choice == "3":
            generate_report()
        elif choice == "4":
            view_report("expense_report.txt", "r")
        elif choice == "5":
            print("Exiting... goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()