from headwaiter import Headwaiter
from queue import Queue


class HeadwaiterBegin:
    """description of class"""
    @staticmethod
    def execute(headwaiter, obj, queue):
        if len(queue._queue) != 0:
            print('Headwaiter starts attending on group no. "{}"'.format(obj.id))
            headwaiter._group_attended_id = obj.id
            queue.dequeue(obj)
            end_attend_time = 5

