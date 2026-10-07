# SQL Expense Tracker

## Overview

This software is a command-line expense tracker written in Python. The program uses a SQLite relational database to store and manage expense information.

The user can add new expenses, view saved expenses, update existing expenses, and delete expenses. The program also provides a spending summary using SQL aggregate functions to calculate the number of expenses, total amount spent, and average expense amount.

I wrote this software to improve my understanding of relational databases and learn how Python can interact with a database using SQL commands. This project gave me experience creating tables, inserting data, retrieving data, modifying records, deleting records, and using aggregate functions.

[Software Demo Video] https://youtu.be/O5-y2iu7Q8A

## Relational Database

The program uses SQLite as the relational database.

The database contains an `expenses` table with the following fields:

- `id` - Integer primary key that automatically increments
- `description` - Text description of the expense
- `category` - Text category for the expense
- `amount` - Numerical value representing the expense amount
- `expense_date` - Text value containing the date of the expense

The program performs SQL operations including `CREATE TABLE`, `INSERT`, `SELECT`, `UPDATE`, and `DELETE`.

The spending summary also uses the SQL aggregate functions `COUNT()`, `SUM()`, and `AVG()`.

## Development Environment

The software was developed using:

- Visual Studio Code
- Python
- SQLite
- Python `sqlite3` module

The program was written in Python and uses the built-in `sqlite3` library to communicate with the SQLite database.

## Useful Websites

- [Python sqlite3 Documentation](https://docs.python.org/3/library/sqlite3.html)
- [SQLite Documentation](https://www.sqlite.org/docs.html)
- [CSE 310 Applied Programming Course](https://byui-cse.github.io/cse310-ww-course/)

## Future Work

- Add the ability to search expenses by category.
- Add date validation for expense dates.
- Add spending summaries for individual categories.
- Add the ability to filter expenses by a date range.