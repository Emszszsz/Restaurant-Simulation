import numpy as np


class Cashier:
    """

    In the restaurant there are multiple cashiers.
    Cashier is the last object that group of clients interacts with.
    p - private
    Attributes:
        >p id - cashier's identification number
        >p group_attended_id - identification number of the group
        that the cashier currently attends on. If it's value == 1
        cashier position is considered available for the first
        group in the queue

    """

    def __init__(self, id):
        self._cashier_id = id
        self._group_attended_id = 0

    def attend(self, g_id):
        self._group_attended_id = g_id


class CashierBegin:
    """description of class"""
    @staticmethod
    def execute(cashier, queue):
        if queue._queue:
            print('Cashier {} starts'.format(cashier._cashier_id))
            queue.dequeue()
            end_cashier = np.random.exponential(0.09, 1)


class CashierEnd(CashierBegin):
    """description of class"""
    @staticmethod
    def execute(cashier):
        print('Cashier {} ends'.format(cashier._cashier_id))
        cashier.attend(0)
