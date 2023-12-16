# main.py
import pygame
import sys
from pygame.locals import QUIT
from player import Player
from level import Level, Platform
from player import vec

pygame.init()

HEIGHT = 600
WIDTH = 1000
FPS = 60
RED = (255, 0, 0)

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Present Popper")

platforms = pygame.sprite.Group()
PT1 = Level(WIDTH, 20, RED, 0, HEIGHT - 20, 500, 100, 'sprites/background/mountains.jpeg')
PT1.add_platform(Platform(WIDTH, 20, RED, WIDTH/2, HEIGHT - 20))
platforms.add(PT1)
P1 = Player(platforms)
all_sprites = pygame.sprite.Group(PT1, P1)

print("Endpoint location:", PT1.end_point.rect.topleft)

camera_offset = vec(0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                P1.jump()

    displaysurface.fill((0, 0, 0))
    displaysurface.blit(PT1.background, PT1.rect)

    P1.move()
    P1.update()

    camera_offset.x += (P1.pos.x - camera_offset.x - WIDTH/2) * 0.05
    camera_offset.y += (P1.pos.y - camera_offset.y - HEIGHT/2) * 0.05

    all_sprites = pygame.sprite.Group(PT1, P1)

    for entity in all_sprites:
        if isinstance(entity, Player):
            displaysurface.blit(
                entity.image, entity.rect.move(
                    -camera_offset.x, -camera_offset.y))
        elif isinstance(entity, Level):
            displaysurface.blit(
                entity.image, entity.rect.move(
                    -camera_offset.x, -camera_offset.y))

            # Iterate through endpoints and render them
            for endpoint in entity.endpoints:
                displaysurface.blit(
                    endpoint.image, endpoint.rect.move(
                        -camera_offset.x, -camera_offset.y))

            # Check for collisions with the endpoint
            if pygame.sprite.spritecollide(P1, entity.endpoints, False):
                # Handle endpoint, start next level or take appropriate action
                print("Endpoint reached! Start the next level.")

    pygame.display.update()
    FramePerSec.tick(FPS)
