# level.py

import pygame

HEIGHT = 600
WIDTH = 1000


class Platform(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y, platform_type='rectangle'):
        super().__init__()
        self.platform_type = platform_type

        if self.platform_type == 'rectangle':
            self.image = pygame.Surface((width, height))
        elif self.platform_type == 'square':
            self.image = pygame.Surface((width, height))
        else:
            raise ValueError(f"Invalid platform type: {platform_type}")

        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))


class EndPoint(pygame.sprite.Sprite):
    def __init__(self, width, height, color, x, y):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(center=(x, y))


class Level(pygame.sprite.Sprite):
    def __init__(
            self, width, height, color,
            x, y, end_x, end_y, background_image):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.background = pygame.image.load(
                background_image).convert()
        self.background_rect = self.background.get_rect()
        self.background_speed = 0.2

        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))

        self.platforms = pygame.sprite.Group()
        self.endpoints = pygame.sprite.Group()

        self.end_point = EndPoint(50, 50, (0, 255, 0), 1200, 600)
        self.endpoints.add(self.end_point)

    def update_background(self):
        # Update the background position based on the scaling factor
        self.background_rect.x += self.background_speed
        if self.background_rect.right < WIDTH:
            self.background_rect.x = 0

    def add_platform(self, platform):
        self.platforms.add(platform)

    def all_sprites(self):
        return pygame.sprite.Group(self.platforms, self.endpoints)

    def draw_background(self, surface):
        surface.blit(
            self.background, (
             -self.background_rect.x - WIDTH / 2,
             -self.background_rect.y - HEIGHT / 2))
