import numpy as np
from waiter import Waiter

class WaiterFoodEnd:
    """description of class"""
    @staticmethod
    def execute(waiter):
        print('Waiter {} ends attending'.format(waiter._waiter_id))
        waiter.end_attend()
        end_dinner = np.random.exponential(0.09,1)

