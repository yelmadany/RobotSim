import sys
import threading
import time
import simulatedEntity
from ext import ext
from GraphClass import GraphC
from GraphClass import dijkstra
from GraphClass import dijsktraEND
from simulationCycle import simulationCycle
from simulatedEntity import simulatedEntity
import pygame
RobotList = [1,]
ExitList = []
CanDrawStuff = False
countC = 0
BLACK = (250, 250, 250)
WHITE = (0, 0, 0)
WINDOW_HEIGHT = 500
WINDOW_WIDTH = 500
CellNumbering = {0: [0, 0], 1: [0, 1], 2: [0, 2], 3: [0, 3], 4: [0, 4], 5: [0, 5], 6: [0, 6], 7: [0, 7], 8: [0, 8], 9: [0, 9], 10: [1, 0], 11: [1, 1], 12: [1, 2], 13: [1, 3], 14: [1, 4], 15: [1, 5], 16: [1, 6], 17: [1, 7], 18: [1, 8], 19: [1, 9], 20: [2, 0], 21: [2, 1], 22: [2, 2], 23: [2, 3], 24: [2, 4], 25: [2, 5], 26: [2, 6], 27: [2, 7], 28: [2, 8], 29: [2, 9], 30: [3, 0], 31: [3, 1], 32: [3, 2], 33: [3, 3], 34: [3, 4], 35: [3, 5], 36: [3, 6], 37: [3, 7], 38: [3, 8], 39: [3, 9], 40: [4, 0], 41: [4, 1], 42: [4, 2], 43: [4, 3], 44: [4, 4], 45: [4, 5], 46: [4, 6], 47: [4, 7], 48: [4, 8], 49: [4, 9], 50: [5, 0], 51: [5, 1], 52: [5, 2], 53: [5, 3], 54: [5, 4], 55: [5, 5], 56: [5, 6], 57: [5, 7], 58: [5, 8], 59: [5, 9], 60: [6, 0], 61: [6, 1], 62: [6, 2], 63: [6, 3], 64: [6, 4], 65: [6, 5], 66: [6, 6], 67: [6, 7], 68: [6, 8], 69: [6, 9], 70: [7, 0], 71: [7, 1], 72: [7, 2], 73: [7, 3], 74: [7, 4], 75: [7, 5], 76: [7, 6], 77: [7, 7], 78: [7, 8], 79: [7, 9], 80: [8, 0], 81: [8, 1], 82: [8, 2], 83: [8, 3], 84: [8, 4], 85: [8, 5], 86: [8, 6], 87: [8, 7], 88: [8, 8], 89: [8, 9], 90: [9, 0], 91: [9, 1], 92: [9, 2], 93: [9, 3], 94: [9, 4], 95: [9, 5], 96: [9, 6], 97: [9, 7], 98: [9, 8], 99: [9, 9]}
Waiter = False
a = threading.RLock

class virtual_Environment:
    global extLst, robotLst, countC,a
    def __init__(self, nRobots):
        self.rows = 10
        self.cols = 10
        self.firstcycle = True
        self.cycle = simulationCycle()
        self.ograph = GraphC()
        self.listR = []
        self.listEx = []
        for i in range(nRobots):
            self.listR.append(simulatedEntity(self.rows, self.cols))

    def extInit(self, nExt):
        for i in range(nExt):
            self.listEx.append(ext())

    def checkReached(self):
        count = 0
        for i in self.listR:
            for y in self.listEx:
                if int(i.loc.x) == int(y.X) and int(i.loc.y) == int(y.Y):
                    print("Robot number " + str(count) + " reached the exit")
                    self.listR.remove(i)
            count += 1

    def calculateClosestMinimum(self, R, D):
        min = 100000
        COST = 100000
        closest = None
        cheapest = None
        for ex in self.listEx:

            cal = abs((R.locpos.x + R.locpos.y) - (ex.loc.x + ex.loc.y))
            cost = D[ex.locVal]

            if (COST > cost):
                COST = cost
                cheapest = ex

            if (min > cal):
                min = cal
                closest = ex

        if cost > 10000:
            return closest.locVal , closest.locVal
        return closest.locVal, cheapest.locVal

    def calculateExitforRobots(self):
        for r in self.listR:
            dict_Of_Costs = dijkstra(self.ograph, r.loc)
            ClosestEx, CheapestEx = self.calculateClosestMinimum(r, dict_Of_Costs)

            if (dict_Of_Costs[CheapestEx] * 1.5 < dict_Of_Costs[ClosestEx]):
                r.target = CheapestEx
            else:
                r.target = ClosestEx
            r.ListOfMovements = dijsktraEND(self.ograph, r.loc, r.target)



    def print_Visuals(self):

        for i in range(self.rows):
            for y in range(self.cols):
                print(self.ograph.vertx[i*10+y],end=' ')
            print()


    def SecondMovement(self):
        for r in self.listR:
            switch =r.loc
            r.loc = r.loc1
            r.loc1 = switch

    def DrawStuff(self):
        global RobotList,ExitList,CanDrawStuff
        RobotList = self.listR
        ExitList = self.listEx

        CanDrawStuff = True


    def startSimulationCycle(self):

        for r in self.listR:
            if (r.loc == r.target):
                self.listR.remove(r)
            if(len(r.ListOfMovements) >= 2):
                nextmove = r.ListOfMovements[0]
                nextnextmove = r.ListOfMovements[1]
            if(len(r.ListOfMovements) == 1):
                nextmove = r.ListOfMovements[0]
                nextnextmove = r.ListOfMovements[0]
            if(len(r.ListOfMovements) == 0):
                nextmove = r.loc
                nextnextmove = r.loc
                return

            for Or in self.listR:
                if(r != Or):
                    if (nextnextmove == Or.loc):
                        r.Collision_Status2 = True
                    if (nextmove == Or.loc):
                        r.Collision_Status = True
            if self.firstcycle == True:
                r.loc = r.ListOfMovements.pop(0)
                r.loc1 = r.loc

            elif r.Collision_Status == False and r.Collision_Status2 == False and r.speed == 2 and (len(r.ListOfMovements) >= 2):

                r.loc = r.ListOfMovements.pop(0)
                r.loc1 = r.ListOfMovements.pop(0)


            elif (r.Collision_Status == False and r.speed == 1) or (
                    r.Collision_Status2 == True and r.Collision_Status == False and r.speed == 2) or (r.Collision_Status == False and r.Collision_Status2 == False and r.speed == 2 and (len(r.ListOfMovements) < 2)):
                r.loc = r.ListOfMovements.pop(0)
                r.loc1 = r.loc
            elif(r.Collision_Status == True):
                r.loc1 = r.loc

            r.Collision_Status2 = False
            r.Collision_Status = False
        self.firstcycle = False
        self.DrawStuff()
        pass


