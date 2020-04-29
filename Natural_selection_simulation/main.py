import pygame as pg
import carrot as crt
import rabbit as rb
import random as rnd
import wolf as wlf
from colours import *

# screen size and game speed
WIDTH      = 400
HEIGHT     = 400
SPEED      = 20
RABBIT_MOVEMENT_SPEED = 3
WOLF_MOVEMENT_SPEED = 3

pg.init()

# set up the drawing window
clock = pg.time.Clock()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Simulation')

#set up food and animals
turn = 1

food = [crt.carrot(screen, 1, WIDTH - 11, 1, HEIGHT - 11) for i in range (400)]
rabbits = [rb.rabbit(screen, RABBIT_MOVEMENT_SPEED, rnd.randint(0,380),rnd.randint(0,380)) for i in range (40)]
wolfs = [wlf.wolf(screen, WOLF_MOVEMENT_SPEED, 200, 200) for i in range (4)]

def createFood(value):
    for i in range(value):
        food.append(crt.carrot(screen, 1, WIDTH - 11, 1, HEIGHT - 11))

# draw screen with objects 
def drawScreen(surface):
    surface.fill(GREEN_DARK)

    for carrot in food:
        carrot.draw()
    for rabbit in rabbits:
        rabbit.draw()
    for wolf in wolfs:
        wolf.draw()

    pg.display.update()  

running = True
while running:
  
    # game speed
    clock.tick(SPEED)

    turn += 1

    if turn%100 == 0:
        createFood(200)

    # draw food, rabbit, screen
    drawScreen(screen)

    for wolf in wolfs:
        if wolf.energy <= 0:
            wolfs.remove(wolf)
            continue
        elif wolf.energy > 0.75*wolf.maxEnergy:
            wolf.reproduce(wolfs, wlf.wolf)

        wolf.move()
        wolf.trail += 1
        wolf.checkTarget()

        if wolf.getWandering() == True:
            wolf.seek(rabbits)

        eat = wolf.rect.collidelist(rabbits)
        if eat != -1:
            rabbits[eat].setEaten = True
            wolf.energy += rabbits[eat].energyRep
            if wolf.energy > wolf.maxEnergy:
                wolf.energy = wolf.maxEnergy
            rabbits.pop(eat)

    # move rabbits
    for rabbit in rabbits:
        #rabbit.age += 1
        #if rabbit.age > rabbit.maxAge:
        #    rabbits.remove(rabbit)
        #    continue
        if rabbit.energy <= 0:
            rabbit.setEaten = True
            rabbits.remove(rabbit)
            continue
        elif rabbit.energy > 0.50*rabbit.maxEnergy:
            rabbit.reproduce(rabbits, rb.rabbit)
        rabbit.move()
        if rabbit.getWandering() == True:
            rabbit.seek(food)

        eat = rabbit.rect.collidelist(food)
        if eat != -1:
            rabbit.energy += food[eat].energyRep
            if rabbit.energy > rabbit.maxEnergy:
                rabbit.energy = rabbit.maxEnergy
            food.pop(eat)

    # quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
            pg.quit()

