class Appear:
    """class that manages the appearance of the clients in the system"""
    @staticmethod
    def execute(obj, queue, restaurant):
        """Adds group to the queue and plans next appearance"""
        mean_a = 2
        std_a = 2.14
        queue.enqueue(obj)
        restaurant.next_appearance_time += 2
        print('Next appearance at {} minutes'
              .format(restaurant.next_appearance_time))
