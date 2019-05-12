"""
waiter module

"""
class Waiter:
    """
    Waiter is an object that brings the group drinks and food.

    """

    def __init__(self, id):
        self._waiter_id = id
        self._group_attended_id = 0

    def attend(self, g_id):
        print('Waiter {} starts attending on group no. "{}"'.format(self._waiter_id, g_id))
        self._group_attended_id = g_id

    def end_attend(self):
       self._group_attended_id = 0
               



