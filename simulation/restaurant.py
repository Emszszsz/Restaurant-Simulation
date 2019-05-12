"""
Restaurant module
"""
import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from tables import Tables
from waiter import Waiter
from cashier import Cashier


class Restaurant:
    """
    Restaurant stores all the data that the other classes need

    """
    def __init__(self):
       self.queue_buffet = Queue()
       self.queue_headwaiter = Queue()
       self.queue_cashiers = Queue()
       self.buffet = Buffet()
       self.headwaiter = Headwaiter()
       self.tables = Tables()
       self.waiter_1 = Waiter(1)
       self.waiter_2 = Waiter(2)
       self.waiter_3 = Waiter(3)
       self.cashier_1 = Cashier(1)
       self.cashier_2 = Cashier(2)
       self.waiters = [self.waiter_1, self.waiter_2, self.waiter_3]
       self.cashiers = [self.cashier_1, self.cashier_2]

