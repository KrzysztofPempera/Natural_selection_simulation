import pygame as pg
import carrot as crt
import rabbit as rb
import wolf as wlf
from colours import *

# screen size and game speed
WIDTH      = 400
HEIGHT     = 400
SPEED      = 30
RABBIT_MOVEMENT_SPEED = 3
WOLF_MOVEMENT_SPEED = 2

pg.init()

# set up the drawing window
clock = pg.time.Clock()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Simulation')

#set up food and animals

food = [crt.carrot(screen, 1, WIDTH - 11, 1, HEIGHT - 11) for i in range (400)]
rabbits = [rb.rabbit(screen, RABBIT_MOVEMENT_SPEED, id = i) for i in range (30)]
wolfs = [wlf.wolf(screen, WOLF_MOVEMENT_SPEED) for i in range (3)]

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

    # draw food, rabbit, screen
    drawScreen(screen)

    for wolf in wolfs:
        wolf.move()
        if wolf.getWandering() == True:
            wolf.seek(rabbits)

        eat = wolf.rect.collidelist(rabbits)
        if eat != -1:
            rabbits.pop(eat)

    # move rabbits
    for rabbit in rabbits:
        rabbit.move()
        if rabbit.getWandering() == True:
            rabbit.seek(food)

        eat = rabbit.rect.collidelist(food)
        if eat != -1:
            food.pop(eat)

    # quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
            pg.quit()

