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
    def __init__(self):
        self._queue_1 = []
        self._queue_2 = []
        self._queue_3 = []

    def enqueue(self, obj):
        if getattr(obj, 'q_type') == 1:
            self._queue_1.append(obj)
        elif getattr(obj, 'q_type') == 2:
            self._queue_2.append(obj)
        elif getattr(obj, 'q_type') == 3:
            self._queue_3.append(obj)
            print("Type of client doesn't match the type of queue")

    def dequeue(self, obj):
        if getattr(obj, 'q_type') == 1:
            self._queue_1.remove(obj)
            print("Group {} leaves the queue".format(obj._id))
        elif getattr(obj, 'q_type') == 2:
            self._queue_2.remove(obj)
            print("Group {} leaves the queue".format(obj._id))
        elif getattr(obj, 'q_type') == 3:
            self._queue_3.remove(obj)
        else:
            print("Type of client doesn't match the type of queue")


