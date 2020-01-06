from restaurant import Restaurant
from restaurant import Group
from restaurant import Stats
import numpy as np

id = 1
flag = True
R = Restaurant()
S = Stats()
while id < 100:
    if flag == True:
        if R.queue_bf and R.buffet.free_places != 0:
            for client in R.queue_bf:
                if client.quant <= R.buffet.free_places:
                    R.buffet.add(client, R.event_list, R.sim_tim)
                    R.queue_bf.remove(client)
                    flag = False
        if len(R.queue_hw) != 0 and len(R.headwaiter.group) == 0:
            R.headwaiter.group.append(R.queue_hw.pop())
            R.headwaiter.take_to_table(R.tables_2, R.tables_3, R.tables_4, R.sim_tim)
            S.mean_time_for_table += R.sim_tim - R.headwaiter.group[0].app_time
            R.headwaiter.group[0].begin = S.mean_time_for_table
            R.event_list.append(R.headwaiter.end)
            flag = False

        for table in R.tables:
            if len(table.group) != 0 and table.group[0].attended != 1:
                table.start_drink(R.waiters, R.sim_tim, R.event_list)
                S.mean_time_waiter += (R.sim_tim - table.group[0].begin)
                table.start_food(R.waiters, R.sim_tim, R.event_list)
                flag = False
                break
        for cashier in R.cashiers:
            if len(cashier.group) == 0 and len(R.queue_cash) != 0:
                cashier.add(R.queue_cash.pop(), R.event_list)
                flag = False
        for table in R.tables:
            if len(table.group) != 0:
                if R.sim_tim == table.group[0].consumption_time:                    
                    R.queue_cash.append(table.group.pop)
                    table.group.remove(table.group[0])
                    flag = False
                    break
        if R.sim_tim == R.next_app:
            g = Group(id)
            g.app_time = R.sim_tim
            id += 1
            S.counter += 1
            S.counter_v.append(abs(S.counter))
            S.time.append(R.sim_tim)
            if g.place_to_eat == 0:
                R.queue_bf.append(g)
                R.next_app = R.sim_tim + np.random.normal(2000, 200)
                R.event_list.append(R.next_app)
                R.event_list.sort()
                flag = False
            else:
                R.queue_hw.append(g)
                #print('group {} to hw'.format(g.id))
                R.next_app = np.random.normal(2000, 200)
                R.event_list.append(R.next_app)
                R.event_list.sort()
                S.mean_q_hw += len(R.queue_hw)
                S.groups += 1
                flag = False

        for waiter in R.waiters:
            if R.sim_tim == waiter.end_drink != 0:
                waiter.free = 0
                flag = False

        for waiter in R.waiters:
            if R.sim_tim == waiter.end_din != 0:
                waiter.free = 0
                flag = False
                break

        if R.sim_tim == R.headwaiter.end != 0:
            R.queue_cash.append(R.headwaiter.group.pop())
            R.headwaiter.group_id = 0
            flag = False

        for client in R.buffet.groups:
            if R.sim_tim == client.consumption_time:
                R.queue_cash.append(client)
                R.buffet.free_places += client.quant
                R.buffet.groups.remove(client)
                flag = False
       
        for cashier in R.cashiers:
            if R.sim_tim == cashier.end != 0:
                cashier.group.pop()
                S.counter -= 1
                S.counter_v.append(abs(S.counter))
                S.time.append(R.sim_tim)
                S.mean_q_c += len(R.queue_cash)
                flag = False

        R.sim_tim = R.event_list.pop()
        flag = True
