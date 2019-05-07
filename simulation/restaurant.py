"""
Restaurant module
"""
import numpy as np
from queue import Queue


class Restaurant:
    """
    Restaurant stores all the data that the other classes need
    Attributes:
    p - private
        >p table_for_two - number of tables for two people
        >p table_for_three - number of tables for three people
        >p table_for_four - number of tables for four people
        >p buffet_seats - number of seats at the buffet
        >p waiters - number of waiters
        >p cashiers - number of cashiers
        >p headwaiter - number of headwaiters
        >p waiters_id - table containing ids of all the waiters
        >p cashiers_id - table containing ids of all the cashiers
        >p tables_for_two_ids - table containing ids of all the tables for two
        >p tables_for_three_ids - table containing ids of all the tables
           for three
        >p tables_for_four_ids - table containing ids of all the tables
           for four
        >p queue_buffet - object of the queue type containing groups
           that will eat at the buffet
        >p queue_headwaiter - object of the queue type containing groups
           that will eat at the table
    """
    def __init__(self):
        self._table_for_two = 5
        self._table_for_three = 6
        self._table_for_four = 3
        self._buffet_seats = 15
        self._waiters = 5
        self._cashiers = 5
        self._headwaiter = 1
        self._waiters_ids = [1, 2, 3, 4, 5]
        self._cashiers_ids = [1, 2, 3, 4, 5]
        self._tables_for_two_ids = [1, 2, 3, 4, 5]
        self._tables_for_three_ids = [1, 2, 3, 4, 5, 6]
        self._tables_for_four_ids = [1, 2, 3]
        self._queue_buffet = Queue(1)
        self._queue_headwaiter = Queue(2)
        self._queue_cashiers = Queue(3)

    def info(self):
        print("Restaurant has:")
        print("{} tables for two".format(self._table_for_two))
        print("{} tables for three".format(self._table_for_three))
        print("{} tables for four".format(self._table_for_four))
        print("{} seats at the buffet".format(self._buffet_seats))
        print("{} waiters".format(self._waiters))
        print("{} cashiers".format(self._cashiers))
