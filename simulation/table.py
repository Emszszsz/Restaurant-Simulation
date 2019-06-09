"""
tables module
"""
import numpy as np
from group import Group


class Table:
    """
    One of the two places that group of clients can eat.
    There are tables for: 2, 3 and four people.

    """
    def __init__(self, id, quant):
        self._table_id = id
        self._table_quant = quant
        self._group_eating = Group(0)
        self.group_eating_id = 0

    def add(self, obj):
        self._group_eating = obj
        self.group_eating_id = obj.id

    def remove(self):
        self.group_eating_id = 0
        self._group_eating = 0

    def end(self, queue):
        queue._queue.append(self._group_eating)
        self._group_eating = Group(0)
        self.group_eating_id = 0
        

