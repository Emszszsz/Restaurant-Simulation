import numpy as np
from buffet import Buffet
from queue import Queue

class BuffetEnd(Buffet, Queue):
    """description of class"""
    def execute(self, obj):
        obj = Buffet()._groups_eating[-1]
        Buffet()._groups_eating = np.delete(Buffet()._groups_eating, -1)
