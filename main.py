import sys
import pygame
from pygame.locals import *
from player import Player
from game_platform import Platform

pygame.init()

HEIGHT = 1000
WIDTH = 1000
FPS = 60
RED = (255, 0, 0)

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Present Popper")

platforms = pygame.sprite.Group()
PT1 = Platform()
platforms.add(PT1)
P1 = Player(platforms)  # Pass the platforms group to the Player class

all_sprites = pygame.sprite.Group(PT1, P1)

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

    P1.move()
    P1.update()

    camera_offset.x += (P1.pos.x - camera_offset.x - WIDTH/2) * 0.05
    camera_offset.y += (P1.pos.y - camera_offset.y - HEIGHT/2) * 0.05
    for entity in all_sprites:
        if isinstance(entity, Player):
            displaysurface.blit(entity.image, entity.rect)
        elif isinstance(entity, Platform):
            displaysurface.blit(entity.surf, entity.rect)

    pygame.display.update()
    FramePerSec.tick(FPS)
