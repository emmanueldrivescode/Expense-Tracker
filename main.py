from task_manager import (add_items, update_items, list_expenses, delete_item, summary_expenses)
import argparse

parser = argparse.ArgumentParser()

subparsers = parser.add_subparsers(dest="command")

# ----- ADD Command --------
add_parser = subparsers.add_parser("add")
add_parser.add_argument("description")
add_parser.add_argument("amount", type=float)

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

# ------ SUMMARY Command ---------
summary_parser = subparsers.add_parser("summary")
summary_parser.add_argument("--fimonth", type=int)


args = parser.parse_args()

if args.command == "add":
    description = args.description
    amount = args.amount
    add_items(description, amount)
    # add_items(args.description, args. amount)

elif args.command == "update":
    item_id = args.id
    description = args.description
    amount =  args.amount
    update_items(item_id, description, amount)
    # update_items(args.id, args.description, args.amount)

elif args.command == "list":
    list_expenses()

elif args.command =="delete":
    item_id =  args.id
    delete_item(item_id)

elif args.command == "summary":
    summary_expenses()