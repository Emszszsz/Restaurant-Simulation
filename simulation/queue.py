"""
queues module
"""

import numpy as np


class Queue:
    """
    Attributes:
    >p type - queue type:
              1 - queue to the buffet
              2 - queue to the headwaiter
              3 - queue to the cashiers
    """


    def enqueue(self, obj):
        self._queue_1 = np.array([], dtype=object)
        self._queue_2 = np.array([], dtype=object)
        self._queue_3 = np.array([], dtype=object)
        if getattr(obj, 'q_type') == 1:
            self._queue_1 = np.insert(self._queue_1, 0, obj)
        elif getattr(obj, 'q_type') == 2:
            self._queue_2 = np.insert(self._queue_2, 0, obj)
        elif getattr(obj, 'q_type') == 3:
            self._queue_3 = np.insert(self._queue_3, 0, obj)
        else:
            print("Type of client doesn't match the type of queue")

    def dequeue(self, obj):
        if getattr(obj, 'q_type') == 1:
            obj = self._queue_1[-1]
            self._queue_1 = np.delete(self._queue_1, -1)
            print("Group {} leaves the queue".format(obj._id))
            return obj
        elif getattr(obj, 'q_type') == 2:
            obj = self._queue_2[-1]
            self._queue_2 = np.delete(self._queue_2, -1)
            print("Group {} leaves the queue".format(obj._id))
            return obj
        else:
            print("Type of client doesn't match the type of queue")

    def info(self):
        print("Queue to the buffet contains {} group(s)".
              format(np.shape(self._queue_1)[0]))
        print("Queue to the headwaiter contains {} group(s)".
              format(np.shape(self._queue_2)[0]))
