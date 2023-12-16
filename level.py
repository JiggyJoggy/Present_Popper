import pygame

HEIGHT = 1000
WIDTH = 1000


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
    def __init__(
            self, width, height, color,
              x, y, end_x, end_y, background_image_path):
        super().__init__()
        self.image = pygame.Surface((width, height))
        self.image.fill(color)
        self.rect = self.image.get_rect(topleft=(x, y))
        self.background = pygame.image.load(
                background_image_path).convert()
        aspect_ratio = self.background.get_width() / self.background.get_height()

        new_width = WIDTH
        new_height = int(WIDTH / aspect_ratio)

        self.background = pygame.transform.scale(
                self.background, (new_width, new_height))

        self.platforms = pygame.sprite.Group()
        self.endpoints = pygame.sprite.Group()

        self.end_point = EndPoint(50, 50, (0, 255, 0), end_x, end_y)
        self.endpoints.add(self.end_point)

    def add_platform(self, platform):
        self.platforms.add(platform)

    def all_sprites(self):
        return pygame.sprite.Group(self.platforms, self.endpoints)

    def draw_background(self, surface):
        surface.blit(self.background, self.rect)
