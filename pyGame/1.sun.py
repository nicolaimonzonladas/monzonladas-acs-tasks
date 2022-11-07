import pygame

# -- Global Constants

# -- Colours



BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
# YELLOW = (y,y,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (500,500)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

circX = 360
circY = 240

y = 255

sunset = False


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
    
    # -- Screen background is BLACK
    screen.fill (BLACK)
    
    # -- Draw here
    YELLOW = (y,y,0)
    pygame.draw.rect(screen, YELLOW, (0,0,500,500))
    pygame.draw.circle(screen, WHITE, (circX,circY),20,0)
    
    
    # if  circX == 674 or y <=6:
    #     sunset = True
    # if circX == 6 or y >=249:
    #     sunset = False
    
    
    if sunset == True:
        circX += 2
        if circX < 250:
            circY += 2
        else:
            circY -= 2
    else:
        # SUNSET IS FALSE, THEREFORE SUNRISE RISING
        circX -= 2
        if circX < 250:
            circY -= 2
        else:
            circY += 2
    
    if circY > 249:
        sunset = True
    else:
        sunset = False
    
    
    
    
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()