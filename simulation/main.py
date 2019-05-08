import numpy as np
from group import Group
from headwaiter import Headwaiter
from buffet import Buffet
from queue import Queue
from restaurant import Restaurant
from appear import Appear
from buffet_end import BuffetEnd
from headwaiter_end import HeadwaiterEnd
from buffet_begin import BuffetBegin

mean_b = 19
std_b = 1.51
l_d = 0.09
l_f = 1

queues = Queue()
buffet = Buffet()

g = Group(1)
Appear.execute(g, queues)
BuffetBegin.execute(g, buffet)