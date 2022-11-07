import pygame

# -- Global Constants

# -- Colours

BLACK = (0,0,0)
ORANGE = (255,150,0)
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
circY = 230

y = 255

step = 2
stepY = 2


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
    pygame.draw.circle(screen, ORANGE, (circX,circY),20,0)
    
   
    circX += step
    if circX > 402 or circX < 80 :
        step = -step 
        
    circY += stepY
    if circY > 402 or circY < 80 :
        stepY = -stepY
    
    if circY > 250:
        if y > 5:
            y -= 5
    elif circY < 250:
        if y < 250:
            y += 5
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(60)
    
    if y > 250:
        y = 250
    elif y < 5:
        y = 0
    
    #End While - End of game loop
    
pygame.quit()