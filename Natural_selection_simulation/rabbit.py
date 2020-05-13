import pygame as pg
import math
import random as rnd
from animal import animal
from colours import *
import json

with open('para.json', 'r') as para:
    config = json.load(para)

# block size
BLOCK_SIZE = 4

# rabbit class definition
class rabbit(animal):
   
    # constructor
    def __init__(self, surface, movementspeed, posx, posy, sense):
        animal.__init__(self, surface, movementspeed, sense)
        self.posX = posx
        self.posY = posy
        self.colour = WHITE
        self.dead = False
        self.energy = config['RABBIT_ENERGY']
        self.maxEnergy = config['RABBIT_MAX_ENERGY']
        self.energyRep = config['RABBIT_ENERGY_REP']
        self.reproduction = config['RABBIT_REPRODUCTION']
        self.maxAge = 200
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
    