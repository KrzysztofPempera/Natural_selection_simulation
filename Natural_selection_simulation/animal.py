import pygame as pg
import random as rnd
import numpy as np
import heapq
import math
from colours import *

# block size
BLOCK_SIZE = 10

# motion direction constants
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3


class animal(object):
# constructor
    def __init__(self, surface, movementspeed):
        self.surface = surface
        self.posX = rnd.randint(0, 380)
        self.posY = rnd.randint(0, 380)
        self.ms = movementspeed
        self.wandering = True
        self.eat = False
        self.path = []
        self.targetDistance = 0
        self.oldPosition = (-1,self.posY)
    
    # function to calculate distance between two points
    def calculateDistance(self,x1,y1,x2,y2):  
        self.dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
        return self.dist  

    # get animal position
    def getPosition(self):
        return self.posX, self.posY

    # get rabbits status
    def getWandering(self):
        return self.wandering

    def getEat(self):
        return self.eat;
   
    # more elegant currentDistance()
    def heuristic(self,a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    # create path to set destination
    def createPath(self, destination):
        moves  = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        visited = set()
        currentPath = {}
        # movement cost from starting node to current/potential node
        gScore = {self.getPosition():0}
        # score for each node
        fScore = {self.getPosition():self.heuristic(self.getPosition(),destination)}
        oheap = []
        heapq.heappush(oheap,(fScore[self.getPosition()],self.getPosition()))

        while oheap:
            current = heapq.heappop(oheap)[1]
            if current == destination:
                data = []
                while current in currentPath:
                    data.append(current)
                    current = currentPath[current]
                return data
            visited.add(current)

            for i,j in moves:
                move = current[0] + i, current[1] + j
                tempGScore = gScore [current] + self.heuristic(current,move)
                if move in visited and tempGScore >= gScore.get(move,0):
                    continue
                if tempGScore < gScore.get(move,0) or move not in [i[1]for i in oheap]:
                    currentPath[move] = current
                    gScore[move] = tempGScore
                    fScore[move] = tempGScore + self.heuristic(move,destination)
                    heapq.heappush(oheap,(fScore[move],move))


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
        moves = ((0,self.ms),(0,-self.ms),(self.ms,0),(-self.ms,0))
        nextMove = moves[rnd.randint(0,3)]
        newPosition = (position[0] + nextMove[0],position[1] + nextMove[1])
        return newPosition

    # move animal
    def move(self):
        if self.wandering == True:
            self.dir = self.wander()
            self.posX = self.dir[0]
            self.posY = self.dir[1]
            self.posY = self.posY % 400
            self.posX = self.posX % 400

        elif self.wandering == False:
            if self.path:
                self.nextMove = self.path.pop(0)
                self.posX = self.nextMove[0]
                self.posY = self.nextMove[1]
            else:
                self.eat = True
        
    # draw animal    
    def draw(self):
        sur = self.surface

        rPosition = self.getPosition()

        pg.draw.rect(sur,self.colour,(rPosition[0],rPosition[1],BLOCK_SIZE,BLOCK_SIZE))

