import numpy as np
from restaurant import Restaurant
from stats import Stats
from group import Group
from appear import Appear
from buffet import *
from headwaiter import *
from waiter import *
from table import *
from cashier import *

R = Restaurant()
Stat = Stats()
i = 1

x = input('Ending 1(time) or 2(number of groups)? 1/2')

if x == '1':
    while R.simulation_time < 36000:
            if R.simulation_time == R.next_appearance_time:
                g = Group(i)
                g.appearance_time = R.simulation_time
                i += 1
                if g.q_type == 1:
                    Appear.execute(g, R.queue_buffet, R)
                if g.q_type == 2:
                    Appear.execute(g, R.queue_headwaiter, R)
                    Stat.queue_tables.append(len(R.queue_headwaiter._queue))
                    Stat.groups_appearance_time.append(g.appearance_time)

            for group in R.buffet.groups_eating:
                if group.buffet_end_time == R.simulation_time:
                    R.buffet.end(group, R.queue_cashiers)

            if  R.simulation_time == R.headwaiter.end_attend_time != 0:
                R.headwaiter.end(R.all_tables)

            for waiter in R.waiters:
                if waiter.end_attend_drink == R.simulation_time != 0:
                    waiter.drink_end()

            for waiter in R.waiters:
                if waiter.end_attend_food == R.simulation_time != 0:
                    waiter.food_end()

            for cashier in R.cashiers:
                if cashier.end_attend_time == R.simulation_time != 0:
                    cashier.end()

            for group in R.queue_buffet._queue:
                if R.buffet._seats_free >= group._group_quant:
                    R.buffet.begin(group, R)

            if R.queue_headwaiter._queue and R.headwaiter._group_attended_id == 0:
                R.headwaiter.begin(
                    R.queue_headwaiter, R.all_tables, R.group_quant,
                    R.group_id, R.simulation_time, Stat)

            for waiter in R.waiters:
                if waiter._group_attended_id == 0:
                    for table in R.all_tables:
                        if table._group_eating.attended == 1:
                            waiter.drink_begin(R.simulation_time, table, Stat)

            for waiter in R.waiters:
                if waiter._group_attended_id == 0:
                    for table in R.all_tables:
                        if table._group_eating.attended == 2:
                            waiter.food_begin(R.simulation_time, table)

            for cashier in R.cashiers:
                if cashier._group_attended_id == 0:
                    Stat.queue_cashiers.append(len(R.queue_cashiers._queue))
                    cashier.begin(R.queue_cashiers, R.simulation_time)

            R.simulation_time += 1

elif x == '2':
    while R.number_of_groups <= 20:
            if R.simulation_time == R.next_appearance_time:
                g = Group(i)
                R.number_of_groups += 1
                g.appearance_time = R.simulation_time
                i += 1
                if g.q_type == 1:
                    Appear.execute(g, R.queue_buffet, R)
                if g.q_type == 2:
                    Appear.execute(g, R.queue_headwaiter, R)
                    Stat.queue_tables.append(len(R.queue_headwaiter._queue))
                    Stat.groups_appearance_time.append(g.appearance_time)

            for group in R.buffet.groups_eating:
                if group.buffet_end_time == R.simulation_time:
                    R.buffet.end(group, R.queue_cashiers)

            if  R.simulation_time == R.headwaiter.end_attend_time != 0:
                R.headwaiter.end(R.all_tables)

            for waiter in R.waiters:
                if waiter.end_attend_drink == R.simulation_time != 0:
                    waiter.drink_end()

            for waiter in R.waiters:
                if waiter.end_attend_food == R.simulation_time != 0:
                    waiter.food_end()

            for cashier in R.cashiers:
                if cashier.end_attend_time == R.simulation_time != 0:
                    cashier.end()

            for group in R.queue_buffet._queue:
                if R.buffet._seats_free >= group._group_quant:
                    R.buffet.begin(group, R)

            if R.queue_headwaiter._queue and R.headwaiter._group_attended_id == 0:
                R.headwaiter.begin(
                    R.queue_headwaiter, R.all_tables, R.group_quant,
                    R.group_id, R.simulation_time, Stat)

            for waiter in R.waiters:
                if waiter._group_attended_id == 0:
                    for table in R.all_tables:
                        if table._group_eating.attended == 1:
                            waiter.drink_begin(R.simulation_time, table, Stat)

            for waiter in R.waiters:
                if waiter._group_attended_id == 0:
                    for table in R.all_tables:
                        if table._group_eating.attended == 2:
                            waiter.food_begin(R.simulation_time, table)

            for cashier in R.cashiers:
                if cashier._group_attended_id == 0:
                    Stat.queue_cashiers.append(len(R.queue_cashiers._queue))
                    cashier.begin(R.queue_cashiers, R.simulation_time)

            R.simulation_time += 1

else:
    x = input('You put the wrong number, choose again: 1 or 2')



Stat.mean_table()
Stat.mean_headwaiter()
Stat.mean_waiter()
Stat.mean_cashier()