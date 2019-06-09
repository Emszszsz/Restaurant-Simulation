"""
Restaurant module
"""
import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from table import Table
from waiter import Waiter
from cashier import Cashier


class Restaurant:
    """
    Restaurant stores all the data that the other classes need

    """
    def __init__(self):
        self.simulation_time = 0
        self.number_of_groups = 0
        self.queue_buffet = Queue()
        self.queue_headwaiter = Queue()
        self.queue_cashiers = Queue()
        self.buffet = Buffet()
        self.headwaiter = Headwaiter()
        self.waiters = [Waiter(i+1) for i in range(7)]
        self.tables_2 = [Table(i+1, 2) for i in range(4)]
        self.tables_3 = [Table(i+1, 3) for i in range(4, 14)]
        self.tables_4 = [Table(i+1, 4) for i in range(14, 18)]
        self.all_tables = self.tables_2 + self.tables_3 + self.tables_4
        self.cashiers = [Cashier(i+1) for i in range(4)]
        self.groups = []
        self.next_appearance_time = 0
