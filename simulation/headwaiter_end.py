from headwaiter import Headwaiter

class HeadwaiterEnd(Headwaiter):
    """Changes state of Headwaiter to available"""
    @staticmethod
    def execute(headwaiter):
        print("Headwaiter ends attending")
        headwaiter._group_attended_id = 0

