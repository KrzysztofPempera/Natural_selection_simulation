import pygame as pg
import random as rnd
import numpy as np
import heapq
import math
import json
from colours import *

with open('para.json', 'r') as para:
    config = json.load(para)

MUTATION_THRESHOLD = 0.5

# motion direction constants
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3


class animal(object):
# constructor
    def __init__(self, surface, movementspeed, sense):
        self.surface = surface
        self.sense = sense
        self.ms = movementspeed
        self.eat = False
        self.wandering = True
        self.velocity = (0,0)
        self.target = object
        self.oldPosition = (-1,-1)
        self.age = 0

   
    # get animal position
    def getPosition(self):
        return self.rect.x, self.rect.y

    # get rabbits status
    def getWandering(self):
        return self.wandering

    def getEat(self):
        return self.eat;
   
    # more elegant currentDistance()
    def heuristic(self,a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    # choose wandering direction
    def wander(self):
        position = self.getPosition()
        newPosition = self.getNewPosition(position)
        if newPosition != self.oldPosition:
            self.oldPosition = position
            return newPosition
        else:
            return self.wander()
            
    def getNewPosition(self, position):
        moves = ((0,self.ms),(0,-self.ms),(self.ms,0),(-self.ms,0), (self.ms,self.ms), (self.ms,-self.ms), (-self.ms,self.ms), (-self.ms,-self.ms))
        nextMove = moves[rnd.randrange(len(moves))]

        newPosition = (position[0] + nextMove[0],position[1] + nextMove[1])
        return newPosition

    def mutate(self, parameter):
        mutationPosibilities = [1,-1]
        ifMutate = rnd.uniform(0,1)

        if ifMutate < MUTATION_THRESHOLD:   
            parameter += rnd.choice(mutationPosibilities)
        return parameter

    def reproduce(self, referenceList, animal):
        self.energy = math.floor(self.energy*config['REPRODUCTION_COST'])
        aPosition = self.getPosition()

        newMs = self.mutate(self.ms)
        newSense = self.mutate(self.sense)

        if newSense <=10:
            newSense = 11
        if newMs <= 0:
            newMs = 1
        
        referenceList.append(animal(self.surface, newMs, aPosition[0], aPosition[1], newSense))

    def normalize(self,v):
        norm = np.linalg.norm(v)
        if norm == 0: 
           return v
        return v / norm

    def createVelocity(self):
        aPosition = self.getPosition()
        tPosition = self.target.getPosition()

        desired = np.subtract(tPosition,aPosition)

        desired = self.normalize(desired)
        desired = desired * self.ms
        velocity = (math.ceil(desired[0]),math.ceil(desired[1]))
        return velocity

    # scan for closest food
    def scan(self, targets):

        aPosition = self.getPosition()
        for target in targets:
            targetPosition = target.rect.center
            targetDistance = self.heuristic(aPosition, targetPosition)
            
            if targetDistance <= self.sense:
                self.wandering = False
                return target
        return

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
            if self.target.dead == False:
                self.velocity = self.createVelocity()
                if self.velocity.count(0) == len(self.velocity):
                    self.wandering = True
                self.rect.x = (self.rect.x + self.velocity[0]) %400
                self.rect.y = (self.rect.y + self.velocity[1]) %400

            elif self.target.dead == True:
                    self.wandering = True
            else:
                self.wandering = True
        self.energy -= self.ms

    # draw animal    
    def draw(self):
        sur = self.surface
        rect = self.rect 
        pg.draw.rect(sur, self.colour, rect)

