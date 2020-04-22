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
    def __init__(self, surface, movementspeed, id):
        animal.__init__(self, surface, movementspeed)
        self.posX = rnd.randint(0, 380)
        self.posY = rnd.randint(0, 380)
        self.colour = WHITE
        self.id = id
        self.sense = SENSE
        self.eaten = False
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
    
        def getEaten(self):
            return self.eaten

        def setEaten(self, bool):
            self.eaten = bool
