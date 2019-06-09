import matplotlib.pyplot as plt
import statistics

class Stats:
    """description of class"""
    def __init__(self):
        self.wait_time_headwaiter = []
        self.queue_tables = []
        self.wait_time_waiter = []
        self.queue_cashiers = []
        self.groups_appearance_time = []
        self.headwaiter_start = []
        self.number_of_all = []
        self.number_of_groups = 0
        self.time = []


    def histogram_queue_tables(self):
        plt.hist(self.queue_tables, bins=20)
        plt.title("Histogram for queue to the tables")
        plt.xlabel("Seconds")
        plt.ylabel("Number of groups")
        plt.show()

    def histogram_table_wait_time(self):
        plt.hist(self.wait_time_headwaiter, bins=20)
        plt.title("Histogram for time spent waiting for the table")
        plt.xlabel("Seconds")
        plt.ylabel("Number of groups")
        plt.show()

    def mean_table(self):
        x = int(statistics.mean(self.queue_tables))
        print('Mean for the number of groups waiting for a table is: {}'.format(x))
        return x

    def mean_headwaiter(self):
        x = int(statistics.mean(self.wait_time_headwaiter)*0.01666)
        print('Mean for the time spent waiting for the table is: {} minutes'.format(x))
        return x

    def mean_waiter(self):
        x = int(statistics.mean(self.wait_time_waiter))
        print('Mean for the time spent waiting for the waiter is: {} seconds'.format(x))
        return x

    def mean_cashier(self):
        x = int(statistics.mean(self.queue_cashiers))
        print('Mean for the number of groups waiting for cashier is: {}'.format(x))
        return x
    
    def phase(self):
        plt.plot(self.time, self.number_of_all)
        plt.ylabel('Number of groups')
        plt.xlabel('Time')
        plt.show()