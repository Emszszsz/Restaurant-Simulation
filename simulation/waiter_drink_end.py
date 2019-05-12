from waiter import Waiter
class WaiterDrinkEnd():
    """description of class"""
    @staticmethod
    def execute(waiter):
        print('Waiter {} ends attending'.format(waiter._waiter_id))
        waiter.end_attend()

