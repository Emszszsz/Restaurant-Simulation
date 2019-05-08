from headwaiter import Headwaiter
from queue import Queue

class HeadwaiterBegin():
    """description of class"""
    @staticmethod
    def execute(headwaiter, obj, queue):
        if len(queue._queue_2) != 0:
            headwaiter._group_attended_id = obj.id
            queue.dequeue(obj)
            end_attend_time = 5

