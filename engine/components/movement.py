import random

class Movement:
    def __init__(self, movement_range = 3):
        self.movement_range = movement_range
        self.name = "Movement"

    def move(self, x = None, y = None):
        if (x == None and y == None):
            x = random.randint(0, self.movement_range)
            y = random.randint(0, self.movement_range)
        
        print(x, y)
        return (x, y)
    
    def update(self): 
        self.move()