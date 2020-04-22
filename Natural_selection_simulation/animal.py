import pygame as pg
import random as rnd
import numpy as np
import heapq
import math
from colours import *


# motion direction constants
UP    = 0
RIGHT = 1
DOWN  = 2
LEFT  = 3


class animal(object):
# constructor
    def __init__(self, surface, movementspeed):
        self.surface = surface
        self.ms = movementspeed
        self.wandering = True
        self.eat = False
        self.path = []
        self.targetDistance = 0
        self.target = object
        self.oldPosition = (-1,-1)
    
    # function to calculate distance between two points
    def calculateDistance(self,x1,y1,x2,y2):  
        self.dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
        return self.dist  

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
        moves = ((0,self.ms),(0,-self.ms),(self.ms,0),(-self.ms,0), (self.ms,self.ms), (self.ms,-self.ms), (-self.ms,self.ms), (-self.ms,-self.ms))
        nextMove = moves[rnd.randrange(len(moves))]
        newPosition = (position[0] + nextMove[0],position[1] + nextMove[1])
        return newPosition

        #find nearest food
    def seek(self, targets):
        self.closest = self.scan(targets)

        if self.wandering == False:
            self.path = self.createPath(self.closest)
            self.path.reverse()
            if self.path:
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
    def scan(self, targets):

        aPosition = self.getPosition()
        for target in targets:
            targetPosition = target.rect.center
            self.targetDistance = self.heuristic(aPosition, targetPosition)
            
            if self.targetDistance <= self.sense:
                self.wandering = False
                self.target = target
                return targetPosition
        return
  
    # move animal
    def move(self):
        if self.wandering == True:
            self.dir = self.wander()
            self.rect.x = self.dir[0] % 400
            self.rect.y = self.dir[1] % 400
            
        elif self.wandering == False:
            if self.path:
                self.nextMove = self.path.pop(0)
                self.rect.x = self.nextMove[0]
                self.rect.y = self.nextMove[1]

            else:
                self.eat = True
                self.wandering = True
        
    # draw animal    
    def draw(self):
        sur = self.surface
        rect = self.rect 
        pg.draw.rect(sur, self.colour, rect)

