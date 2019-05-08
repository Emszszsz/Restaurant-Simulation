from tables import Tables
from queue import Queue

class TableEnd():
    """description of class"""
    @staticmethod
    def execute(obj, tables, queue):
        obj.q_type = 3
        queue.enqueue(obj)
        tables.remove(obj)


