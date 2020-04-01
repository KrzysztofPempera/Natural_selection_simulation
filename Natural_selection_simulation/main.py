import pygame as pg
import carrot as crt
import rabbit as rb
from colours import *

# screen size and game speed
WIDTH      = 400
HEIGHT     = 400
SPEED      = 100
SPEED_TICK = 2
ROWS       = 20

pg.init()

# set up the drawing window
clock = pg.time.Clock()
screen = pg.display.set_mode([WIDTH, HEIGHT])
pg.display.set_caption('Simulation')

# set up food and rabbit
food = [crt.carrot(screen, 1, WIDTH - 20, 1, HEIGHT - 20) for i in range (200)]
rabbit = rb.rabbit(screen, 200, 200, 1)

# draw grid 
#def drawGrid(surface, rows, width):
#    gridSize = 20

#    x = 0
#    y = 0

#    for i in range(rows):
#        x = x + gridSize
#        y = y + gridSize

#        pg.draw.line(surface, (WHITE), (x,0),(x,width))
#        pg.draw.line(surface, (WHITE), (0,y),(width,y))

# draw screen with objects 
def drawScreen(surface):
    surface.fill(GREEN_DARK)

    for i in range(len(food)):
        food[i].draw()

    rabbit.draw()

    pg.display.flip()  
    pg.display.update()

running = True
while running:
  
    # game speed
    clock.tick(SPEED)

    # draw food, rabbit, screen
    drawScreen(screen)

    # move rabbits
    rabbit.move()

    for carrot in food:
        if rabbit.getPosition() == carrot.getPosition():
            food.remove(carrot)
            print('deleted')

    # quit
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 
            pg.quit()

