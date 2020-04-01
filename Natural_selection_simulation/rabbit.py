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
SENSE = 5

# rabbit class definition
class rabbit(object):
   
    # constructor
    def __init__(self, surface, startPosX, startPosY, movementspeed):
        self.surface = surface
        self.posX = startPosX
        self.posY = startPosY
        self.ms = movementspeed
        self.wandering = True
        self.target = None
        self.path = []
        self.targetDistance = 0

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
    def seek(self, food):
        self.closest = self.scan(food)

        if self.wandering == False:
            self.path = self.createPath(self.closest)
        elif self.wandering == True:
            return print('searching')

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
    
    def tempName(self, direction):
        if direction == UP:
            return 0,-self.ms
        elif direction == RIGHT:
            return self.ms,0
        elif direction == DOWN:
            return 0, self.ms
        elif direction == LEFT:
            return -self.ms,0


    def heuristic(self,a, b):
        return np.sqrt((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2)

    # create path to set destination
    def createPath(self, destination):
        moves  = [(0,1),(0,-1),(1,0),(-1,0),(1,1),(1,-1),(-1,1),(-1,-1)]
        close_set = set()
        came_from = {}
        start = list(self.getPosition())
        goal = list(destination)
        gscore = {self.getPosition():0}
        fscore = {self.getPosition():self.heuristic(start,goal)}
        oheap = []
        heapq.heappush(oheap,(fscore[self.getPosition()],self.getPosition()))
        while oheap:
            current = heapq.heappop(oheap)[1]
            if current == destination:
                data = []
                while current in came_from:
                    data.append(current)
                    current = came_from[current]
                return data
            close_set.add(current)

            for i,j in moves:
                move = current[0] + i, current[1] + j
                tennative_g_score = gscore [current] + self.heuristic(current,move)
                if move in close_set and tennative_g_score >= gscore.get(move,0):
                    continue
                if tennative_g_score < gscore.get(move,0) or move not in [i[1]for i in oheap]:
                    came_from[move] = current
                    gscore[move] = tennative_g_score
                    fscore[move] = tennative_g_score + self.heuristic(move,destination)
                    heapq.heappush(oheap,(fscore[move],move))
        return False


    #def createPath(self, destination):
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
            elif self.dir == RIGHT:
                self.posX += self.ms
            elif self.dir == DOWN:
                self.posY += self.ms
            elif self.dir == LEFT:
                self.posX -= self.ms
        elif self.wandering == False:
            self.path.append(self.getPosition())
            self.path.reverse()
            print(self.path)
            self.wandering = True

        
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


