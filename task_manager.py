from storage import (load_expenses as load, save_expenses)
from models import (create_item)
from datetime import datetime

# ---- Adds Function------
def add_items(description, amount):

    expenses = load()
    
    if expenses:
        new_id = expenses[-1]['ID'] + 1
    else:
        new_id = 1

    new_item = create_item(new_id, description, amount)
    expenses.append(new_item)
    save_expenses(expenses)
    print("Expense added succesfully!")

# ------ Update Function ------
def update_items(item_id, description, amount):
    expenses =  load()

    for item in expenses:
       if item_id == item['ID']:
           current_time = datetime.now().strftime("%Y-%m-%d %H:%M")

           item['Description'] = description
           item['Amount'] = amount
           item['Updated Date'] = current_time
           save_expenses(expenses)
           print("Expense updated successfully!")
           return
       
    print("Expense ID Not Found!")

# ------ Display Function --------
def display_expenses(item):
    print(f"ID : {item['ID']}")
    print(f"Description : {item['Description']}")
    print(f"Amount : ${item['Amount']}")
    print(f"Created Date: {item['Created Date']}")
    print(f"Updated Date : {item['Updated Date']}")
    print()

# ------- List Function -------
def list_expenses():
    expenses = load()

    for item in expenses:
        display_expenses(item)

# ------ Delete Function --------
def delete_item(item_id):
    expenses = load()

    for item in expenses:
        if item_id == item['ID']:
            expenses.remove(item)
            save_expenses(expenses)
            print("Expense deleted successfully!")
    else:
        print("Task Not Found!")

# ----- Summary Function -------
def summary_expenses():
    expenses = load()

    total = 0
    for item in expenses:
        total += item['Amount']

    print(f"Total Expenses = ${total}")

# ------ Monthly Summary Function ---------
def summary_expenses_by_month(month):
    expenses = load()

    total = 0

    for item in expenses:
        if month == item['Created Date'].split("-")[1]:
            total += item['Amount']

    print(f"Total Expenses for July = ${total}")

