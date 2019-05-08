"""
tables module
"""
import numpy as np


class Tables:
    """
    One of the two places that group of clients can eat.
    There are tables for: 2, 3 and four people.

    Attributes:
    p - private
        >p table_id - id of the table
        >p group_id - id of the group that is currently
           sitting at that table

    Methods:
        > __init__(self, id, g_id) - initialises a table
        > info(self) - displays info about the table
    """
    def __init__(self, id, g_id):
        self._table_id = id
        self._group_id = g_id

    def info(self):
        if self._group_id != 0:
            print("at the table number {} sits group number {}".
                  format(self._table_id, self._group_id))
        else:
            print("table number {} is empty".format(self._table_id))
