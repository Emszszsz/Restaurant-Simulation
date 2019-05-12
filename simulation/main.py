import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from restaurant import Restaurant
from tables import Tables
from waiter import Waiter
from cashier import Cashier
from appear import Appear
from buffet_begin import BuffetBegin
from buffet_end import BuffetEnd
from headwaiter_begin import HeadwaiterBegin
from headwaiter_end import HeadwaiterEnd
from table_begin import TableBegin
from table_end import TableEnd
from waiter_drink_begin import WaiterDrinkBegin
from waiter_drink_end import WaiterDrinkEnd
from waiter_food_begin import WaiterFoodBegin
from waiter_food_end import WaiterFoodEnd
from cashier_begin import CashierBegin
from cashier_end import CashierEnd

queue_buffet = Queue()
queue_headwaiter = Queue()
queue_cashiers = Queue()
buffet = Buffet()
headwaiter = Headwaiter()
tables = Tables()
waiter_1 = Waiter(1)
waiter_2 = Waiter(2)
waiter_3 = Waiter(3)
cashier_1 = Cashier(1)
cashier_2 = Cashier(2)
waiters = [waiter_1, waiter_2, waiter_3]
cashiers = [cashier_1, cashier_2]
i = 1
while i<4:
    g = Group(i)
    if g.q_type == 1:
        Appear.execute(g, queue_buffet)
        BuffetBegin.execute(g, buffet)
        BuffetEnd.execute(g, queue_cashiers, buffet)
        for cashier in cashiers:
            if cashier._group_attended_id == 0:
                CashierBegin.execute(cashier, g, queue_cashiers)
                CashierEnd.execute(cashier, g)
                break
    elif g.q_type == 2:
        Appear.execute(g, queue_headwaiter)
        HeadwaiterBegin.execute(headwaiter, g, queue_headwaiter)
        TableBegin.execute(g, tables)
        HeadwaiterEnd.execute(headwaiter)
        for waiter in waiters:
            if waiter._group_attended_id == 0:
               WaiterDrinkBegin.execute(waiter, g)
               WaiterDrinkEnd.execute(waiter)
               break
        for waiter in waiters:
            if waiter._group_attended_id == 0:
                WaiterFoodBegin.execute(waiter, g)
                WaiterFoodEnd.execute(waiter)
                break
        TableEnd.execute(g, tables, queue_cashiers)
        for cashier in cashiers:
            if cashier._group_attended_id == 0:
                CashierBegin.execute(cashier, g, queue_cashiers)
                CashierEnd.execute(cashier, g)
                break
        
        
    i+=1