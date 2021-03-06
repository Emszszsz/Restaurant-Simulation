import numpy as np


class Appear:
    """class that manages the appearance of the clients in the system"""
    @staticmethod
    def execute(obj, queue, restaurant):
        """Adds group to the queue and plans next appearance"""
        mean_a = 1000
        std_a = 200
        queue._queue.append(obj)
        if obj.q_type == 2:
            restaurant.groups.append(obj)
        restaurant.next_appearance_time = restaurant.simulation_time + abs(int(np.random.normal(mean_a, std_a)))
        obj.appearance_time = restaurant.simulation_time