from bson.objectid import ObjectId
from datetime import date

from database_connect import databaseConnection
from create_expense_menus import createStoreMenu, createAccountsMenu, createCategoryMenu


def addExpense():
    db = databaseConnection()
    dbExpenses = db["expenses"]
    dbAccounts = db["accounts"]
    today = date.today()

    expenseData = {
        "cost": 0.0,
        "date": today.isoformat(),
        "store": "",
        "account_id": "",
        "category": "",
        "description": "",
    }

    print("Enter the cost:", end=" ")
    while True:
        try:
            costResponse = float(input())
            if costResponse == 0:
                break
            expenseData["cost"] = costResponse
            break
        except:
            print("Only float values accepted. Please re-enter the cost:", end=" ")
    if costResponse == 0:
        return

    storeMenu = createStoreMenu()
    storeMenu.printMenu()
    storeResponse = storeMenu.getResponse("Select the store name: ")

    if storeResponse == 0:
        return
    if storeResponse == 4:
        print("Please type the name of the store:", end=" ")
        storeResponse = input()
        expenseData["store"] = storeResponse
        print(expenseData)
    else:
        expenseData["store"] = storeMenu.menu[storeResponse]

    accountsMenu = createAccountsMenu()
    accountsMenu.printMenu()
    accountResponse = accountsMenu.getResponse("Select the account used: ")
    if accountResponse == 0:
        return
    else:
        expenseData["paymentMethod"] = accountsMenu.menu[accountResponse]
        # Get the account data that they selected
        account = dbAccounts.find_one({"name": expenseData["paymentMethod"]})
        expenseData["paymentMethod"] = account["_id"]

    categoryMenu = createCategoryMenu()
    categoryMenu.printMenu()
    categoryResponse = categoryMenu.getResponse("Select the expense category: ")

    if categoryResponse == 0:
        return
    else:
        expenseData["category"] = categoryMenu.menu[categoryResponse]


    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")
    expenseData["description"] = input("Enter a description: ")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~")


    addedExpenseId = dbExpenses.insert_one(expenseData)

    # If the account is type == cash we need to minus instead of adding
    if account["type"] == "cash":
        expenseData = expenseData["cost"] * -1
    # Update the account balance
    try:
        dbAccounts.update_one(
            {"_id": ObjectId(account["_id"])},
            {"$inc": {"balance": round(float(expenseData["cost"]), 2)}},
        )
    except:
        # If increasing/decreasing the balance fails delete the added expense
        dbExpenses.delete_one({"_id": ObjectId(addedExpenseId.inserted_id)})
        print("    #########################")
        print("  ERROR : Failed to Add Expense")
        print("    #########################")
        print("      Returning to Main Menu")

    print("    ##########################")
    print("    Successfully Added Expense")
    print("    ##########################")
    print("      Returning to Main Menu")
