import numpy as np
from queue import Queue


class Appear:
    """class that manages the appearance of the clients in the system"""
    @staticmethod 
    def execute(obj, queue):
        """Adds group to the queue and plans next appearance"""
        mean_a = 34
        std_a = 2.14
        queue.enqueue(obj)
        appearance_time = abs(np.random.normal(mean_a, std_a))



