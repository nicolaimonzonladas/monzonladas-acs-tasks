import pygame
import random
import math

# Global Constants

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# Initialise PyGame
pygame.init()

# Blank Screen
size = (800,500)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("Snow")


# "Pile up" effect for snow - FOR SOME REASON NOT WORKING.
def pileUp(x):
    pygame.draw.rect(screen, WHITE, (x,495,5,5))
    # print("test")

# Define the class snow which is a sprite
class Snow(pygame.sprite.Sprite):
    # Define the constructor for snow
    def __init__(self, color, width, height, speed):
        # Call the sprite contrsuctor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width,height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 800)
        self.rect.y = random.randrange(0,500)
        # Set speed of the sprite
        self.speed = speed
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
        # Respawn code
        if self.rect.y > 500:
            pileUp(self.rect.x) # not working
            # print("landed")
            self.rect.y = -5
        

# Exit game flag set to false
done = False

# Create a list of the snow blocks
snow_group = pygame.sprite.Group()
# Create a lsit of all sprites
all_sprites_group = pygame.sprite.Group()

# Create the snowflakes
number_of_flakes = 50 
for x in range(number_of_flakes):
    my_snow = Snow(WHITE, 5, 5, random.randrange(1,5))
    snow_group.add(my_snow)
    all_sprites_group.add(my_snow)

# Manages how fast screen refreshes
clock = pygame.time.Clock()


### Game Loop


while not done:
    # User input and controls
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        # End If
    # Next event
    
    # Game logic goes after this comment
    
    all_sprites_group.update()
    # Screen background is BLACK
    screen.fill(BLACK)
    
    # Draw here
    
    all_sprites_group.draw(screen)
    
    # Flip display to reveal new position of objects
    pygame.display.flip()
    
    # The clock ticks over
    clock.tick(60)
    
    # End While End of game loop
pygame.quit()