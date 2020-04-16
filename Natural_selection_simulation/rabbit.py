import pygame as pg
import math

from animal import animal
from colours import *

# sense radius
SENSE = 15

# rabbit class definition
class rabbit(animal):
   
    # constructor
    def __init__(self, surface, movementspeed, id):
        animal.__init__(self, surface, movementspeed)
        self.colour = WHITE
        self.id = id
    
    #find nearest food
    def seek(self, food):
        self.closest = self.scan(food)

        if self.wandering == False:
            self.path = self.createPath(self.closest)
            self.path.reverse()
            self.path = self.newPath()
        elif self.wandering == True:
            return

    def newPath(self):
        newPath = []
        temp = math.floor(len(self.path)/self.ms)
        for i in range(temp):
            newPath.append(self.path[i*self.ms])
        newPath.append(self.path.pop())
        return newPath

    # scan for closest food
    def scan(self, food):

        rPosition = self.getPosition()
        for carrot in food:
            cPositionX = carrot.posX
            cPositionY = carrot.posY
            self.targetDistance = self.calculateDistance(rPosition[0], rPosition[1],cPositionX, cPositionY)
            
            if self.targetDistance == SENSE:
                self.wandering = False
                return cPositionX,cPositionY
        return
  


