"""
waiter module

"""
import numpy as np

class Waiter:
    """
    Waiter is an object that brings the group drinks and food.

    """

    def __init__(self, id):
        self._waiter_id = id
        self._group_attended_id = 0
        self.end_attend_drink = 0
        self.end_attend_food = 0
        self.lambda_n = 300
        self.lambda_j = 1700

    def attend_drink(self, g_id):
        print('Waiter {} starts attending (drink)'
              .format(self._waiter_id))
        self._group_attended_id = g_id

    def attend_food(self, g_id):
        print('Waiter {} starts attending (food)'
              .format(self._waiter_id))
        self._group_attended_id = g_id

    def end_attend(self):
        self._group_attended_id = 0


class WaiterDrinkBegin:
    """description of class"""
    @staticmethod
    def execute(waiter, obj, time):
        waiter.attend_drink(obj)
        waiter.end_attend_drink = time + int(np.random.exponential(1/waiter.lambda_n))
        obj.attended = 2


class WaiterDrinkEnd:
    """description of class"""
    @staticmethod
    def execute(waiter):
        print('Waiter {} ends attending (drink)'.format(waiter._waiter_id))
        waiter.end_attend()


class WaiterFoodBegin:
    """description of class"""
    @staticmethod
    def execute(waiter, obj, time):
        waiter.attend_food(obj.id)
        waiter.end_attend_food = time + int(np.random.exponential(1/waiter.lambda_j))
        obj.attended = 3
        obj.dinner_end_time = waiter.end_attend_food + int(np.random.exponential(1/obj.lambda_f))


class WaiterFoodEnd:
    """description of class"""
    @staticmethod
    def execute(waiter):
        print('Waiter {} ends attending (food)'.format(waiter._waiter_id))
        waiter.end_attend()
