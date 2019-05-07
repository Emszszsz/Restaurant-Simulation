"""
cashier module
"""

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
        self._id = id

    def attend(self, g_id):
        self._group_attended_id = g_id

    def info(self):
        if self._group_attended_id != 0:
            print("Cashier number {} attends on group number {}".
                  format(self._id, self._group_attended_id))

"""
Creating and object to see if the class and
it's methods work
"""
c = Cashier(1)
c.attend(1)
c.info()
