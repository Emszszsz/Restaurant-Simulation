"""
tables module
"""
import numpy as np


class Tables:
    """
    One of the two places that group of clients can eat.
    There are tables for: 2, 3 and four people.

    """
    def __init__(self):
        self._table_id = {1:2, 2:2, 3:3, 4:3, 5:4}


    def add(self, obj):
        self._groups = []
        for i in range(1,6):
            if self._table_id[i] >= obj._group_quant:
                self._groups.append(obj)

    def remove(self, obj):
       self._groups.remove(obj)
