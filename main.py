from task_manager import (add_items, update_items, list_expenses, list_expenses_by_category, delete_item, summary, summary_expenses_by_month, export_csv)
import argparse # Import a built-in module function in python for using commandLine arguments

# Creates a parser for the imported built-in module function that act as an helper that understand hat the user types in through the terminal
parser = argparse.ArgumentParser() 

# This is a subparser that holds/contains all other command the user types in through the Terminal as CommandLine arguments
subparsers = parser.add_subparsers(dest="command")

# ----- ADD Command --------
add_parser = subparsers.add_parser("add")
add_parser.add_argument("description")
add_parser.add_argument("amount", type=float)
add_parser.add_argument("category")

# ------ UPDATE Command -------
update_parser = subparsers.add_parser("update")
update_parser.add_argument("id", type=int)
update_parser.add_argument("description")
update_parser.add_argument("amount", type=float)

# ------ DELETE Command -------
delete_parser = subparsers.add_parser("delete")
delete_parser.add_argument("id", type=int)

#-------- LIST Command ---------
list_parser = subparsers.add_parser("list")
list_parser.add_argument("--category")

# ------ SUMMARY Command ---------
summary_parser = subparsers.add_parser("summary")
summary_parser.add_argument("--month", type=int)

# ----------- Export COMMAND -----------
export_parser  = subparsers.add_parser("export")


args = parser.parse_args()

if args.command == "add":
    description = args.description
    amount = args.amount
    category = args.category
    add_items(description, amount, category)
    # add_items(args.description, args. amount)

elif args.command == "update":
    item_id = args.id
    description = args.description
    amount =  args.amount
    update_items(item_id, description, amount)
    # update_items(args.id, args.description, args.amount)

elif args.command == "list":
    if args.category:
        category = args.category
        list_expenses_by_category(category)
    else:
        list_expenses()

elif args.command =="delete":
    item_id =  args.id
    delete_item(item_id)

elif args.command == "summary":
    if args.month:
        month = args.month
        summary_expenses_by_month(month)
    else:
        summary()

elif args.command == "export":
    export_csv()