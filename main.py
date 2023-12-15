import sys
import pygame
from pygame.locals import *

pygame.init()
vec = pygame.math.Vector2

HEIGHT = 600
WIDTH = 1500
ACC = 1
FRIC = -0.12
FPS = 60

FramePerSec = pygame.time.Clock()

displaysurface = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Present Popper")

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((30, 30))
        self.surf.fill((255, 255, 255))
        self.rect = self.surf.get_rect()

        self.pos = vec((10, 100))
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)

    def move(self):
        self.acc = vec(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.acc.x = -ACC
        if pressed_keys[K_d]:
            self.acc.x = ACC

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        hits = pygame.sprite.spritecollide(P1, platforms, False)
        if P1.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -9


class platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill((255, 0, 0))
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))


PT1 = platform()
P1 = Player()

platforms = pygame.sprite.Group()
platforms.add(PT1)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)

camera_offset = vec(0, 0)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                P1.jump()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                P1.jump()

    displaysurface.fill((0, 0, 0))

    P1.move()
    P1.update()

    camera_offset.x += (P1.pos.x - camera_offset.x - WIDTH/2) * 0.05
    camera_offset.y += (P1.pos.y - camera_offset.y - HEIGHT/2) * 0.05
    for entity in all_sprites:
        displaysurface.blit(entity.surf, entity.rect.move(-camera_offset.x, -camera_offset.y))

    pygame.display.update()
    FramePerSec.tick(FPS)
