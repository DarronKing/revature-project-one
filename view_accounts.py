from bson.objectid import ObjectId

from database_connect import databaseConnection
from view_account_menus import viewAccountMenu, newAccountTypeMenu, accountDetails


def viewAccounts():
    db = databaseConnection()
    dbAccounts = db["accounts"]

    mainMenu = viewAccountMenu()

    mainMenu.printMenu()
    mainResponse = mainMenu.getResponse("Select an account: ")

    if mainResponse == 0:
        return

    if mainResponse == len(mainMenu.menu):
        newAccountName = input("Enter the name of the new account: ")
        if newAccountName == 0:
            return

        newAccountBalance = input("Enter the current balance of the new account: ")

        typeMenu = newAccountTypeMenu()
        typeMenu.printMenu()
        newAccountType = typeMenu.getResponse("Enter the new account type: ")

        newAccount = {
            "name": newAccountName,
            "balance": newAccountBalance,
            "type": newAccountType,
        }

        dbAccounts.insert_one(newAccount)

        print("    ##########################")
        print("   Successfully Created Account")
        print("    ##########################")
        print("      Returning to Main Menu")

    else:
        detailMenu = accountDetails()
        accounts = {}
            
        count = 1
        for i in dbAccounts.find():
            accounts[count] = i
            count += 1

        account = accounts[mainResponse]

        print ("###################")
        print(f"Account Name: {account['name']}")
        print(f"Balance: {round(float(account['balance']), 2)}")
        if "payment_due" in account:
            print(f"Due Date: {account['payment_due']}")
        print ("###################")

        detailMenu.printMenu()
        detailResponse = detailMenu.getResponse("Select: ")

        if detailResponse == 1:
            payAmount = input("Enter the amount: ")
            # If account type == credit, then we are going to decrease the balance
            if account["type"] == "credit":
                payAmount = float(payAmount) * -1
                dbAccounts.update_one(
                    {"name" : "USD"},
                    {"$inc": {"balance": round(payAmount, 2)}},
                )

            dbAccounts.update_one(
                {"_id": ObjectId(account["_id"])},
                {"$inc": {"balance": round(float(payAmount), 2)}},
            )

            if account["type"] == "credit":
                print("    #########################")
                print("    Successfully Paid Account")
                print("    #########################")
                print("      Returning to Main Menu")
            elif account["type"] == "cash":
                print("    ##########################")
                print("     Successfully Added Cash")
                print("    ##########################")
                print("      Returning to Main Menu")
        
        if detailResponse == 2:
            dbAccounts.delete_one({"_id" : ObjectId(account["_id"])})

            print("    ##########################")
            print("   Successfully Deleted Account")
            print("    ##########################")
            print("      Returning to Main Menu")
