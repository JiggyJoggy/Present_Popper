# main.py
import pygame
from pygame.locals import *
from player import Player
from level import Level
from level import Platform

pygame.init()

HEIGHT = 1000
WIDTH = 1000
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Present Popper")

level = Level(WIDTH, HEIGHT, (0, 0, 0), 0, 0)

# Create instances of Platform directly within Level
platform1 = level.add_platform(Platform(200, 20, (255, 0, 0), WIDTH / 2, HEIGHT - 10))
platform2 = level.add_platform(Platform(150, 20, (255, 0, 0), WIDTH / 4, HEIGHT - 50))

all_sprites = pygame.sprite.Group()
all_sprites.add(level.platforms)

# Create the Player instance after initializing the platforms
P1 = Player(level.platforms)
all_sprites.add(P1)  # Add the player to the sprite group

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                P1.jump()

    displaysurface.fill((0, 0, 0))

    P1.move()
    P1.update()

    all_sprites.draw(displaysurface)

    pygame.display.update()
    FramePerSec.tick(FPS)
