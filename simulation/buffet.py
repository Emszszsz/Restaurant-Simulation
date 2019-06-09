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
        seats = 14
        self.groups_eating = []
        self._all_seats = seats
        self._seats_free = seats
        self.mean_b = 3200
        self.std_b = 100

    def add(self, obj):
        self.groups_eating.append(obj)
        self._seats_free = self._all_seats - obj._group_quant

    def begin(self, obj, restaurant):
        print("Group {} starts at buffet".format(obj.id))
        restaurant.queue_buffet._queue.remove(obj)
        self.add(obj)
        obj.attended = 1
        obj.buffet_end_time = restaurant.simulation_time + abs(
            int(np.random.normal(self.mean_b, self.std_b)))

    def end(self, obj, queue):
        print('Group {} ends at the buffet'.format(obj.id))
        queue._queue.append(obj)
        self.groups_eating.remove(obj)
        self._seats_free += obj._group_quant