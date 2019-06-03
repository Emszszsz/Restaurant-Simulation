import numpy as np
import random as random


class Group:

    """ Group of clients that is interpreted by system as one
    unseparable client
    p - private
    Attributes:
               >p id - identification number of the group, must be
               greater than 0
               >  probs - probabilities of the appearance of certain
                  numbered group
               >  choices - quantities(1, 2, 3, 4) from which, system
                  randomly chooses one to asign to the group
               >p place_to_eat - either a buffet or table
               >p group_quant - quantity of the group
               >p appearance_time - time in which the group appears
                  in the system
               >p time_spent_b - time the client spent at the buffet
               >p time_spent_t - time the client spent at the table
    Methods:
               > __init__(self, if, appearance_time, time_spent_b,
                   time_spent_t)
                 - method that initialises a group object
               > info(self) - displays all the information of the group

    """

    def __init__(self, id):
        self.id = id
        self.lambda_f = 1900
        probs = [0.11, 0.33, 0.33, 0.23]
        choices = [1, 2, 3, 4]
        self._place_to_eat = random.random()
        self._group_quant = np.random.choice(choices, p=probs)
        if self._place_to_eat < 0.5:
            self.q_type = 1
        else:
            self.q_type = 2
        self.buffet_end_time = 0
        self.dinner_end_time = 0
        self.attended = 0
        self.appearance_time = 0
        self.end_attend_headwaiter = 0
