from database_connect import databaseConnection
from class_menu import Menu



def viewAccountMenu():
    db = databaseConnection()
    dbAccounts = db["accounts"]
    accounts = {}

    # Populate accounts with the accounts from DB
    count = 1
    for i in dbAccounts.find():
        accounts[count] = f"Account name: {i['name']} -- Balance: {i['balance']}"
        count += 1

    accounts[count] = "Add New Account"
    mainAccountMenu = Menu(accounts)
    return mainAccountMenu

def newAccountTypeMenu():
    typeMenu = Menu(
        {
            1: "Credit",
            2: "Cash",
        }
    )
    return typeMenu

def accountDetails():
    detailMenu = Menu({1: "Pay Account", 2: "Delete Account"})
    return detailMenu


