import numpy as np
import random
import matplotlib.pyplot as plt
class Group:
    def __init__(self, id):
        self.id = id
        self.quant = np.random.choice(np.arange(1, 5), p=[0.11, 0.33, 0.33, 0.23])
        self.place_to_eat = random.getrandbits(1)
        self.consumption_time = 0
        self.drink = 0
        self.attended = 0
        self.app_time = 0
        self.begin = 0


class Buffet:
    def __init__(self):
        self.places = 14
        self.groups = []
        self.free_places = 14
    def add(self, group, e_list, time):
        self.free_places -= group.quant
        self.groups.append(group)
        group.consumption_time = time + np.random.normal(3200, 100)
        e_list.append(group.consumption_time)


class Table:
    def __init__(self, places, id):
        self.places = places
        self.id = id
        self.group = []
    def start_drink(self, waiters, time, ev_list):
        for waiter in waiters:
            if waiter.free == 0 and self.group[0].drink == 0:
                waiter.free = 1
                self.group[0].drink = 1
                waiter.drink(self.group[0], time, ev_list)
            break
    def start_food(self, waiters, time, ev_list):
        for waiter in waiters:
            if waiter.free == 0 and self.group[0].drink == 1:
                waiter.free = 1
                waiter.food(self.group[0], time, ev_list)
                self.group[0].attended = 1
            break


class Headwaiter:
    def __init__(self):
        self.group = []
        self.end = 0
        self.group_id = 0
    def take_to_table(self, table2, table3, table4, time):
        if self.group[0].quant <= 2:
            for table in table2:
                if len(table.group) == 0:
                    table.group.append(self.group[0])
                    self.group_id = self.group[0].id
                break
            self.end = time + 30
        elif self.group[0].quant == 3:
            for table in table3:
                if len(table.group) == 0:
                    table.group.append(self.group[0])
                    self.group_id = self.group[0].id
                break
            self.end = time + 30
        else:
            for table in table4:
                if len(table.group) == 0:
                    table.group.append(self.group[0])
                    self.group_id = self.group[0].id
                break
            self.end = time + 30

class Waiter:
    def __init__(self, id):
        self.id = id
        self.end_drink = 0
        self.end_din = 0
        self.free = 0
    def drink(self, group, time, ev_list):
        self.end_drink = time + np.random.exponential(300)
        ev_list.append(self.end_drink)
    def food(self, group, time, ev_list):
        self.end_din = time + np.random.exponential(1700)
        group.consumption_time = time + np.random.exponential(1900)
        ev_list.append(self.end_din)
        ev_list.append(group.consumption_time)

class Cashier:
    def __init__(self, id):
        self.id = id
        self.group = []
        self.end = 0
    def add(self, group, e_list):
        self.group.append(group)
        self.end = np.random.exponential(200)
        e_list.append(self.end)



class Restaurant:
    def __init__(self):
        self.queue_hw = []
        self.queue_bf = []
        self.queue_cash = []
        self.waiters = [Waiter(i) for i in range(1,8)]
        self.cashiers = [Cashier(i) for i in range(1,5)]
        self.headwaiter = Headwaiter()
        self.tables_2 = [Table(2, i) for i in range(1,5)]
        self.tables_3 = [Table(3, i) for i in range(1,11)]
        self.tables_4 = [Table(4, i) for i in range(1,5)]
        self.tables = self.tables_2 + self.tables_3 + self.tables_4
        self.buffet = Buffet()
        self.next_app = 0
        self.event_list = []
        self.sim_tim = 0

class Stats:
    def __init__(self):
        self.counter = 0
        self.counter_v = []
        self.time = []
        self.mean_time_for_table = 0
        self.mean_time_waiter = 0
        self.groups = 0
        self.mean_q_hw = 0
        self.mean_q_c = 0
    def phase(self):
        self.time.sort()
        plt.plot(self.time, self.counter_v)
        plt.xlabel('time')
        plt.ylabel('groups')
        plt.show()
    def mean_table(self):
        return abs(self.mean_time_for_table/self.groups)
    def mean_queue_hw(self):
        return abs(self.mean_q_hw/self.groups)
    def mean_waiter(self):
        return abs(self.mean_time_waiter/self.groups)
    def mean_queue_c(self):
        return abs(self.mean_q_c/200)

        