import random as rnd
import pygame as pg
from colours import *


# block size
BLOCK_SIZE = 10

# carrot class definition
class carrot(object):
    
    # constructor
    def __init__(self, surface, minX, maxX, minY, maxY):
        self.surface = surface
        self.posX = rnd.randint(minX, maxX - 1)
        self.posY = rnd.randint(minY, maxY - 1)

        self.colour = ORANGE

    # get carrots position
    def getPosition(self):
        return (self.posX, self.posY)

    # draw carrot
    def draw(self):
        sur = self.surface

        cPosition = self.getPosition()

        pg.draw.rect(sur,self.colour,(cPosition[0],cPosition[1],BLOCK_SIZE,BLOCK_SIZE))
