import pygame

# Global Constants

# Colours
BLACK = (0,0,0)
WHITE = (255,255,255)
BLUE = (50,50,255)
YELLOW = (255,255,0)

# Initialise PyGame
pygame.init()

# Blank Screen
size = (600,400)
screen = pygame.display.set_mode(size)

# Title of new window/screen
pygame.display.set_caption("My Window")

import pygame

# Platform class
class Platform(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.Surface((20, 5))
        self.image.fill((0, 255, 0))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

# Player class
class Player(pygame.sprite.Sprite):
    def __init__(self, x, y, spriteGroup):
        super().__init__()
        self.image = pygame.Surface((20, 20))
        self.image.fill((255, 255, 255))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 5
        self.jumpSpeed = 2
        self.gravity = 0.5
        self.isJumping = False
        self.collissionGroup = spriteGroup

    def update(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]:
            self.rect.x -= self.speed
        if keys[pygame.K_RIGHT]:
            self.rect.x += self.speed
        if keys[pygame.K_UP] and not self.isJumping:
            self.isJumping = True
            self.rect.y -= self.jumpSpeed
        if self.isJumping:
            self.rect.y += self.gravity
            self.gravity += 0.5
            collision = pygame.sprite.spritecollide(self, self.collissionGroup, False)
            if collision:
                if self.rect.y > 300:
                    self.rect.y = 300
                self.isJumping = False
                self.gravity = 0.5
                self.rect.bottom = collision[0].rect.top
                


# Exit game flag set to false
done = False

# Create all sprites pygame group, and platforms group
allSpritesGroup = pygame.sprite.Group()
allPlatformsGroup = pygame.sprite.Group()



# Create the player, and add the the all sprites pygame group
player = Player(50, 300, allPlatformsGroup)
allSpritesGroup.add(player)

# Create the platforms here (I only did 2) and add to platforms and all sprites pygame groups

platform1 = Platform(100, 200)
platform2 = Platform(200, 100)
allPlatformsGroup.add(platform1, platform2)
allSpritesGroup.add(platform1, platform2)


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
    
    # Screen background is BLACK
    screen.fill (BLACK)
    
    # Draw here
    # pygame.draw.rect(screen, BLUE, (220,165,200,150))    
    player.update()
    allPlatformsGroup.update()
    screen.blit(player.image, player.rect)
    allPlatformsGroup.draw(screen)


    # Flip display to reveal new position of objects
    pygame.display.flip()
    
    # The clock ticks over
    clock.tick(60)
    
    # End While End of game loop
pygame.quit()