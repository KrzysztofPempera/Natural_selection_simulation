import random as rnd
import pygame as pg
from colors import *


# block size
BLOCK_SIZE = 10

# carrot class definition
class carrot(object):
    
    #constructor
    def __init__(self, surface, minX, maxX, minY, maxY):
        self.surface = surface
        self.posX = rnd.randint(minX, maxX - 1)
        self.posY = rnd.randint(minY, maxY - 1)

        self.colour = ORANGE

    def getPosition(self):
        return (self.posX, self.posY)

    def move(self):
        self.posX += 1
        self.posY += 1

    def draw(self):
        sur = self.surface

        cPosition = self.getPosition()

        pg.draw.rect(sur,self.colour,(cPosition[0],cPosition[1],BLOCK_SIZE,BLOCK_SIZE))
