import numpy as np
from restaurant import Restaurant
from group import Group
from appear import Appear
from buffet import *
from headwaiter import *
from waiter import *
from table import *
from cashier import *

R = Restaurant()
i = 1

while R.simulation_time < 10:

    if R.simulation_time == R.next_appearance_time:
        g = Group(i)
        i += 1
        print('Time: {}'.format(R.simulation_time))
        if g.q_type == 1:

            Appear.execute(g, R.queue_buffet, R)
            BuffetBegin.execute(g, R.buffet)
            BuffetEnd.execute(g, R.queue_cashiers, R.buffet, 2)

        elif g.q_type == 2:

            Appear.execute(g, R.queue_headwaiter, R)
            HeadwaiterBegin.execute(R.headwaiter, R.queue_headwaiter, R.tables)
            TableBegin.execute(g, R.tables)
            HeadwaiterEnd.execute(R.headwaiter, 3)

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
                CashierBegin.execute(cashier, R.queue_cashiers)
                CashierEnd.execute(cashier)
                break

    else:
        R.simulation_time += 1
