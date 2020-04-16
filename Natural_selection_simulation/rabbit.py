import pygame as pg
from animal import animal
from colours import *


# motion direction constants
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3

# sense radius
SENSE = 15

# rabbit class definition
class rabbit(animal):
   
    # constructor
    def __init__(self, surface, movementspeed):
        animal.__init__(self, surface, movementspeed)
        self.colour = WHITE
    
    #find nearest food
    def seek(self, food):
        self.closest = self.scan(food)

        if self.wandering == False:
            self.path = self.createPath(self.closest)
            self.path.reverse()
            print("FOUND")
        elif self.wandering == True:
            print("searching..")
            return
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
  


