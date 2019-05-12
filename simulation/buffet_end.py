from buffet import Buffet
from queue import Queue


class BuffetEnd:
    """description of class"""
    @staticmethod
    def execute(obj, queue, buffet):
        print('Group {} ends at the buffet'.format(obj.id))
        queue.enqueue(obj)
        buffet.groups_eating.remove(obj)