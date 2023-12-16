import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))


class Level(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.platforms = pygame.sprite.Group()

    def add_platform(self, platform):
        self.platforms.add(platform)
