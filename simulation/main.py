import numpy as np
from restaurant import Restaurant
from group import Group
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

R = Restaurant()
i = 1
while i<4:
    g = Group(i)
    if g.q_type == 1:
        Appear.execute(g, R.queue_buffet)
        BuffetBegin.execute(g, R.buffet)
        BuffetEnd.execute(g, R.queue_cashiers, R.buffet)
        for cashier in R.cashiers:
            if cashier._group_attended_id == 0:
                CashierBegin.execute(cashier, g, R.queue_cashiers, g.buffet_end_time)
                CashierEnd.execute(cashier, g)
                break
    elif g.q_type == 2:
        Appear.execute(g, R.queue_headwaiter)
        HeadwaiterBegin.execute(R.headwaiter, g, R.queue_headwaiter)
        TableBegin.execute(g, R.tables)
        HeadwaiterEnd.execute(R.headwaiter)
        for waiter in R.waiters:
            if waiter._group_attended_id == 0:
               WaiterDrinkBegin.execute(waiter, g)
               WaiterDrinkEnd.execute(waiter)
               break
        for waiter in R.waiters:
            if waiter._group_attended_id == 0:
                WaiterFoodBegin.execute(waiter, g)
                WaiterFoodEnd.execute(waiter)
                break
        TableEnd.execute(g, R.tables, R.queue_cashiers)
        for cashier in R.cashiers:
            if cashier._group_attended_id == 0:
                CashierBegin.execute(cashier, g, R.queue_cashiers, g.table_end_time)
                CashierEnd.execute(cashier, g)
                break
        
        
    i+=1