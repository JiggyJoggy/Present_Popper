import sys
import pygame
from pygame.locals import *
from player import Player, P1, PT1, vec
from game_platform import Platform

pygame.init()

HEIGHT = 800
WIDTH = 1600
FPS = 60

RED = (255, 0, 0)

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Present Popper")

rectangles = []
all_sprites = pygame.sprite.Group(PT1, P1, rectangles)

camera_offset = vec(0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE or event.key == pygame.K_w:
                P1.jump()
        # elif event.type == pygame.MOUSEBUTTONDOWN:
        #     mouse_x, mouse_y = pygame.mouse.get_pos()
        #     new_rect = pygame.Rect(mouse_x, mouse_y, 30, 30)
        #     rectangles.append(new_rect)

    displaysurface.fill((0, 0, 0))

    P1.move()
    P1.update()

    camera_offset.x += (P1.pos.x - camera_offset.x - WIDTH/2) * 0.05
    camera_offset.y += (P1.pos.y - camera_offset.y - HEIGHT/2) * 0.05

    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect.move(-camera_offset.x, -camera_offset.y))

    pygame.display.update()
    FramePerSec.tick(FPS)
