"""
Headwaiter module
"""
import numpy as np


class Headwaiter:
    """
    Headwaiter is active if the group's attribute '_place_to_eat'<=0.5
    Attributes:
    p - private
        >p group_attended_id - id of the group that the headwaiter is currently
           attending on
    """
    def __init__(self):
        self._group_attended_id = 0
        self.end_attend_time = 0


class HeadwaiterBegin:
    """description of class"""
    @staticmethod
    def execute(headwaiter, queue, tables):
        if queue._queue and headwaiter._group_attended_id == 0:
            for i in queue._queue:
                if i._group_quant == 4:
                    print('Headwaiter begins to attend on group no. "{}"'
                          .format(i.id))
                    headwaiter._group_attended_id = i.id
                    queue._queue.remove(i)
                    headwaiter.end_attend_time = 3
                    break
                elif i._group_quant == 3:
                    print('Headwaiter begins to attend on group no. "{}"'
                          .format(i.id))
                    headwaiter._group_attended_id = i.id
                    queue._queue.remove(i)
                    headwaiter.end_attend_time = 3
                    break
                elif i._group_quant == 2:
                    print('Headwaiter begins to attend on group no. "{}"'
                          .format(i.id))
                    headwaiter._group_attended_id = i.id
                    queue._queue.remove(i)
                    headwaiter.end_attend_time = 3
                    break
                elif i._group_quant == 1:
                    print('Headwaiter begins to attend on group no. "{}"'
                          .format(i.id))
                    headwaiter._group_attended_id = i.id
                    queue._queue.remove(i)
                    headwaiter.end_attend_time = 3
                    break


class HeadwaiterEnd:
    """Changes state of Headwaiter to available"""
    @staticmethod
    def execute(headwaiter, time):
        if headwaiter.end_attend_time == time:
            print("Headwaiter ends attending")
            headwaiter._group_attended_id = 0
