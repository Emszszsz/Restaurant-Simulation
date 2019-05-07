"""
waiter module

"""

import numpy as np


class Waiter:
    """
    Waiter is an object that brings the group drinks and food.

    Attributes:
    p - private
        >p waiter_id - id of the waiter
        >p group_attended_id - id of the group the waiter
           is currently attending on

    Methods:

        > __init__(self, id) - initialises a Waiter object
        > attend(self, g_id) - is activated when a group appears
          at the table and is not attended on yet
        > info(self) - displays information about the waiter
    """

    def __init__(self, id):
        self._waiter_id = id

    def attend(self, g_id):
        self._group_attended_id = g_id

    def info(self):
        if self._group_attended_id != 0:
            print("waiter number {} attends on group number {}".
                  format(self._waiter_id, self._group_attended_id))
        else:
            print("waiter number {} is available".format(self._waiter_id))

"""
Check if the class and it's methods work
"""
w = Waiter(1)
w.attend(1)
w.info()
