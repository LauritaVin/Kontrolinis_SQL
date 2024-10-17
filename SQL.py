import sqlite3

#create database

conn = sqlite3.connect("Finances.sqlite")
c = conn.cursor()

#create empty table

with conn:
    c.execute ('''CREATE TABLE IF NOT EXISTS finances(
    id SERIAL NOT NULL PRIMARY KEY,
    type STRING,
    amount INTEGER NOT NULL,
    category STRING)''')

def enter (id, type, amount, category):
    c.execute("INSERT INTO finances (id, type, amount, category) VALUES (?, ?, ?, ?)",
                   (id, type, amount, category))

    conn.commit()
    print("Amount added successfully!")

def enter_income():
    id = int(input("Enter transaction id: "))
    type = "income"
    while True:
        amount = float(input("Enter income amount: "))
        if round(amount, 2) == amount:
            break
        print("Income amount format invalid.")
    category = input("Enter income type: ")
    enter(id, type, amount, category)

def enter_expense():
    id = int(input("Enter transaction id: "))
    type = "expense"
    while True:
        amount = float(input("Enter expense amount (negative number): "))
        if amount < 0 and round(amount, 2) == amount:
            break
        print("Expense amount must be negative.")
    category = input("Enter expense type: ")
    enter(id, type, amount, category)

def get_balanse():
    c.execute("SELECT SUM (amount) FROM finances")
    conn.commit()

    sum = c.fetchone()[0]

    print(f"Total balance is: {sum}")

def get_all_icome():
    c.execute("SELECT * FROM finances WHERE type = 'income'")
    conn.commit()

    total_income = c.fetchall()

    print(f"Total recorded income: {total_income}")

def get_all_expense():
    c.execute("SELECT * FROM finances WHERE type = 'expense'")
    conn.commit()

    total_expense = c.fetchall()

    print(f"Total recorded expenses: {total_expense}")

def delete_info():

    id = int(input("Enter transaction id which you want to delete: "))

    c.execute("DELETE FROM finances WHERE id = ?",
              (id,))
    conn.commit()

    print("Amount deleted successfully!")

def update_info():

    id = int(input("Enter transaction id which you want to update: "))
    amount = float(input("Enter new amount: "))
    category = input("Enter new category: ")
    type = input("Enter new type: ")

    c.execute("UPDATE finances SET type = ?, amount = ?, category = ? WHERE id = ?",
              (type, amount, category, id))

    print("Information updated successfully!")
def main():

    while True:
        print("Please select one from the menu: ")
        print("1. Enter income")
        print("2. Enter expenses")
        print("3. Get balance")
        print("4. Get all incomes")
        print("5. Get all expenses")
        print("6. Delete income/expense")
        print("7. Update income/expense")
        print("8. Exit")

        menu_number = int(input("Please select one from the menu: "))

        if menu_number == 1:
            enter_income()

        if menu_number == 2:
            enter_expense()

        if menu_number == 3:
            get_balanse()

        if menu_number == 4:
            get_all_icome()

        if menu_number == 5:
            get_all_expense()

        if menu_number == 6:
            delete_info()

        if menu_number == 7:
            update_info()

        if menu_number == 8:
            break

if __name__ == "__main__":
    main()

conn.close()