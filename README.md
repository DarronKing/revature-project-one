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

Run the two following commands in Command Prompt to start the MongoDB shell and Server
* "C:\Program Files\MongoDB\Server\5.0\bin\mongod.exe" --dbpath="c:\data\db"
  * Starts the mongoDB server --The mongoDB server needs to be ran every time for the program to function 
* "C:\Program Files\MongoDB\Server\5.0\bin\mongo.exe"
  * Starts the mongoDB shell --Only required for setting up the dataBase -- first time only --

Inside of MongoDB Shell
* Set up database: revatureTrial
  * use revatureTrial
* Set up two collections: expenses, accounts
  * db.createCollection("expenses")
  * db.createCollection("accounts")

Run main.py
