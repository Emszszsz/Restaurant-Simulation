""" Clients group module

"""

import numpy as np


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
        self._id = id
        probs = [0.2, 0.4, 0.1, 0.3]
        choices = [1, 2, 3, 4]
        self._place_to_eat = abs(np.random.normal(0.5, 0.1))
        self._group_quant = np.random.choice(choices, p=probs)
        if self._place_to_eat >= 0.5:
            self.q_type = 1
        else:
            self.q_type = 2
