import pygame
from pygame.locals import *
from game_platform import Platform
from physics import Object

vec = pygame.math.Vector2

HEIGHT = 800
WIDTH = 1600

ACC = 1
FRIC = -0.12
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Player(Object):
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

        # if self.pos.x > WIDTH: # Keeps it in the border we have set with WIDTH
        #     self.pos.x = 0
        # if self.pos.x < 0:
        #     self.pos.x = WIDTH

    def jump(self):
        hits = pygame.sprite.spritecollide(self, platforms, False)
        if hits:
            self.vel.y = -9

PT1 = Platform()
P1 = Player()
platforms = pygame.sprite.Group()
platforms.add(PT1)

all_sprites = pygame.sprite.Group()
all_sprites.add(PT1)
all_sprites.add(P1)