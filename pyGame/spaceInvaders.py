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
size = (1000,800)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("Invader")

# Define the class Invader which is a sprite
class Invader(pygame.sprite.Sprite):
    # Define the constructor for Invader
    def __init__(self, color, width, height):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(0, 1000)
        self.rect.y = random.randrange(-50,0)
    def update(self):
        self.rect.y = self.rect.y + 1
        # Respawn code
        if self.rect.y > 800:
            self.rect.y = -5
            self.rect.x = random.randrange(0,995)

# Define the class Player which is a sprite
class Player(pygame.sprite.Sprite):
    # Define the constructor for Player
    def __init__(self, color, width, height, speed):
        # Call the sprite constructor
        super().__init__()
        # Create a sprite and fill it with colour
        self.image = pygame.Surface([width, height])
        self.image.fill(color)
        # Set the position of the sprite
        self.rect = self.image.get_rect()
        self.rect.x = 100
        self.rect.y = 20
        # Set speed of the sprite
        self.speed = 0
    # Class update function - runs for each pass through the game loop
    def update(self):
        self.rect.y = self.rect.y + self.speed
        # Respawn code
        if self.rect.y > 800:
            # print("landed")
            self.rect.y = -5
            self.rect.x = random.randrange(0,995)
        
        


# Exit game flag set to false
done = False

# Create a list of the Invader blocks
Invader_group = pygame.sprite.Group()
# Create a list of all sprites
all_sprites_group = pygame.sprite.Group()


# Create the Invaders
number_of_flakes = 50 
for x in range(number_of_flakes):
    my_Invader = Invader(WHITE, 5, 5)
    Invader_group.add(my_Invader)
    all_sprites_group.add(my_Invader)
    
# Create the Player
player = Player(YELLOW, 20, 20, 1)
all_sprites_group.add(player)

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
    # pygame.draw.rect(screen, BLUE, (220,165,200,150))
    # pygame.draw.circle(screen, YELLOW, (40,100),40,0)
    
    # Flip display to reveal new position of objects
    pygame.display.flip()
    
    # The clock ticks over
    clock.tick(60)
    
    # End While End of game loop
pygame.quit()