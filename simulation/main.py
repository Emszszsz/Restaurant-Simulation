import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from restaurant import Restaurant
from appear import Appear
from buffet_begin import BuffetBegin
from buffet_end import BuffetEnd
from headwaiter_begin import HeadwaiterBegin
from headwaiter_end import HeadwaiterEnd

mean_b = 19
std_b = 1.51
l_d = 0.09
l_f = 1

queues = Queue()
buffet = Buffet()
headwaiter = Headwaiter()
i = 0
while i<4:
    g = Group(i)
    Appear.execute(g, queues)
    if g.q_type == 1:
        BuffetBegin.execute(g, buffet)
        BuffetEnd.execute(g, queues, buffet)
    elif g.q_type == 2:
        HeadwaiterBegin.execute(headwaiter,g,queues)
        HeadwaiterEnd.execute(headwaiter)
    i+=1