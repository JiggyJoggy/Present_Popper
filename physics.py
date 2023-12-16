import pygame
from pygame.locals import *
from game_platform import Platform

vec = pygame.math.Vector2

class Object(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.vel = vec(0, 0)
        self.acc = vec(0, 0)
        self.pos = vec(0, 0)

    def move(self):
        FRIC = -0.12

        self.acc = vec(0, 0.5)

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

    def update(self):
        hits = pygame.sprite.spritecollide(Object, Platform, False)
        if Object.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1
