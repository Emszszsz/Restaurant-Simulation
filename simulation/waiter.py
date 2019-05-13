"""
waiter module

"""


class Waiter:
    """
    Waiter is an object that brings the group drinks and food.

    """

    def __init__(self, id):
        self._waiter_id = id
        self._group_attended_id = 0

    def attend(self, g_id):
        print('Waiter {} starts attending on group no. "{}"'
              .format(self._waiter_id, g_id))
        self._group_attended_id = g_id

    def end_attend(self):
        self._group_attended_id = 0


import numpy as np
from waiter import Waiter


class WaiterDrinkBegin:
    """description of class"""
    @staticmethod
    def execute(waiter, obj):
        print('Drink')
        waiter.attend(obj.id)


class WaiterDrinkEnd:
    """description of class"""
    @staticmethod
    def execute(waiter):
        print('Waiter {} ends attending'.format(waiter._waiter_id))
        waiter.end_attend()


class WaiterFoodBegin:
    """description of class"""
    @staticmethod
    def execute(waiter, obj):
        print('food')
        waiter.attend(obj.id)


class WaiterFoodEnd:
    """description of class"""
    @staticmethod
    def execute(waiter):
        print('Waiter {} ends attending'.format(waiter._waiter_id))
        waiter.end_attend()
        end_dinner = np.random.exponential(0.09, 1)