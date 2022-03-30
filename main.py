from class_menu import Menu
from create_expense import addExpense
from view_accounts import viewAccounts
from create_file_expense import createFileExpense

mainMenu = Menu(
    {
        1: "Add Expense",
        2: "View Accounts",
        3: "Expense Breakdown",
        4: "Add Bulk Expenses from JSON (Does not update balances!)",
    }
)

print("    #########################")
print("         Expense Tracker")
print("    #########################")

while True:
    mainMenu.printMenu()
    response = mainMenu.getResponse("Select your choice: ")

    if response == 0:
        break

    if response == 1:
        addExpense()
    elif response == 2:
        viewAccounts()
    elif response == 4:
        createFileExpense()

