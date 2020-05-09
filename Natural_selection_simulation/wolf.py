import pygame as pg
import math
import numpy as np
from animal import animal
from colours import *
from rabbit import rabbit

# block size
BLOCK_SIZE = 10

class wolf(animal):
    
    # constructor
    def __init__(self, surface, movementspeed, posx, posy, sense):
        animal.__init__(self, surface, movementspeed, sense)
        self.colour = RED
        self.posX = posx
        self.posY = posy
        self.trail = 0
        self.energy = 500
        self.maxEnergy = 1500
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
