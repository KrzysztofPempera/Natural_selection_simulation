import pygame as pg
import carrot as crt
import rabbit as rb
import wolf as wlf
from colours import *

# screen size and game speed
WIDTH      = 400
HEIGHT     = 400
SPEED      = 30
RABBIT_MOVEMENT_SPEED = 2
WOLF_MOVEMENT_SPEED = 3
# declare food positions array
food = []
#foodPosition = [[-1 for i in range (400)] for j in range(400)]

pg.init()

# set up the drawing window
clock = pg.time.Clock()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Simulation')


# set up food and rabbit
for i in range (400):
    food.append(crt.carrot(screen, 1, WIDTH - 11, 1, HEIGHT - 11))
#    foodPosition[food[i].posX][food[i].posY] = i
#food = [crt.carrot(screen, 170, 230, 170 , 230) for i in range (5)]
#rabbits = [rb.rabbit(screen, 200, 200, MOVEMENT_SPEED) for i in range (10)]
rabbits = [rb.rabbit(screen, RABBIT_MOVEMENT_SPEED, id = i) for i in range (10)]
wolfs = [wlf.wolf(screen, WOLF_MOVEMENT_SPEED) for i in range (2)]

# draw screen with objects 
def drawScreen(surface):
    surface.fill(GREEN_DARK)

    for carrot in food:
        carrot.draw()
    for rabbit in rabbits:
        rabbit.draw()
    for wolf in wolfs:
        wolf.draw()

    pg.display.flip()  

running = True
while running:
  
    # game speed
    clock.tick(SPEED)

    # draw food, rabbit, screen
    drawScreen(screen)

    # move rabbits
    for rabbit in rabbits:
        rabbit.move()
        if rabbit.getWandering() == True:
            rabbit.seek(food)
        elif rabbit.getEat() == True:
            for carrot in food:
                if rabbit.getPosition() == carrot.getPosition():
                    food.remove(carrot)
                    break
            rabbit.eat = False
            rabbit.wandering = True

    for wolf in wolfs:
        wolf.move()
        if wolf.getWandering() == True:
            wolf.seek(rabbits)
        elif wolf.getEat() == True:
            if wolf.getPosition() == rabbits[wolf.target].getPosition():
                rabbits.pop(wolf.target)
            wolf.eat = False
            wolf.wandering = True
            wolf.target = -1
            #temp = rabbit.getPosition()
            #eat = foodPosition[temp[0]][temp[1]]
            #food.pop(eat)
            #foodPosition[temp[0]][temp[1]] = -1
            #rabbit.eat = False
            #rabbit.wandering = True

    # quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
            pg.quit()

