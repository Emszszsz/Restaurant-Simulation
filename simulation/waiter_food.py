import numpy as np
from waiter import Waiter

class WaiterFood():
    """description of class"""
    @staticmethod
    def execute(waiter, obj):
        print('food')
        waiter.attend(obj.id)
        end_dinner = np.random.exponential(1,2)
        waiter.end_attend(obj.id)

