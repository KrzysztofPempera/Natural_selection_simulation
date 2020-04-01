import pygame as pg
import random as rnd
from colours import *

# block size
BLOCK_SIZE = 10

# motion direction constants
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3


# rabbit class definition
class rabbit(object):
   
    # constructor
    def __init__(self, surface, startPosX, startPosY, movementspeed):
        self.surface = surface
        self.posX = startPosX
        self.posY = startPosY
        self.ms = movementspeed
        self.seek = False

        self.colour = WHITE
    
    # get rabbits position
    def getPosition(self):
        return (self.posX, self.posY)

    # choose wandering direction
    def wander(self):
        return rnd.randint(1,4)

    # move rabbit
    def move(self):
        if self.seek == False:
            self.dir = self.wander()
        
        if self.dir == UP:
            self.posY -= self.ms
        elif self.dir == RIGHT:
            self.posX += self.ms
        elif self.dir == DOWN:
            self.posY += self.ms
        elif self.dir == LEFT:
            self.posX -= self.ms
        
        if self.posX >= 400:
            self.posX = self.posX - 400
        if self.posY >= 400:
            self.posY = self.posY - 400

    # draw rabbit    
    def draw(self):
        sur = self.surface

        rPosition = self.getPosition()

        pg.draw.rect(sur,self.colour,(rPosition[0],rPosition[1],BLOCK_SIZE,BLOCK_SIZE))


