from location import location
class ext:
    def __init__(self):

        self.X = int(input("Enter Row Number for the exit: "))
        self.Y = int(input("Enter Col Number for the exit: "))

        if(self.X >= 10):
            self.X = 9
        if(self.Y >= 10):
            self.Y = 9

        self.loc = location()
        self.loc.setxy(int(self.X),int(self.Y))
        self.locVal = self.loc.getCurrentLoc()
