from location import location
class simulatedEntity:

    def __init__(self,r,c):
        self.speed = 2
        self.x = 0
        self.y = 1
        self.Collision_Status = False
        self.Collision_Status2 = False
        self.locpos = location(r, c)
        self.target = None
        self.loc = self.locpos.getCurrentLoc()
        self.loc1 = self.loc
        self.ListOfMovements = None
    def getCurrentLocation(self):
        return self.loc.getCurrentLoc()

    def setDestination(self,e):
        self.ext = e


    def move(self):

        pass
    def stopCollision(self):
        self.speed=0

