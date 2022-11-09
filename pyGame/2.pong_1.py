import pygame
import random

# -- Global Constants

ballWidth = 20
xVal = 50
yVal = 200

xDir = 4
yDir = 8

screenW = 500
screenH = 500

randomColor = 255

# -- Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)



# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (screenW,screenH)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Pong")

# -- Exit game flag set to false
done = False

# -- Manages how fast screen refreshes
clock = pygame.time.Clock()


### -- Game Loop


while not done:
    # -- User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        #End If
    #Next event
    
    # -- Game logic goes after this comment
    
    if yVal < 0:
        yDir = yDir * -1
    
    if yVal > screenH-ballWidth:
        yDir = yDir * -1
    
    if xVal < 0:
        xDir = xDir * -1
    
    if xVal > screenW-ballWidth:
        xDir = xDir * -1
    
    xVal = xVal + xDir
    yVal = yVal + yDir
    
        
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    
    RANDOMCOLOR = (random.randint(0,255),random.randint(0,255),random.randint(0,255))
    print()
    pygame.draw.rect(screen, RANDOMCOLOR, (xVal,yVal,ballWidth,ballWidth))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()