class systemController:
    global extLst,Waiter
    def __init__(self):
        self.count = 0
        self.nRob = int(input("Enter the number of robots: "))
        if self.nRob >= 100:
            print("Please enter number less than 100!!!")
            while self.nRob >= 100:
                self.nRob = int(input("Enter the number of robots: "))
        # self.nRow = int(input("Enter the number of rows: "))
        # self.nCol = int(input("Enter the number of cols: "))
        self.VE = virtual_Environment(self.nRob)
        self.VE.extInit(int(input("Enter the number of Exits: ")))
        self.VE.calculateExitforRobots()
        print("Environment SetUpDONE!")
        print(f"Simulation Cycle READY ")
        input("Press enter to continue.................")
        extLst = self.VE.listEx
        while len(self.VE.listR) != 0:
            self.VE.startSimulationCycle()
            print()
            print(f"Simulation Cycle:{self.VE.cycle.getCycle()}.0")
            self.VE.print_Visuals()
            time.sleep(0.5)
            self.VE.SecondMovement()
            input("Press enter to continue:")
            self.VE.cycle.incCycle()
            time.sleep(0.5)
        print("Simulation ended no more robots :D")
        pygame.quit()
        pygame.display.update()
        sys.exit(-1)





def Draw():
    global countC,SCREEN, CLOCK
    pygame.display.set_caption(str('Robot Simulation || Version 0.'+str(countC*"0")+'1🔥👌'))
    countC+=1
    if countC == 50:
        countC = 0
    blockSize = 50  # Set the size of the grid block
    image = pygame.image.load("Grass.png")
    ScreenImage = image.get_rect()
    SCREEN.blit(image, ScreenImage)
    for x in range(0, WINDOW_WIDTH, blockSize):
        for y in range(0, WINDOW_HEIGHT, blockSize):
            rect = pygame.Rect(x, y, blockSize, blockSize)
            pygame.draw.rect(SCREEN, WHITE, rect, 1)
    if CanDrawStuff:
        cont = 0
        imageExit = pygame.image.load("Exit.png")
        imageRobo = pygame.image.load("Robot.png")
        for i in range(10):
            for y in range(10):
                real_y = y + 10 * cont
                for z in RobotList:
                    if int(real_y) == int(z.loc):
                        Cords = CellNumbering[real_y]
                        l, o = Cords
                        SCREEN.blit(imageRobo, (l * blockSize, o * blockSize))
                for z in ExitList:
                    if int(real_y) == int(z.locVal):
                        Cords = CellNumbering[real_y]
                        l, o = Cords
                        SCREEN.blit(imageExit, (l * blockSize, o * blockSize))


            cont += 1
    pygame.time.wait(10)

def main():
    global SCREEN, CLOCK,a
    pygame.init()
    SCREEN = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    CLOCK = pygame.time.Clock()
    SCREEN.fill(BLACK)
    a = pygame.image.load('Troll.png')
    pygame.display.set_icon(a)
    while True:
        Draw()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or len(RobotList) == 0:
                pygame.quit()
                sys.exit()
        pygame.display.update()
        pygame.time.wait(10)

T2 = threading.Thread(target= systemController)
T = threading.Thread(target=main)
T2.start()
time.sleep(0.5)
T.start()
T2.join()
T.join()



