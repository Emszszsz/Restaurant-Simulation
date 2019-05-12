from waiter import Waiter

class WaiterDrinkBegin:
    """description of class"""
    @staticmethod
    def execute(waiter,obj):
        print('Drink')
        waiter.attend(obj.id)