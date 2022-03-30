import pandas as pd
from matplotlib import pyplot as plt

from database_connect import databaseConnection

def expenseBreakdown():
    db = databaseConnection()
    dbExpenses = db["expenses"]
    
    #TODO: Pull the data from the database all organized like 

    df = pd.DataFrame(dbExpenses.find())

    plt.pie(df["cost"])
    plt.show()

    # print(df)

expenseBreakdown()