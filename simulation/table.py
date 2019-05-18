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
        self._group_eating = []
        self.group_eating_id = 0
        self.end_dinner = 0

    def add(self, obj):
        self._group_eating.insert(0, obj)
        self.group_eating_id = obj.id

    def remove(self, obj):
        self.group_eating_id = 0
        self._group_eating.pop()


class TableEnd:
    """description of class"""
    @staticmethod
    def execute(table, queue):
        queue.enqueue(table.group_eating[0])
        table.remove()
