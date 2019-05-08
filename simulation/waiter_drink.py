from waiter import Waiter

class WaiterDrink():
    """description of class"""
    @staticmethod
    def execute(waiter,obj):
        print('Drink')
        waiter.attend(obj.id)
        waiter.end_attend(obj.id)