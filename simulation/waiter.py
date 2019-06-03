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

    def drink_begin(self, time, table, stat):
        if table._group_eating.attended == 1:
            print('Waiter {} starts attending on group no. {} (drink)'.
                  format(self._waiter_id, table._group_eating.id))
            self._group_attended_id = table._group_eating.id
            self.end_attend_drink = time + int(np.random.exponential(self.lambda_n))
            table._group_eating.attended = 2
            stat.wait_time_waiter.append(time - table._group_eating.end_attend_headwaiter)

    def drink_end(self):
        if self._group_attended_id:
            print('Waiter {} ends attending (drink)'.format(self._waiter_id))
            self._group_attended_id = 0

    def food_begin(self, time, table):
        if table._group_eating.attended == 2:
            print('Waiter {} starts attending on group no. {} (food)'.
                  format(self._waiter_id, table._group_eating.id))
            self._group_attended_id = table._group_eating.id
            self.end_attend_food = time + int(np.random.exponential(self.lambda_j))
            table._group_eating.attended = 3
            table._group_eating.dinner_end_time = self.end_attend_food + int(np.random.exponential(table._group_eating.lambda_f))

    def food_end(self):
        if self._group_attended_id:
            print('Waiter {} ends attending (food)'.format(self._waiter_id))
            self._group_attended_id = 0
