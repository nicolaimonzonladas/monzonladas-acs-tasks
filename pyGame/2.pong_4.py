# Imports
import pygame
import random

# Initialise PyGame
pygame.init()

# Global Constants

# Ball
ballWidth = 20
xVal = 50
yVal = 200
xDir = 6
yDir = 6

# Canvas setup
screenW = 800
screenH = 500

# Paddle sizing
paddWidth = 15
paddLength = 60

# Paddle (starting) locations
p1PadX = 0
p1PadY = 20

p2PadX = screenW -20
p2PadY = 20


# Score, fonts
score = 0
font = pygame.font.Font('freesansbold.ttf', 32)


# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)






# Blank Screen
size = (screenW,screenH)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("Pong")

# Exit game flag set to false
done = False

# Manages how fast screen refreshes
clock = pygame.time.Clock()


### Game Loop

while not done:
    # User input and controls, code to move up and down
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                # p1PadY = p1PadY - 20
                print("up")
            elif event.key == pygame.K_DOWN:
                # p1PadY = p1PadY + 20
                print("down")
    # Code that somehow makes moving smooth
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        if p1PadY < 0:
            p1PadY = 0
        else:
            p1PadY = p1PadY - 7
    if keys[pygame.K_DOWN]:
        if p1PadY >= screenH - paddLength:
            p1PadY = screenH - paddLength
        else:
            p1PadY = p1PadY + 7
    
    
    # Game logic (goes after this comment)
    
    # Bounce collision detection on all sides of canvas.
    # Bounces by multiplying matching direction by -1
    # To account for top left coord being used for ball, 
    # ballWidth has been subtracted from right and lower sides' detection.
    if yVal <= 0:
        yDir = yDir * -1
    
    if yVal >= screenH-ballWidth:
        yDir = yDir * -1
    
    if xVal <= 0:
        xDir = xDir * -1
    
    if xVal >= screenW-ballWidth-paddWidth: # - paddle width to account for computer, that never loses
        xDir = xDir * -1
    
    # Moves the ball by xDir and yDir each frame
    xVal = xVal + xDir
    yVal = yVal + yDir
    
    # Checks collision with paddle and ball
    if xVal <= paddWidth and yVal <= p1PadY + paddLength and yVal >= p1PadY:
        xDir = xDir * -1 # Bounce collision
        xDir = xDir
        yDir = yDir 
        score += 1 # Adds 1 to score
    elif xVal < 2: # I don't know why<2, but works. Tried xVal==0 but score increased by more than 1.
        score -= 1 # Removes 1 from score
        
    # P2 (Computer) movement calculations
    if p2PadY < 0:
        p2PadY = 0
    else:
        p2PadY  = ((yVal)- (paddLength/2)+(ballWidth/2)) 
        print((screenW - xVal)/10)
    if p2PadY >= screenH - paddLength:
        p2PadY = screenH - paddLength
    else:
        p2PadY  = ((yVal)- (paddLength/2)+(ballWidth/2)) 
        print((screenW - xVal)/10)
    
    # Ignore: (1 + (xVal /100))/10 + (1-0.8684000000000001)
    # - (screenW - xVal)/10

    
    # Screen background is BLACK
    screen.fill (BLACK)
    
    # Ball and paddles drawn here
    pygame.draw.rect(screen, BLUE, (xVal,yVal,ballWidth,ballWidth))
    pygame.draw.rect(screen, WHITE, (p1PadX,p1PadY,paddWidth,paddLength))
    pygame.draw.rect(screen, WHITE, (p2PadX,p2PadY,paddWidth,paddLength))


    # Score is rendered
    score1 = font.render("Score : " + str(score), True, (255, 255, 255))
    screen.blit(score1, (100, 50))
    
    # Flip display to reveal new position of objects
    pygame.display.flip()
    
    # The clock ticks over
    clock.tick(60)
    
    #End While - End of game loop
pygame.quit()