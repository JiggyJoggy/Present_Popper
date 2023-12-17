# main.py

import pygame
import sys
from pygame.locals import QUIT
from player import Player, vec
from level import Level, Platform
from level_data import level1

pygame.init()

HEIGHT = 600
WIDTH = 1000
FPS = 60
COLOR = (100, 23, 238)

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Present Popper")

platforms = pygame.sprite.Group()

current_level = level1.create_level(WIDTH, HEIGHT, COLOR)  # Set the initial level

P1 = Player(platforms)
all_sprites = pygame.sprite.Group(current_level, P1)

# Set the initial camera position to be centered on the player
camera_offset = vec((WIDTH - P1.rect.width) // 2, (HEIGHT - P1.rect.height) // 2)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                P1.jump()

    displaysurface.fill((0, 0, 0))

    current_level.draw_background(displaysurface)

    P1.move()
    P1.update()

    # Adjust the camera position based on player movement
    camera_offset.x += (P1.pos.x - camera_offset.x - WIDTH/2) * 0.05

    # Keep the camera within bounds to avoid going off-screen
    camera_offset.x = max(0, min(WIDTH - P1.rect.width, camera_offset.x))
    camera_offset.y = max(0, min(HEIGHT - P1.rect.height, camera_offset.y))

    all_sprites = pygame.sprite.Group(current_level, P1)

    current_level.update_background()

    for entity in all_sprites:
        if isinstance(entity, Player):
            displaysurface.blit(entity.image, entity.rect.move(-camera_offset.x, -camera_offset.y))
        elif isinstance(entity, Level):
            displaysurface.blit(entity.image, entity.rect.move(-camera_offset.x, -camera_offset.y))

            # Iterate through endpoints and render them
            for endpoint in entity.endpoints:
                displaysurface.blit(endpoint.image, endpoint.rect.move(-camera_offset.x, -camera_offset.y))

            # Check for collisions with the endpoint
            if pygame.sprite.spritecollide(P1, entity.endpoints, False):
                # Handle endpoint, start next level or take appropriate action
                print("Endpoint reached! Start the next level.")

    pygame.display.update()
    FramePerSec.tick(FPS)
