from unicodedata import category
import pandas as pd
from matplotlib import pyplot as plt
import random

from database_connect import databaseConnection


def expenseBreakdown():
    db = databaseConnection()
    dbExpenses = db["expenses"]
    expenseArr = []
    categoryArr = []
    colorsArr = []

    df = pd.DataFrame(
        dbExpenses.aggregate(
            [{"$group": {"_id": "$category", "total_amt": {"$sum": "$cost"}}}]
        )
    )

    if len(df) > 0:

        # Fill the Cost array with a list of all the expenses
        for i in df["total_amt"]:
            expenseArr.append(float(i))

        # # Fill the category array
        for i in df["_id"]:
            categoryArr.append(i)
        # # Make Color Array based on the length of the categories (categories will be used as labels)
        for i in categoryArr:
            colorsArr.append(
                (random.randrange(1, 10)/10, random.randrange(1, 10)/10,
                random.randrange(1, 10)/10)
            )

        plt.pie(
            expenseArr,
            labels=categoryArr,
            colors=colorsArr,
            autopct="%1.1f%%",
            shadow=True,
            startangle=140,
        )

        plt.axis('equal')
        plt.show()

    else:
        print("    #########################")
        print("     No Expenses in Database")
        print("    #########################")
        print("      Returning to Main Menu")
