import pygame

HEIGHT = 1000
WIDTH = 1000
ACC = 1
FRIC = -0.12
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)


class Platform(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.surf = pygame.Surface((WIDTH, 20))
        self.surf.fill(RED)
        self.rect = self.surf.get_rect(center=(WIDTH/2, HEIGHT - 10))
