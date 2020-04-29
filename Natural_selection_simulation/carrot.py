import random as rnd
import pygame as pg
from colours import *


# block size
BLOCK_SIZE = 8

# carrot class definition
class carrot(object):
    
    # constructor
    def __init__(self, surface, minX, maxX, minY, maxY):
        self.surface = surface
        self.colour = ORANGE
        self.energy = 30
        self.rect = pg.Rect(rnd.randint(minX, maxX - 1), rnd.randint(minY, maxY - 1), BLOCK_SIZE, BLOCK_SIZE)

    # get carrots position
    def getPosition(self):
        return self.rect.x, self.rect.y

    # draw carrot
    def draw(self):
        sur = self.surface

        pg.draw.rect(sur,self.colour,self.rect)
