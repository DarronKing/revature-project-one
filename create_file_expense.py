from database_connect import databaseConnection
import json

def createFileExpense():
    db = databaseConnection()
    dbExpenses = db["expenses"]

    # file = input("enter the json: ")

    # fileOpen = open("/revature-project-one/expenseJSON/" + str(file), 'r')
    # fileOpen = open("C:\\Users\dare5\Documents\Revature\projectOneV1.2\revature-project-one\expenseJSON" + str(file), 'r')
    # fileOpen = open(file, 'r')

    # fileOpen = open("revature-project-one/" + file, 'r')
    # fileOpen = open("C:/Users/dare5/Documents/Revature/revature-project-one/" + file)
    # data = json.load(fileOpen)
    # print(data)


    while True:
        try:
            file = input("Enter the json file name: ")
            if file == "0":
                break

            # fileOpen = open("revature-project-one/" + file, 'r')
            fileOpen = open("C:/Users/dare5/Documents/Revature/revature-project-one/" + file)

            data = json.load(fileOpen)
            dbExpenses.insert_many(data)
            print("    #########################")
            print("         Expenses Added")
            print("    #########################")
            print("      Returning to Main Menu")

            fileOpen.close()
            break
        
        except:
            print('Failed to load file, make sure it is in directory -')
            print(" C:/Users/dare5/Documents/Revature/projectOneV1.2/expenseJSON")

    if file == 0:
        return

