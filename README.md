# Solution Overview

There are two main .py files on this project: input.py and main.py 

## input.py
this is where the input of the system is handled. I coded it in such a way that it accepts two types of inputs: 
- chart of accounts and general ledger coming from a relational data base 
- chart of accounts and general ledger coming from a .xls file
The choice is made by a variable called ```option```, which is harded coded in the main.py file. If ```option = 1``` that means that the data comes from a database. If ```option = 2``` it means that the data comes from a .xlsx file.
The code is very simple and it goes as follows:

We first need to import pandas for .xlsx handling and also mysql.connector if we want to retrieve data from a database
```
import mysql.connector
import pandas as pd
```
Then, we define a function that will handle the data based on the chosen option. if ```option = 1 ``` it returns the data in the format of a list of tuples. For example:
```
 [('1',), ('1.1',), ('1.2',), ... ,  ('1.3.1.1',), ('1.3.1.3',)]
```

If ```option = 2``` it returns the data in the format of a DataFrame
```
def get_accounts_data(excel_filename="", option=2):
    if option == 1:
        
        #  ..............................................................
        #  ... part of the code that deals with connecting to database...
        #  ..............................................................

        # dummy data replicating type of data that will come from database (list of tuples)
        accounts_data = [('1',), ('1.1',), ('1.2',), ('1.2.1',), ('1.2.2',), ('1.3',), ('1.3.1',), ('1.3.1.1',), ('1.3.1.3',)]
        return accounts_data

    else:
        # reading account numbers from excel file
        try:
            accounts_data = pd.read_excel(excel_filename)
        except OSError:
            print('Could not read/open file', excel_filename)
        else:
            return accounts_data
 ```
 Then, the next function deals with getting the transaction data from the ledger. It follows the same logic as the last function.
 ```

def get_ledger_data(excel_filename="", option=2):
    if option == 1:
       
        #  ..............................................................
        #  ... part of the code that deals with connecting to database...
        #  ..............................................................
        
        # dummy data replicating type of data that will come from database (list of tuples)
        ledger_data = [('1.2.1', 7), ('1.2.2', 8), ('1.1', 1), ('1.2.2', 2), ('1.3.1.3', 10), ('1.3.1.3', 6), ('1.3.1.1', 2), ('1.2.1', 4), ('1.2.1', 1), ('1.3.1.3', 6), ('1.2.1', 9), ('1.3.1.3', 10), ('1.3.1.1', 8), ('1.3.1.3', 9), ('1.1', 1), ('1.3.1.1', 4), ('1.2.2', 7), ('1.3.1.3', 7), ('1.2.1', 10), ('1.2.2', 9)]

        return ledger_data

    else:
        try:
            ledger_data = pd.read_excel(excel_filename)
        except OSError:
            print('Could not read/open file', excel_filename)
        else:
            return ledger_data

```

## main.py
  
this is where we use the data that comes from input.py and use it to create a .csv file containing all of the account numbers followed by its respective value. I chose a .csv file because it can easily be used in other processing pipes, even if it's to create another excel file or to create a table within a database from it.

the code goes as follows:

```
import csv
from input import get_ledger_data, get_accounts_data
```
The TreeNode class has 5 attributes that are really self-explanatory, and also 3 methods.

1) the add_child method adds a child for a current node
2) fill_values is a method used in the root node that is supposed to be called once the entire tree structure is set up and it basically sums up all the values and put them in their respective account number
3) extract_data is also a method used in the root node that gathers all the tree information and puts it in a dictionary

```
class TreeNode:
    def __init__(self, account):
        self.account = account
        self.level = len(account.split('.'))
        self.value = 0
        self.children = []
        self.parent = None
    
    def add_child(self, child):
               .
               .
               
    def fill_values(self, dictionary):
               .
               .
               
    def extract_data(self, dic):
               .
               .
    
```
Now we have the build_tree function, that is used in the root node, and also uses the accounts_data from input.py as argument. This function populates the entire tree, and it does that by setting the account attribute of each node to the account number corresponding.
```
def build_tree(accounts_data):
              .
              .
```
Then we have the calculate_ledger function, which takes in the ledger_data coming from input.py and it sums up all the repeated values and stores all of the account numbers and their values in a dictionary. Then it returns this dictionary
```
def calculate_ledger(ledger_data)
            .
            .
    return dictx
```

Then we have the create_csv function that gets the dictionary coming from the extract_data method of TreeNode class and it turns that into the final output in .csv format

```
def create_csv(data):
          .
          .
```
Next we have two other methods that work exactly as the build_tree and calculate_ledger methods, however they handle inputs coming from a relational database instead (option = 1)

```
def build_tree_database(accounts_data):
          .
          .
def calculate_ledger_database(ledger_data):
          .
          .
```

Now we have the main function that puts it all together, based on the option chosen:

```
def main():

  excel_filename_chartofaccounts = 'chart_of_accounts.xlsx'
  excel_filename_generalledger = 'general_ledger.xlsx'
  option = 2
  
```
Now we have an if statement handling the input when option = 2. Looking at the snippet below, we first build the tree based on the accounts_data coming from input.py and also on the fact that option = 2. Then, we calculate dictx, which is a dictionary containing the ledger transactions already summed up. Then, we call fill_values(dictx) on the root node, which is basically going to populate all the tree nodes with their respective values. Then, we call extract_data(data) on the root node, which will gather all the information and store it in the dictionary called data. Finally we call create_csv(data) and this generates a .csv file with all the info needed. 
```
  if option == 2:
    root = build_tree(get_accounts_data(excel_filename_chartofaccounts, option))
    dictx = calculate_ledger(get_ledger_data(excel_filename_generalledger, option))
    root.fill_values(dictx)
    data = {}
    root.extract_data(data)
    create_csv(data)
```
Of course we also have an else part but it is pretty much the same thing but instead of calling build_tree and calculate_ledger, it calls build_tree_database and calculate_ledger_database
```
    else:
        root = build_tree_database(get_accounts_data(excel_filename_chartofaccounts, option))
        dictx = calculate_ledger_database(get_ledger_data(excel_filename_chartofaccounts, option))
                                          .
                                          .
```

Finally, we call main() and the .csv file is created.

# Running the program in Linux environment 

1) Navigate the terminal to the directory where the script is located using the ```cd``` command.
2) Type ```python main.py```
3) A file named chart_of_accounts.csv should appear on the same folder. This file is the final desired output

# test_results.py
This file contains two tests, one for each option. 
- The first test uses as an input two excel files. They are named chart_of_accounts.test.xlsx and general_ledger_test.xlsx. I wrote them to be exactly like the given example on the deepesg/data_challenge repository. 
- The second tests uses as an input two lists of tuples (simulating an output coming from a relational database), I also hardcoded them to be exactly like the last case, but with different format, as already stated.


# Running the test in Linux environment

1) Navigate the terminal to the directory where the script is located using the ```cd``` command.
2) Type ```python -m unittest test_results.py```
3) You should see on the terminal that 2 tests were ran and an 'OK' message
