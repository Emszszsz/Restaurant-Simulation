"""
    Buffet module
"""

import numpy as np


class Buffet:
    """
    Buffet is one of two places where clients can eat
    p - private
    Attributes:
               >p groups eating - identification numbers of the
                   groups that are currently eating at the buffet
               >p all_seats - all the seats that buffet has
               >p seats_free - number of seats that are
                   currently free
    Methods:
               >__init__(self, seats) - initialises an object
               >add(self, obj) - adds a client(obj) to the buffet if there are
                   enough seats
               >info - displays the information about current state
                   of the buffet

    """

    def __init__(self):
        seats = 12
        self.groups_eating = []
        self._all_seats = seats
        self._seats_free = seats

    def add(self, obj):
        self.groups_eating.append(obj)
        self._seats_free = self._all_seats - obj._group_quant

    def info(self):
        print("Number of groups currently eating at the buffet: {}".
              format(np.shape(self.groups_eating)[0]))
        print("Number of free seats at the buffet: {}".
              format(self._seats_free))
