import pygame as pg
import math
import random as rnd
from animal import animal
from colours import *

# block size
BLOCK_SIZE = 9

# rabbit class definition
class rabbit(animal):
   
    # constructor
    def __init__(self, surface, movementspeed, posx, posy, sense):
        animal.__init__(self, surface, movementspeed, sense)
        self.posX = posx
        self.posY = posy
        self.colour = WHITE
        self.eaten = False
        self.energy = 150
        self.maxEnergy = 500
        self.energyRep = 150
        self.maxAge = 200
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
    
        def getEaten(self):
            return self.eaten

