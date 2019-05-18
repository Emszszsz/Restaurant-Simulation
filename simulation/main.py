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
while R.simulation_time < 20000:
    if R.simulation_time == R.next_appearance_time:
        g = Group(i)
        i += 1

    if g.q_type == 1:
        Appear.execute(g, R.queue_buffet, R)
    if g.q_type == 2:
        Appear.execute(g, R.queue_headwaiter, R)

    for group in R.queue_buffet._queue:
        if R.buffet._seats_free >= group._group_quant and group.attended == 0:
            BuffetBegin.execute(group, R.buffet, R)
    for group in R.buffet.groups_eating:
        if R.simulation_time == group.buffet_end_time:
            BuffetEnd.execute(group, R.queue_cashiers, R.buffet)
    if R.queue_headwaiter._queue and R.headwaiter._group_attended_id == 0:
        HeadwaiterBegin.execute(R.headwaiter, R.queue_headwaiter,
                                R.table_1, R.table_2, R.table_3, R.table_4,
                                R.group_quant, R.simulation_time)
    if (R.simulation_time == R.headwaiter.end_attend_time and
       R.headwaiter._group_attended_id):
        HeadwaiterEnd.execute(R.headwaiter, R.tables)
    for table in R.tables:
        if table.group_eating_id and table._group_eating[0].attended == 1:
            for waiter in R.waiters:
                if waiter._group_attended_id == 0:
                    WaiterDrinkBegin.execute(waiter, table._group_eating[0],
                                             R.simulation_time)
                    break
    for waiter in R.waiters:
        if (R.simulation_time == waiter.end_attend_drink and
           waiter._group_attended_id):
            WaiterDrinkEnd.execute(waiter)
            break
    for table in R.tables:
        if table.group_eating_id and table._group_eating[0].attended == 2:
            for waiter in R.waiters:
                if waiter._group_attended_id == 0:
                    WaiterFoodBegin.execute(waiter, table._group_eating[0],
                                            R.simulation_time)
                    break
    for waiter in R.waiters:
        if (R.simulation_time == waiter.end_attend_food and
           waiter._group_attended_id):
            WaiterFoodEnd.execute(waiter)
            break
    for cashier in R.cashiers:
        if R.queue_cashiers and cashier._group_attended_id == 0:
            CashierBegin.execute(cashier, R.queue_cashiers, R.simulation_time)
            break
    for cashier in R.cashiers:
        if (R.simulation_time == cashier.end_attend_time and
           cashier._group_attended_id):
            CashierEnd.execute(cashier)
            break
    R.simulation_time += 1
