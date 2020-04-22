import pygame as pg
from animal import animal
from colours import *
from rabbit import rabbit

SENSE = 30

class wolf(animal):
    
    # constructor
    def __init__(self, surface, movementspeed):
        animal.__init__(self, surface, movementspeed)
        self.colour = RED
        self.posX = 200
        self.posY = 200
        self.target = rabbit
    
    #find nearest food
    def seek(self, food):
        self.closest = self.scan(food)

        if self.wandering == False:
            self.path = self.createPath(self.closest)
            self.path.reverse()
        elif self.wandering == True:
            return

    # scan for closest food
    def scan(self, rabbits):

        rPosition = self.getPosition()
        for rabbit in rabbits:
            rPositionX = rabbit.posX
            rPositionY = rabbit.posY
            self.targetDistance = self.calculateDistance(rPosition[0], rPosition[1],rPositionX, rPositionY)
            
            if self.targetDistance <= SENSE:
                self.wandering = False
                self.target = rabbit
                return rPositionX,rPositionY
        return


