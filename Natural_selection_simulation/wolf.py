import pygame as pg
from animal import animal
from colours import *
from rabbit import rabbit

SENSE = 35

# block size
BLOCK_SIZE = 10

class wolf(animal):
    
    # constructor
    def __init__(self, surface, movementspeed, posx, posy):
        animal.__init__(self, surface, movementspeed)
        self.colour = RED
        self.posX = posx
        self.posY = posy
        self.energy = 1000
        self.maxEnergy = 1500
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
