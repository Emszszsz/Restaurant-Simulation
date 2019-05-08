from headwaiter import Headwaiter

class HeadwaiterEnd(Headwaiter):
    """Changes state of Headwaiter to available"""
    @staticmethod
    def execute(headwaiter):
        headwaiter.is_available(0)

