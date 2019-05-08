"""
waiter module

"""

import numpy as np


class Waiter:
    """
    Waiter is an object that brings the group drinks and food.

    """

    def __init__(self):
       self.waiters = {1:0, 2:0, 3:0}

    def attend(self, g_id):
       for i in range(1,3):
           if self.waiters[i] == 0:
               print('Waiter {} has begun to attend'.format(i))
               print('On group number {}'.format(g_id))
               self.waiters[i] = g_id
               break

    def end_attend(self, id):
       for i in range(1,3):
           if self.waiters[i] == id:
               print('Waiter {} has ended attending'.format(i))
               self.waiters[i] = 0
               



