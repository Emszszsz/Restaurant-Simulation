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
        self.end_attend_time = 0
        self.lambda_p = 200

    def attend(self, g_id):
        self._group_attended_id = g_id


class CashierBegin:
    """description of class"""
    @staticmethod
    def execute(cashier, queue, time):
        if queue._queue:
            print('Cashier {} starts'.format(cashier._cashier_id))
            cashier._group_attended_id = queue._queue[len(queue._queue)-1].id
            queue.dequeue()
            cashier.end_attend_time = time + int(np.random.exponential(cashier.lambda_p))


class CashierEnd():
    """description of class"""
    @staticmethod
    def execute(cashier):
        print('Cashier {} ends'.format(cashier._cashier_id))
        cashier._group_attended_id = 0
