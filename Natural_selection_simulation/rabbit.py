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
        self.eat = False
        self.path = []
        self.targetDistance = 0

        self.colour = WHITE
    
# function to calculate distance between two points
    def calculateDistance(self,x1,y1,x2,y2):  
        self.dist = math.sqrt((x2 - x1)**2 + (y2 - y1)**2)  
        return self.dist  

    # get rabbits position
    def getPosition(self):
        return self.posX, self.posY

    # get rabbits status
    def getWandering(self):
        return self.wandering

    #find nearest food
    def seek(self, food):
        self.closest = self.scan(food)

        if self.wandering == False:
            self.path = self.createPath(self.closest)
            self.path.reverse()
        elif self.wandering == True:
            print("searching..")
    # scan for closest food
    def scan(self, food):

        rPosition = self.getPosition()
        for carrot in food:
            cPositionX = carrot.posX
            cPositionY = carrot.posY
            self.targetDistance = self.calculateDistance(rPosition[0], rPosition[1],cPositionX, cPositionY)
            
            if self.targetDistance <= SENSE:
                self.wandering = False
                return cPositionX,cPositionY
        return
   
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


    #def createPathbts(self, destination):
    #    visited = set([destination])
    #    tempQ = collections.deque([[self.getPosition()]])
    #    while tempQ:
    #        path = tempQ.popleft()
    #        x, y = path[-1]
    #        if path[-1] == destination:
    #            return path
    #        for x2, y2 in ((x+1,y), (x-1,y), (x,y+1), (x,y-1)):
    #            if (x2, y2) not in visited:
    #                tempQ.append(path + [(x2, y2)])
    #                visited.add((x2, y2))
    #    print('breakpoint')


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
                self.posY = self.posY % 400
            elif self.dir == RIGHT:
                self.posX += self.ms
                self.posX = self.posX % 400
            elif self.dir == DOWN:
                self.posY += self.ms
                self.posY = self.posY % 400
            elif self.dir == LEFT:
                self.posX -= self.ms
                self.posX = self.posX % 400

        elif self.wandering == False:
            if self.path:
                self.nextMove = self.path.pop(0)
                self.posX = self.nextMove[0]
                self.posY = self.nextMove[1]
            else:
                self.eat = True
                self.wandering = True
        
        # fix out of bounds behavior
        #if self.posX >= 400:
        #    self.posX = self.posX - 400
        #if self.posY >= 400:
        #    self.posY = self.posY - 400

    # draw rabbit    
    def draw(self):
        sur = self.surface

        rPosition = self.getPosition()

        pg.draw.rect(sur,self.colour,(rPosition[0],rPosition[1],BLOCK_SIZE,BLOCK_SIZE))


