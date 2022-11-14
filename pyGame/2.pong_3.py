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

paddWidth = 15
paddLength = 60

p1PadX = 0
p1PadY = 20

p2PadX = 0
p2PadY = 20

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
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # p1PadY = p1PadY - 20
                print("test")
            elif event.key == pygame.K_DOWN:
                # p1PadY = p1PadY + 20
                print("test")
            #End if
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        p1PadY = p1PadY - 5
        # print("hlelo")
    if keys[pygame.K_DOWN]:
        p1PadY = p1PadY + 5
    
        #End if
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

    pygame.draw.rect(screen, BLUE, (xVal,yVal,ballWidth,ballWidth))
    pygame.draw.rect(screen, WHITE, (p1PadX,p1PadY,paddWidth,paddLength))

    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()