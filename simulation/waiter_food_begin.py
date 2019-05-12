from waiter import Waiter

class WaiterFoodBegin():
    """description of class"""
    @staticmethod
    def execute(waiter, obj):
        print('food')
        waiter.attend(obj.id)

