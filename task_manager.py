from storage import (load_expenses as load, save_expenses as save)
from models import (create_item)
from datetime import datetime
import calendar, os, csv

# ---- Adds Function------
def add_items(description, amount, category):

    expenses = load()
    
    if expenses:
        new_id = expenses[-1]['ID'] + 1
    else:
        new_id = 1

    new_item = create_item(new_id, description, amount, category)
    expenses.append(new_item)
    save(expenses)
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
           save(expenses)
           print("Expense updated successfully!")
           return
       
    print("Expense ID Not Found!")

# ------ Display Function --------
def display_expenses(item):
    print(f"ID : {item['ID']}")
    print(f"Description : {item['Description']}")
    print(f"Category : {item['Category']}")
    print(f"Amount : ${item['Amount']}")
    print(f"Created Date: {item['Created Date']}")
    print(f"Updated Date : {item['Updated Date']}")
    print()

# ------- List Function -------
def list_expenses_by_category(category):
    expenses = load()
    found = False

    for item in expenses:
        if category == item['Category']:
            display_expenses(item)
            found = True
    
    if not found:
        print("Category Not Found!")

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
            save(expenses)
            print("Expense deleted successfully!")
    else:
        print("Task Not Found!")

def summary():
    expenses = load()
    total = 0

    for item in expenses:
        total += item['Amount']

    print(f"Total Expenses = ${total}")

# ----- Summary Monthly Function -------
def summary_expenses_by_month(month):
    expenses = load()
    total = 0

    for item in expenses:
        item_month = int(item['Created Date'].split("-")[1])

        if item_month == month:
            total += item['Amount']
    
    month_name = calendar.month_name[month]
    print(f"Total expenses for {month_name} = ${total}")

def export_csv():
    expenses = load()
    file_name =  "expense.csv"

    if os.path.exists(file_name):
        print("Expense CSV file already exist!")
        return
    
    if not os.path.exists(file_name):
        with open(file_name, "w", newline="") as file:
            writer = csv.writer(file)

            writer.writerow(['ID', 'DESCRIPTION', 'CATEGORY', 'AMOUNT', 'TIME CRATED', 'TIME UPDATED'])

            for item in expenses:
                writer.writerow([
                    item['ID'],
                    item['Description'],
                    item['Category'],
                    item['Amount'],
                    item['Created Date'],
                    item['Updated Date']
                ])
    
    print("Expenses exported successfully!")