import pygame as pg
import math
import random as rnd
from animal import animal
from colours import *

# sense radius
SENSE = 15

# block size
BLOCK_SIZE = 9

# rabbit class definition
class rabbit(animal):
   
    # constructor
    def __init__(self, surface, movementspeed, posx, posy):
        animal.__init__(self, surface, movementspeed)
        self.posX = posx
        self.posY = posy
        self.colour = WHITE
        self.sense = SENSE
        self.eaten = False
        self.energy = 150
        self.maxEnergy = 500
        self.energyRep = 150
        self.maxAge = 200
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
    
        def getEaten(self):
            return self.eaten

        def setEaten(self, bool):
            self.eaten = bool
