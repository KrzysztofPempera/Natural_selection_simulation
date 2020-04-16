import pygame as pg
import carrot as crt
import rabbit as rb
from colours import *

# screen size and game speed
WIDTH      = 400
HEIGHT     = 400
SPEED      = 30
MOVEMENT_SPEED = 2

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
rabbits = [rb.rabbit(screen, MOVEMENT_SPEED) for i in range (100)]

# draw screen with objects 
def drawScreen(surface):
    surface.fill(GREEN_DARK)

    for i in range(len(food)):
        food[i].draw()
    for i in range(len(rabbits)):
        rabbits[i].draw()

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

