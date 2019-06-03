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
        self._group_attended_id = 0
        self.end_attend_time = 0
        self.lambda_p = 200

    def attend(self, g_id):
        self._group_attended_id = g_id

    def begin(self, queue, time):
        if queue._queue:
            self._group_attended_id = queue._queue[len(queue._queue)-1].id
            queue._queue.pop()
            self.end_attend_time = time + int(np.random.exponential(self.lambda_p))
            print('Cashier {} starts to attend on group no. {}'.
                  format(self._id, self._group_attended_id))

    def end(self):
        print('Cashier {} ends'.format(self._id))
        self._group_attended_id = 0

