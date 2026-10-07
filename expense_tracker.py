import sqlite3

# Connect to the SQLite database.
# If the database does not exist, SQLite will create it.
connection = sqlite3.connect("expenses.db")

# Create a cursor that allows us to execute SQL commands.
cursor = connection.cursor()

# Gets a valid dollar amount from the user and prevents invalid input.
def get_valid_amount(prompt):
    while True:
        try:
            amount = float(input(prompt))

            if amount < 0:
                print("Amount cannot be negative. Please try again.")
            else:
                return amount

        except ValueError:
            print("Please enter a valid number.")

# Adds a new expense to the database using information entered by the user.
def add_expense():
    description = input("Enter expense description: ")
    category = input("Enter category: ")
    amount = get_valid_amount("Enter amount: $")
    expense_date = input("Enter date (YYYY-MM-DD): ")

    cursor.execute("""
        INSERT INTO expenses (description, category, amount, expense_date)
        VALUES (?, ?, ?, ?)
    """, (description, category, amount, expense_date))

    connection.commit()

    print("\nExpense added successfully!")


# Retrieves and displays all expenses stored in the database.
def view_expenses():
    cursor.execute("SELECT * FROM expenses")
    expenses = cursor.fetchall()

    print("\n--- ALL EXPENSES ---")

    if len(expenses) == 0:
        print("No expenses found.")
    else:
        for expense in expenses:
            print(
                f"ID: {expense[0]} | "
                f"Description: {expense[1]} | "
                f"Category: {expense[2]} | "
                f"Amount: ${expense[3]:.2f} | "
                f"Date: {expense[4]}"
            )
            
# Updates an existing expense selected by its ID.
def update_expense():
    view_expenses()

    expense_id = input("\nEnter the ID of the expense you want to update: ")

    # Check whether the selected expense exists.
    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )
    expense = cursor.fetchone()

    if expense is None:
        print("\nExpense not found.")
        return

    print("\nEnter the new information for this expense.")

    description = input("Enter new description: ")
    category = input("Enter new category: ")
    amount = get_valid_amount("Enter new amount: $")
    expense_date = input("Enter new date (YYYY-MM-DD): ")

    cursor.execute("""
        UPDATE expenses
        SET description = ?, category = ?, amount = ?, expense_date = ?
        WHERE id = ?
    """, (description, category, amount, expense_date, expense_id))

    connection.commit()

    print("\nExpense updated successfully!")

# Deletes an expense from the database using its ID.
def delete_expense():
    view_expenses()

    expense_id = input("\nEnter the ID of the expense you want to delete: ")

    # Check whether the selected expense exists.
    cursor.execute(
        "SELECT * FROM expenses WHERE id = ?",
        (expense_id,)
    )
    expense = cursor.fetchone()

    if expense is None:
        print("\nExpense not found.")
        return

    cursor.execute(
        "DELETE FROM expenses WHERE id = ?",
        (expense_id,)
    )

    connection.commit()

    print("\nExpense deleted successfully!")

# Calculates and displays summary information using SQL aggregate functions.
def spending_summary():
    cursor.execute("""
        SELECT COUNT(amount), SUM(amount), AVG(amount)
        FROM expenses
    """)

    summary = cursor.fetchone()

    expense_count = summary[0]
    total_spent = summary[1]
    average_expense = summary[2]

    print("\n--- SPENDING SUMMARY ---")

    if expense_count == 0:
        print("No expenses found.")
    else:
        print(f"Number of Expenses: {expense_count}")
        print(f"Total Spent: ${total_spent:.2f}")
        print(f"Average Expense: ${average_expense:.2f}")


# Displays the main menu and handles the user's menu selections.
def main_menu():
    while True:
        print("\n========================")
        print("     EXPENSE TRACKER")
        print("========================")
        print("1. Add Expense")
        print("2. View Expenses")
        print("3. Update Expense")
        print("4. Delete Expense")
        print("5. Spending Summary")
        print("6. Exit")

        choice = input("\nChoose an option: ")

        if choice == "1":
            add_expense()

        elif choice == "2":
            view_expenses()

        elif choice == "3":
            update_expense()

        elif choice == "4":
            delete_expense()

        elif choice == "5":
            spending_summary()

        elif choice == "6":
            print("\nThank you for using Expense Tracker!")
            break

        else:
            print("\nInvalid option. Please choose 1-6.")


# Create the expenses table if it does not already exist.
cursor.execute("""
    CREATE TABLE IF NOT EXISTS expenses (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        description TEXT NOT NULL,
        category TEXT NOT NULL,
        amount REAL NOT NULL,
        expense_date TEXT NOT NULL
    )
""")

# Start the Expense Tracker application.
main_menu()

# Close the database connection after the user exits.
connection.close()