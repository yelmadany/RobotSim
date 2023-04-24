class simulationCycle:
    def __init__(self):
        self.__time = 0

    def incCycle(self):
        self.__time += 1

    def getCycle(self):
        return self.__time

