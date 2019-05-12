import numpy as np
from buffet import Buffet


class BuffetBegin:
    """description of class"""
    @staticmethod
    def execute(obj, buffet):
        if buffet._seats_free >= obj._group_quant:
            print("Group {} starts at buffet".format(obj.id))
            buffet.add(obj)
            obj.buffet_end_time = np.random.normal(0, 0.01)
        else:
            print('No available seats for the group')