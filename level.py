import pygame


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))


class EndPoint(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, 400))


class Level(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y, end_x, end_y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.platforms = pygame.sprite.Group()
        self.endpoints = pygame.sprite.Group()

        self.end_point = EndPoint(50, 50, (0, 250, 0), end_x, end_y)
        self.endpoints.add(self.end_point)

    def add_platform(self, platform):
        self.platforms.add(platform)

    def all_sprites(self):
        return pygame.sprite.Group(self.platforms, self.endpoints)
