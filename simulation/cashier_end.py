from cashier import Cashier
from group import Group


class CashierEnd:
    """description of class"""
    @staticmethod
    def execute(cashier, obj):
        print('Cashier {} ends attending on group no. "{}" '.format(cashier._cashier_id, obj.id))
        obj.__del__()
        cashier.attend(0)
