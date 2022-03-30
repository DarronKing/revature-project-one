from database_connect import databaseConnection
from class_menu import Menu

def createStoreMenu():

    storeMenu = Menu(
        {
            1: "Costco",
            2: "Amazon",
            3: "Walmart",
            4: "Other",
        }
    )
    return storeMenu

def createAccountsMenu():
    db = databaseConnection()
    dbAccounts = db["accounts"]

    accounts = {}
    c = 1
    for i in dbAccounts.find():
        accounts[c] = i["name"]
        c += 1
    accountsMenu = Menu(accounts)
    return accountsMenu

def createCategoryMenu():
    categoryMenu = Menu(
        {
            1: "Housing",
            2: "Personal Health",
            3: "Food",
            4: "Transportation",
            5: "Misc. Living Costs",
            6: "Medical",
            7: "Insurance",
            8: "Savings / Investments",
            9: "Personal Spending",
            10: "Debts",
        }
    )
    return categoryMenu