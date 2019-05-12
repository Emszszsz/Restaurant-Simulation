import numpy as np
from cashier import Cashier
from queue import Queue
class CashierBegin():
    """description of class"""
    @staticmethod
    def execute(cashier, obj, queue):
        if len(queue._queue)!= 0:
            queue.dequeue(obj)
            print('Cashier {} attends on group no. "{}"'.format(cashier._cashier_id, obj.id))
            cashier.attend(obj.id)
            end_cashier = np.random.exponential(0.09,1)

