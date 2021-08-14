import unittest
from main import *
import pandas as pd
from input import get_ledger_data, get_accounts_data


class TestOptions(unittest.TestCase):

    # testing final data assuming that initial input comes from .xlsx files
    def test_option2(self):
        root = build_tree(get_accounts_data('chart_of_accounts_test.xlsx', 2))
        dictx = calculate_ledger(get_ledger_data('ledger_test.xlsx', 2))
        root.fill_values(dictx)
        data = {}
        root.extract_data(data)
        self.assertEqual(data,
                         {'root': 121, '1': 121, '1.1': 2, '1.2': 57, '1.2.1': 31, '1.2.2': 26, '1.3': 62, '1.3.1': 62,
                          '1.3.1.1': 14, '1.3.1.3': 48})

    # testing final data assuming that initial input comes from a relational database
    # (in this case the data comes as a list of tuples, instead of a DataFrame)
    def test_option1(self):
        accounts_data = [('1',), ('1.1',), ('1.2',), ('1.2.1',), ('1.2.2',), ('1.3',), ('1.3.1',), ('1.3.1.1',),
                         ('1.3.1.3',)]
        ledger_data = [('1.2.1', 7), ('1.2.2', 8), ('1.1', 1), ('1.2.2', 2), ('1.3.1.3', 10), ('1.3.1.3', 6),
                       ('1.3.1.1', 2), ('1.2.1', 4), ('1.2.1', 1), ('1.3.1.3', 6), ('1.2.1', 9), ('1.3.1.3', 10),
                       ('1.3.1.1', 8), ('1.3.1.3', 9), ('1.1', 1), ('1.3.1.1', 4), ('1.2.2', 7), ('1.3.1.3', 7),
                       ('1.2.1', 10), ('1.2.2', 9)]

        root = build_tree_database(accounts_data)
        dictx = calculate_ledger_database(ledger_data)
        root.fill_values(dictx)
        data = {}
        root.extract_data(data)
        self.assertEqual(data,
                         {'root': 121, '1': 121, '1.1': 2, '1.2': 57, '1.2.1': 31, '1.2.2': 26, '1.3': 62, '1.3.1': 62,
                          '1.3.1.1': 14, '1.3.1.3': 48})


