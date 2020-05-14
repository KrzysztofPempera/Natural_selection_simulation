import pygame as pg
import math
import numpy as np
from animal import animal
from colours import *
from rabbit import rabbit
import json

with open('para.json', 'r') as para:
    config = json.load(para)

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
        self.energy = config['WOLF_ENERGY']
        self.maxEnergy = config['WOLF_MAX_ENERGY']
        self.reproduction = config['WOLF_REPRODUCTION']
        self.maxAge = config['WOLF_MAX_AGE']
        self.rect = pg.Rect(self.posX, self.posY, BLOCK_SIZE, BLOCK_SIZE)
