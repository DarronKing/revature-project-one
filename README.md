# Revature Project One: Expense Tracker

## Use Python and MongoDB to create an Expense Tracker
Using Python and MongoDB I created a simple command line interface program that anyone can use to both, track their expenses, manage their account balances, create new accounts, and get detailed analytics on monthly and yearly expense patterns.

## Technologies Used
* Python 3
* MongoDB
* PyMongo

## Features
* Adding in expenses automatically removes/adds balances to accounts
* Viewing and creating accounts
* Paying credit cards automatically removes from the USD account
* Get detailed analytics on expenses based on the category of expense

### TO-DO List
* Make more analytics (monthly-yearly, based on store, based on type, etc)
* Automatically set up databases and MongoDB when installing

## Getting Started
git clone https://github.com/DarronKing/revature-project-one.git

### Software needed
* Python 3
* MongoDB

Inside of MongoDB Shell
* Set up database: revatureTrial
  * use revatureTrial
* Set up two collections: expenses, accounts
  * db.createCollection("expenses")
  * db.createCollection("accounts")

Run main.py
