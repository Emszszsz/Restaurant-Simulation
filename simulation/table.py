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
        self._group_eating = 0

    def add(self, g_id):
        self._group_eating = g_id

    def remove(self):
        self._group_eating = 0


class TableBegin:
    """description of class"""
    @staticmethod
    def execute(obj, tables):
        for table in tables:
            if table._group_eating == 0:
                table.add(obj.id)
                break
            else:
                print('No available tables')


class TableEnd:
    """description of class"""
    @staticmethod
    def execute(obj, tables, queue):
        obj.q_type = 3
        queue.enqueue(obj)
        for table in tables:
            if obj.id == table._group_eating:
                table.remove()
                break
