from headwaiter import Headwaiter

class HeadwaiterEnd(Headwaiter):
    """Changes state of Headwaiter to available"""
    def execute(self):
        Headwaiter().is_available(0)

