from buffet import Buffet

class BuffetBegin():
    """description of class"""
    @staticmethod
    def execute(obj, buffet):
        if buffet._seats_free >= obj._group_quant:
            buffet.add(obj)
        else:
            print('No available seats for the group')