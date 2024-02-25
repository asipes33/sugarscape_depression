import math
import random

class Depression:
    def __init__(self, configuration):
        self.depSugarMetabolism = configuration["depSugarMetabolism"]
        self.depSpiceMetabolism = configuration["depSpiceMetabolism"]
        self.depMovement = configuration["depMovement"]
        self.depAggression = configuration["depAggression"]
        self.depMaxFriends = configuration["depMaxFriends"]
        self.depHappiness = configuration["depHappiness"]
        self.configuration = configuration
        self.agent = None

    def __str__(self):
        return "{0}".format(self.ID)