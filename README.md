# Expense Tracker CLI

A simple Command Line Interface (CLI) Expense Tracker built with Python. This application allows users to manage their daily expenses directly from the terminal by adding, updating, deleting, listing, summarizing, and exporting expense records.

## Features

- Add a new expense with a description, amount, and category.
- Update an existing expense.
- Delete an expense by ID.
- View all expenses.
- Filter expenses by category.
- View a summary of all expenses.
- View a monthly expense summary.
- Export expenses to a CSV file.
- Store expense data in a JSON file.
- Built-in input validation and error handling.

## Technologies Used

- Python 3
- argparse
- JSON
- CSV
- datetime

## Project Structure

```
Expense-Tracker/
│── main.py
│── task_manager.py
│── storage.py
│── models.py
│── expenses.json
│── README.md
```

## Usage

### Add an Expense

```bash
python main.py add "Lunch" 20 Food
```

### Update an Expense

```bash
python main.py update 1 "Dinner" 30
```

### Delete an Expense

```bash
python main.py delete 1
```

### List All Expenses

```bash
python main.py list
```

### Filter Expenses by Category

```bash
python main.py list --category Food
```

### View Total Expense Summary

```bash
python main.py summary
```

### View Monthly Summary

```bash
python main.py summary --month 7
```

### Export Expenses to CSV

```bash
python main.py export
```

## Data Storage

Expenses are stored locally in a JSON file, making the application lightweight and easy to use without a database.

## Error Handling

The application validates user input by checking for:

- Invalid expense IDs
- Invalid month values
- Invalid amounts
- Empty expense records
- Non-existent categories
- Missing expenses during export

## Learning Outcomes

This project helped reinforce concepts such as:

- Command-line argument parsing with `argparse`
- Working with JSON files
- Reading and writing CSV files
- Functions and modular programming
- Error handling and input validation
- Python file handling
- Project structure and code organization

## Future Improvements

- Monthly budget tracking
- Budget warnings
- Search expenses
- Expense sorting
- Data visualization
- SQLite database support

---

Roasmap.sh URL: https://roadmap.sh/projects/expense-tracker
GutHub repo: https://github.com/emmanueldrivescode/Expense-Tracker

Built as a learning project while improving Python and backend development skills.