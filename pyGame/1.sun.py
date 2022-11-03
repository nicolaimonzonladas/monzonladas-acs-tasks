import pygame

# -- Global Constants

# -- Colours

y = 255

BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
# YELLOW = (y,y,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,480)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("My Window")

# -- Exit game flag set to false
done = False

circX = 40
circY = 100

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
    pygame.draw.rect(screen, YELLOW, (0,0,640,480))
    pygame.draw.circle(screen, WHITE, (circX,circY),40,0)
    
    

    
    if sunset == True:
        circX += 5
        circY += 5
        y = y + 5
    else:
        circX -= 5
        circY -= 5
        y = y - 5
    
    circX += 5
    
    
    if circX == 680 or y <=6:
        sunset = True
        
    
    
    # if y <= 6:
    #     y = 255
        
    # y = y - 5
    
    
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()