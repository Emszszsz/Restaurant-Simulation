import numpy as np
class Appear:
    """class that manages the appearance of the clients in the system"""
    @staticmethod
    def execute(obj, queue, restaurant):
        """Adds group to the queue and plans next appearance"""
        mean_a = 1900
        std_a = 40000
        queue.enqueue(obj)
        if obj.q_type == 2:
            restaurant.group_quant.append(obj._group_quant)
        restaurant.next_appearance_time = np.random.normal(mean_a, std_a)
