import pygame

# -- Global Constants

# -- Colours

WHITE = (255,255,255)
BLACK = (0,0,0)
ORANGE = (255,150,0)
BLUE = (50,50,255)
GREEN = (50,155,0)
# YELLOW = (y,y,0)

# -- Initialise PyGame
pygame.init()

# -- Blank Screen
size = (640,240)
screen = pygame.display.set_mode(size)

# -- Title of new window/screen
pygame.display.set_caption("Sun")

# -- Exit game flag set to false
done = False

circX = 0
circY = 0

y = 0

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
    screen.fill(BLACK)
    
    # -- Draw here
    YELLOW = (y,y,0)
    pygame.draw.rect(screen, YELLOW, (0,0,700,500))
    pygame.draw.circle(screen, WHITE, (circX,int(((3/1280)*(circX - 320)**2 ))),20,0)
    pygame.draw.circle(screen, GREEN, (320, 300), 100, 0)    
    pygame.draw.rect(screen, BLUE, (300, 180, 40, 40))
    pygame.draw.polygon(screen, BLUE, ((285,180), (355,180), (320,160)))
   
    circX += 1

    if circX > 640:
        circX = 0
   
    # circX += step
    # if circX > 402 or circX < 80 :
    #     step = -step 
        
    # circY += stepY
    # if circY > 402 or circY < 80 :
    #     stepY = -stepY
    
    # if circY > 250:
    #     if y > 5:
    #         y -= 5
    # elif circY < 250:
    #     if y < 250:
    #         y += 5
    
    # -- flip display to reveal new position of objects
    pygame.display.flip()
    
    # - The clock ticks over
    clock.tick(120)
    
    if circX > 0 and circX < 320:
        y += 0.7
    elif circX > 320:
        y -= 0.7
    elif circX < 5:
        y = 0
    
    #End While - End of game loop
    
pygame.quit()