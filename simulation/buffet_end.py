import numpy as np
from buffet import Buffet
from queue import Queue

class BuffetEnd():
    """description of class"""
    @staticmethod
    def execute(obj, queue, buffet):
        obj.q_type = 3
        queue.enqueue(obj)
        buffet.groups_eating.remove(obj)