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
        self.current_table = 0


class HeadwaiterBegin:
    """description of class"""
    @staticmethod
    def execute(headwaiter, queue, table1,
                table2, table3, table4, quant, time):
        max_group = max(quant)
        index_max = quant.index(max_group)
        if table4.group_eating_id == 0:
            print('Headwaiter begins to attend on group no. "{}"'
                  .format(queue._queue[index_max].id))
            headwaiter._group_attended_id = queue._queue[index_max].id
            table4.add(queue._queue.pop(index_max))
            quant.remove(max_group)
            headwaiter.end_attend_time = time + 30

        elif table3.group_eating_id == 0 and max_group <= 3:
            print('Headwaiter begins to attend on group no. "{}"'
                  .format(queue._queue[index_max].id))
            headwaiter._group_attended_id = queue._queue[index_max].id
            table3.add(queue._queue.pop(index_max))
            quant.remove(max_group)
            headwaiter.end_attend_time = time + 30

        elif table2.group_eating_id == 0 and max_group <= 2:
            print('Headwaiter begins to attend on group no. "{}"'
                  .format(queue._queue[index_max].id))
            headwaiter._group_attended_id = queue._queue[index_max].id
            table2.add(queue._queue.pop(index_max))
            quant.remove(max_group)
            headwaiter.end_attend_time = time + 30

        elif table1.group_eating_id == 0 and max_group <= 2:
            print('Headwaiter begins to attend on group no. "{}"'
                  .format(queue._queue[index_max].id))
            headwaiter._group_attended_id = queue._queue[index_max].id
            table1.add(queue._queue.pop(index_max))
            quant.remove(max_group)
            headwaiter.end_attend_time = time + 30


class HeadwaiterEnd:
    """Changes state of Headwaiter to available"""
    @staticmethod
    def execute(headwaiter, tables):
        print("Headwaiter ends attending on group no. {}".
              format(headwaiter._group_attended_id))
        for table in tables:
            if table.group_eating_id == headwaiter._group_attended_id:
                table._group_eating[0].attended = 1
                break
        headwaiter._group_attended_id = 0
