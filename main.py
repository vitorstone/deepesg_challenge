"""
Main Function

This script creates a .csv file according to the chart of accounts input and the general ledger input

This script requires that `pandas` and `csv` to be installed within the Python
environment you are running this script in.

"""


import pandas as pd
import csv
from input import get_ledger_data, get_accounts_data

class TreeNode:
    """
     This class represents a TreeNode

     Attributes
     -----------------
     account: str
        a string that holds the account number of the node
     level: int
        an integer that states the level of a certain node within the tree
     value: int
        an integer that holds the value of the node
     children: list
        list that holds all the child nodes of the current node
     parent: TreeNode
        it holds the parent node of a certain node

     Methods
     ----------------
     add_child(child)
        adds a child node to the children list of the current node
     fill_values(dictionary)
        populates all the values of a tree using a dictionary with ledger transactions as input

     extract_data(dic)
        populates a dictionary with all the accounts and its values and returns it

    """

    def __init__(self, account):
        self.account = account
        self.level = len(account.split('.'))
        self.value = 0
        self.children = []
        self.parent = None

    def add_child(self, child):
        """
             this method adds a child node to current node

             Parameters
             -----------
             child: TreeNode

        """
        child.parent = self
        self.children.append(child)

    def fill_values(self, dictionary):
        """
            this method adds a child node to current node. It implements a logic similar to a
            postorder tree traversal.

            Parameters
            --------------
            dictionary: dict
                this dictionary is a result of summing up all the ledger transactions,
                therefore it holds all the leaf nodes' accounts of the tree and its respective
                values already summed up.

        """
        if len(self.children) == 0:
            self.value = dictionary[self.account]
            # self.parent.value += self.value
        else:
            for child in self.children:
                child.fill_values(dictionary)
                self.value += child.value

    def extract_data(self, dic):
        """
            this method populates an empty dictionary with all the accounts and their respective values

            Parameters
            --------------
            dic: dict
                an empty dictionary

         """
        dic[self.account] = self.value
        if self.children:
            for child in self.children:
                child.extract_data(dic)


def build_tree(accounts_data):
    """
        this method iterates through the chart of accounts data and generates a
        tree data structure, in which all the nodes contain the account numbers and
        their respective children, but still leave the node values as default (zero)

        Parameters
        -----------
        accounts_data: DataFrame
            DataFrame containing account numbers

        Returns
        ----------
            it returns the root node of the tree
    """
    root = TreeNode("root")

    # populating the tree
    def evaluate_data(prev, current):
        if prev.level < current.level:
            return prev.add_child(current)
        else:
            evaluate_data(prev.parent, current)

    for i in accounts_data.index:
        myObj = TreeNode(str(accounts_data['account'][i]))

        if myObj.level == 1:
            root.add_child(myObj)
            previous = myObj
        else:
            evaluate_data(previous, myObj)
            previous = myObj

    return root


def calculate_ledger(ledger_data):
    """
        this method iterates through general ledger data and sums up the values of
        all repeated accounts

        Parameters
        -----------
        ledger_data: DataFrame
            DataFrame containing account numbers and their respective total value

        Returns
        --------
            it returns a dictionary containing all the accounts that were in the ledger
            and their respective values
    """

    # generating dictionary
    dictx = {}
    for i in ledger_data.index:
        if str(ledger_data['account'][i]) not in dictx:
            dictx[str(ledger_data['account'][i])] = ledger_data['value'][i]
        else:
            # dict[x['account'][i]] = dict.get(x['account'][i]) + x['value'][i]
            dictx[str(ledger_data['account'][i])] += ledger_data['value'][i]

    return dictx


def create_csv(data):
    """
        this method iterates through a dictionary and then creates a .csv file corresponding to this data.
        The csv file created is the final output of this challenge project.

        Parameters
        ------------
        data: dictionary
            contains all the account numbers and their respective values
    """
    f = open('chart_of_accounts.csv', "w", newline="")
    writer = csv.writer(f)

    for key in data:
        if key != 'root':
            writer.writerow([key, data[key]])
    f.close()


def build_tree_database(accounts_data):
    """
        this method iterates through the chart of accounts data and generates a
        tree data structure, in which all the nodes contain the account numbers and
        their respective children, but still leave the node values as default (zero)

        Parameters
        -----------
        accounts_data: list of tuples
            list of tuples containing account numbers

        Returns
        ----------
            it returns the root node of the tree
    """
    root = TreeNode("root")

    # populating the tree
    def evaluate_data(prev, current):
        if prev.level < current.level:
            return prev.add_child(current)
        else:
            evaluate_data(prev.parent, current)

    for element in accounts_data:
        myObj = TreeNode(str(element[0]))

        if myObj.level == 1:
            root.add_child(myObj)
            previous = myObj
        else:
            evaluate_data(previous, myObj)
            previous = myObj

    return root


def calculate_ledger_database(ledger_data):
    """
        this method iterates through general ledger data and sums up the values of
        all repeated accounts

        Parameters
        -----------
        ledger_data: list of tuples
            list of tuples containing account numbers and their respective total value


        Returns
        --------
            it returns a dictionary containing all the accounts that were in the ledger
            and their respective values
    """

    # generating dictionary
    dictx = {}
    for element in ledger_data:
        if str(element[0]) not in dictx:
            dictx[str(element[0])] = element[1]
        else:
            dictx[str(element[0])] += element[1]

    return dictx


def main():
    """"
        This function creates a .csv file according to the chart of accounts input and the general ledger input

        Important!!
            Need to change the next 3 lines accordingly
            option = 1 -> data will come from relational database. If this option is chosen then the
                          filenames can be left as empty strings
            option = 2 -> data will come from .xlsx files. If this option is chosen then the filenames
                          need to be filled appropriately
    """

    excel_filename_chartofaccounts = 'chart_of_accounts.xlsx'
    excel_filename_generalledger = 'general_ledger.xlsx'
    option = 2

    if option == 2:
        root = build_tree(get_accounts_data(excel_filename_chartofaccounts, option))
        dictx = calculate_ledger(get_ledger_data(excel_filename_generalledger, option))
        root.fill_values(dictx)
        data = {}
        root.extract_data(data)
        create_csv(data)
    else:
        root = build_tree_database(get_accounts_data(excel_filename_chartofaccounts, option))
        dictx = calculate_ledger_database(get_ledger_data(excel_filename_chartofaccounts, option))
        root.fill_values(dictx)
        data = {}
        root.extract_data(data)
        create_csv(data)

main()
