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
    
    def begin(self, queue, tables, groups, time, stat):
        for table in tables:
            if table.group_eating_id == 0 and self.current_table == 0:
                self.current_table = table._table_id
                break
            if table._table_id == self.current_table:
                for i in groups:
                    if table._table_quant == i._group_quant:
                        table.group_eating_id = i.id
                        groups.remove(i)
                        self._group_attended_id = table.group_eating_id
                        for group in queue._queue:
                            if group.id == table.group_eating_id:
                                print('Headwaiter attends on group no. {}'.
                                      format(group.id))
                                stat.wait_time_headwaiter.append(time - group.appearance_time)
                                self.end_attend_time = time + 30
                                queue._queue.remove(group)
                                group.end_attend_headwaiter = self.end_attend_time
                                table._group_eating = group
                                break

    def end(self, tables):
       for table in tables:
           if table._group_eating.id == self._group_attended_id:
               table._group_eating.attended = 1
       print("Headwaiter ends attending on group no. {}".
             format(self._group_attended_id))
       self._group_attended_id = 0
       self.current_table = 0
       self.end_attend_time = 0
    
    @staticmethod
    def sort(list):
        for i in range(len(list)):
            j = len(list)-1
            while j>i:
                if list[j]._group_quant <list[j-1]._group_quant:
                     tmp = list[j]
                     list[j] = list[j-1]
                     list[j-1] = tmp
                j -= 1
        return list
