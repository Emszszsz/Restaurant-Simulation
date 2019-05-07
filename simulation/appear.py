import numpy as np
from queue import Queue

class Appear(Queue):
    """class that manages the appearance of the clients in the system"""
    def __init__(self):
        self.mean_a = 34
        self.std_a = 2.14

    def execute(self, obj):
        """Adds group to the queue and plans next appearance"""
        Queue().enqueue(obj)
        appearance_time = abs(np.random.normal(self.mean_a, self.std_a))



