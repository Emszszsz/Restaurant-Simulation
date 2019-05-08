import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from restaurant import Restaurant
from tables import Tables
from waiter import Waiter
from appear import Appear
from buffet_begin import BuffetBegin
from buffet_end import BuffetEnd
from headwaiter_begin import HeadwaiterBegin
from headwaiter_end import HeadwaiterEnd
from table_begin import TableBegin
from table_end import TableEnd
from waiter_drink import WaiterDrink
from waiter_food import WaiterFood


queues = Queue()
buffet = Buffet()
headwaiter = Headwaiter()
tables = Tables()
waiters = Waiter()
i = 1
while i<4:
    g = Group(i)
    Appear.execute(g, queues)
    if g.q_type == 1:
        BuffetBegin.execute(g, buffet)
        BuffetEnd.execute(g, queues, buffet)
    elif g.q_type == 2:
        HeadwaiterBegin.execute(headwaiter, g, queues)
        TableBegin.execute(g, tables)
        HeadwaiterEnd.execute(headwaiter)
        WaiterDrink.execute(waiters, g)
        WaiterFood.execute(waiters, g)
        TableEnd.execute(g, tables, queues)
    i+=1