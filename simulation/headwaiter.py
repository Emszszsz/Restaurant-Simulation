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
    def __init__(self, group_id):
        self._group_attended_id = group_id

    def is_available(self, id):
        if id != 0:
            return False
        else:
            return True

    def info(self):
        if self._group_attended_id == 0:
            print("Headwaiter doesn't attend on any group")
        else:
            print("Headwaiter attends on group {} ".
                  format(self._group_attended_id))
