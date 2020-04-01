import pygame as pg
import random as rnd
import math
from colours import *

# block size
BLOCK_SIZE = 10

# motion direction constants
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

# sense radius
SENSE = 15

# rabbit class definition
class rabbit(object):
   
    # constructor
    def __init__(self, surface, startPosX, startPosY, movementspeed):
        self.surface = surface
        self.posX = startPosX
        self.posY = startPosY
        self.ms = movementspeed
        self.wandering = True

        self.colour = WHITE
    

    
# function to calculate distance between two points
    def calculateDistance(self,x1,y1,x2,y2):  
        self.dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
        return self.dist  

    # get rabbits position
    def getPosition(self):
        return (self.posX, self.posY)

    # get rabbits status
    def isWandering(self):
        return(self.wandering)

    #find nearest food
    def search(self, food):
        self.closest = self.scan(food)

        if self.wandering == False:
            return self.closest
        else:
            return print('searching')

    # scan for closest food
    def scan(self, food):

        rPosition = self.getPosition()
        for carrot in food:
            cPositionX = carrot.posX
            cPositionY = carrot.posY
            distance = self.calculateDistance(rPosition[0], rPosition[1],cPositionX, cPositionY)
            
            if distance <= SENSE:
                self.wandering = False
                return cPositionX,cPositionY
            
    # create path to set destination
    #def createPath(self, destination):
    #    end = destination
    #    rPosition = self.getPosition()
    #    self.distance = self.calculateDistance(rPosition[0], rPosition[1],end[0], end[1])
    #    while True:
    #        if rPosition != end:
    #            tempPosition = rPosition


    # choose wandering direction
    def wander(self):
        return rnd.randint(0,3)

    # move rabbit
    def move(self):
        if self.wandering == True:
            self.dir = self.wander()

            # check wandering direction
            if self.dir == UP:
                self.posY -= self.ms
            elif self.dir == RIGHT:
                self.posX += self.ms
            elif self.dir == DOWN:
                self.posY += self.ms
            elif self.dir == LEFT:
                self.posX -= self.ms
        elif self.wandering == False:
            print('find')
        
        # fix out of bounds behavior
        if self.posX >= 400:
            self.posX = self.posX - 400
        if self.posY >= 400:
            self.posY = self.posY - 400

    # draw rabbit    
    def draw(self):
        sur = self.surface

        rPosition = self.getPosition()

        pg.draw.rect(sur,self.colour,(rPosition[0],rPosition[1],BLOCK_SIZE,BLOCK_SIZE))


