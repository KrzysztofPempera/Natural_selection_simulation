import pygame as pg
from animal import animal
from colours import *
from rabbit import rabbit

SENSE = 30

# block size
BLOCK_SIZE = 10

class wolf(animal):
    
    # constructor
    def __init__(self, surface, movementspeed):
        animal.__init__(self, surface, movementspeed)
        self.colour = RED
        self.posX = 200
        self.posY = 200
        self.sense = SENSE
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
        
    def checkTarget(self):
        if self.wandering == False:
            if self.target.eaten == True:
                self.wandering = True

            elif self.path and self.target.getPosition() != self.path[-1]:
                self.path = self.createPath(self.target.getPosition())
                self.path.reverse()
                if self.path:
                    self.path = self.newPath()
