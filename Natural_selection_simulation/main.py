import pygame as pg
import carrot as crt
import rabbit as rb
import random as rnd
import wolf as wlf
import math as math
import csv
import json
from colours import *

with open('para.json', 'r') as para:
    config = json.load(para)

# screen size and game speed
WIDTH      = 400
HEIGHT     = 400
SPEED      = 20
RABBIT_MOVEMENT_SPEED = config['RABBIT_MOVEMENT_SPEED']
WOLF_MOVEMENT_SPEED = config['WOLF_MOVEMENT_SPEED']
WOLF_SENSE = config['WOLF_SENSE']
RABBIT_SENSE = config['RABBIT_SENSE']
CARROT_REP = config['CARROT_REP']

pg.init()

# set up the drawing window
clock = pg.time.Clock()
screen = True

#set up food and animals
turn = 1
food = [crt.carrot(screen, 1, WIDTH - 11, 1, HEIGHT - 11) for i in range (400)]
rabbits = [rb.rabbit(screen, RABBIT_MOVEMENT_SPEED, rnd.randint(0,380),rnd.randint(0,380), RABBIT_SENSE) for i in range (40)]
wolfs = [wlf.wolf(screen, WOLF_MOVEMENT_SPEED, 200, 200, WOLF_SENSE) for i in range (4)]
wolfCount = []
rabbitCount = []
foodCount = []

def createFood(value):
    for i in range(value):
        food.append(crt.carrot(screen, 1, WIDTH - 11, 1, HEIGHT - 11))

def createReport(elapsedTime, wolfCount, rabbitCount): 
    with open('result.csv', 'a') as result:
        result.write(str(turn))
        result.write("\n")

def getCounts():
    return wolfCount, rabbitCount, foodCount

def start():
    global turn, CARROT_REP, wolfCount, rabbitCount, foodCount
    running = True
    while running:
  
        # game speed
        clock.tick(SPEED)
        print("TURN: ",turn)
        turn += 1
        
        createFood(CARROT_REP)


        for wolf in wolfs:
            if wolf.energy <= 0:
                wolfs.remove(wolf)
                continue
            elif wolf.energy > wolf.reproduction*wolf.maxEnergy:
                wolf.reproduce(wolfs, wlf.wolf)

            wolf.move()
            wolf.age += 1
            if wolf.age >=wolf.maxAge:
                wolfs.remove(wolf)
                continue
            if wolf.getWandering() == True:
                wolf.seek(rabbits)

            eat = wolf.rect.collidelist(rabbits)
            if eat != -1:
                rabbits[eat].dead = True
                wolf.energy += rabbits[eat].energyRep
                if wolf.energy > wolf.maxEnergy:
                    wolf.energy = wolf.maxEnergy
                rabbits.pop(eat)

        # move rabbits
        for rabbit in rabbits:

            if rabbit.energy <= 0:
                rabbit.dead = True
                rabbits.remove(rabbit)
            elif rabbit.energy > rabbit.reproduction*rabbit.maxEnergy:
                rabbit.reproduce(rabbits, rb.rabbit)

            rabbit.move()

            if rabbit.wandering == True:
                rabbit.seek(food)

            eat = rabbit.rect.collidelist(food)
            if eat != -1:
                food[eat].dead = True
                rabbit.energy += food[eat].energyRep
                if rabbit.energy > rabbit.maxEnergy:
                    rabbit.energy = rabbit.maxEnergy
                food.pop(eat)
        
        wolfCount.append(len(wolfs))
        rabbitCount.append(len(rabbits))
        foodCount.append(len(food))

        # quit
        if len(rabbits) == 0 or len(wolfs) == 0:
            running = False
            elapsedTime = pg.time.get_ticks()
            wolfCountRep = len(wolfs)
            rabbitCountRep = len(rabbits)
            pg.quit()
            createReport(elapsedTime,wolfCountRep,rabbitCountRep)
start()