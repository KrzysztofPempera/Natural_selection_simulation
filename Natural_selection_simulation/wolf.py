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
        self.velocity = (0,0)
        self.target = object
        self.energy = 500
        self.maxEnergy = 900
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)

    def normalize(self,v):
        norm = np.linalg.norm(v)
        if norm == 0: 
           return v
        return v / norm

    def createVelocity(self):
        wPosition = self.getPosition()
        tPosition = self.target.getPosition()

        desired = np.subtract(tPosition,wPosition)

        desired = self.normalize(desired)
        desired = desired * self.ms
        velocity = (math.ceil(desired[0]),math.ceil(desired[1]))
        return velocity

    def seek(self, targets):
        self.target = self.scan(targets)
        if self.target:
            self.velocity = self.createVelocity()

    def move(self):
        if self.wandering == True:
            self.dir = self.wander()
            self.rect.x = self.dir[0] % 400
            self.rect.y = self.dir[1] % 400
            
        elif self.wandering == False:
            if self.target.eaten == False:
                self.velocity = self.createVelocity()
                if self.velocity[0] + self.velocity[1] == 0:
                    self.wandering = True
                print(self.velocity,'  ',self.target.getPosition())
                self.rect.x = (self.rect.x + self.velocity[0]) %400
                self.rect.y = (self.rect.y + self.velocity[1]) %400

            elif self.target.eaten == True:
                    self.wandering = True

        self.energy -= self.ms

