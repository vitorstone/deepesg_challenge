"""
Input Handler

This script allows the user to choose whether the input data will come from a relational database
or a .xlsx file

This script requires that `pandas` be installed within the Python
environment you are running this script in.
`mysql-connector-python` is optional , depending on the use case.

This file can also be imported as a module and contains the following
functions:

    * get_accounts_data - returns a variable containing the account numbers (type of return depends
                          on chosen option

    * get_ledger_data - returns a variable containing the transactions data (accounts and values)
                        (type of return depends on chosen option)

Important:
    option = 1 -> data will come from relational database
    option =2 -> data will come from .xlsx files

"""

import mysql.connector
import pandas as pd


def get_accounts_data(excel_filename="", option=2):
    """
        this method iterates through the chart of accounts and returns its data

        Parameters
        -----------
        excel_filename: str
            string containing the excel file name for the chart of accounts

        option: int , default = 2
            if option = 1, it means data comes from database and if it is 2 then
            it means data comes from .xlsx file

        Returns
        --------
            accounts_data: list of tuples or DataFrame
                the output contains the account number
                if option = 1 then it returns a list of tuples
                if option = 2 then it returns a DataFrame
    """

    if option == 1:

        # this part of the code connects to a relational database and retrieves the account numbers from it

        # db = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     passwd="root",
        #     database="my_database"
        # )
        # mycursor = db.cursor()
        # mycursor.execute("SELECT account FROM chart_of_accounts")
        # accounts_data = mycursor.fetchall()

        # dummy data replicating type of data that will come from database (list of tuples)
        accounts_data = [('1',), ('1.1',), ('1.2',), ('1.2.1',), ('1.2.2',), ('1.3',), ('1.3.1',), ('1.3.1.1',), ('1.3.1.3',)]
        return accounts_data

    else:
        # reading account numbers from excel file
        accounts_data = pd.read_excel(excel_filename)
        return accounts_data


def get_ledger_data(excel_filename="", option=2):
    """
        this method iterates through general ledger and returns its data

        Parameters
        -----------
        excel_filename: str
            string containing the excel file name for the chart of accounts

        option: int , default = 2
            if option = 1, it means data comes from database and if it is 2 then
            it means data comes from .xlsx file

        Returns
        --------
            ledger_data: list of tuples or DataFrame
                this output contains the account
                if option = 1 then it returns a list of tuples
                if option = 2 then it returns a DataFrame
    """

    if option == 1:
        # db = mysql.connector.connect(
        #     host="localhost",
        #     user="root",
        #     passwd="root",
        #     database="my_database"
        # )
        # mycursor = db.cursor()
        # mycursor.execute("SELECT * FROM general_ledger")
        # ledger_data = mycursor.fetchall()

        ledger_data = [('1.2.1', 7), ('1.2.2', 8), ('1.1', 1), ('1.2.2', 2), ('1.3.1.3', 10), ('1.3.1.3', 6), ('1.3.1.1', 2), ('1.2.1', 4), ('1.2.1', 1), ('1.3.1.3', 6), ('1.2.1', 9), ('1.3.1.3', 10), ('1.3.1.1', 8), ('1.3.1.3', 9), ('1.1', 1), ('1.3.1.1', 4), ('1.2.2', 7), ('1.3.1.3', 7), ('1.2.1', 10), ('1.2.2', 9)]

        return ledger_data
    else:
        ledger_data = pd.read_excel(excel_filename)
        return ledger_data


