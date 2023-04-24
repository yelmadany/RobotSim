import random

class cell:
    def __init__(self):
            self.__cost = random.randint(1,5)
    def getcost(self):
        return int(self.__cost)
    def __str__(self):
        return str(self.__cost)
    def __call__(self):
        return self
