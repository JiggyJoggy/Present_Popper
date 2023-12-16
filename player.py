import pygame
from pygame.locals import K_a, K_d

HEIGHT = 1000
WIDTH = 1000
ACC = 1
FRIC = -0.12
FPS = 60
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set the new width and height for the resized Santa image
new_width = 70
new_height = 100
vec = pygame.math.Vector2


class Player(pygame.sprite.Sprite):
    def __init__(self, platforms):
        super().__init__()

        self.platforms = platforms

        # Load player images for animation
        self.player_images_left = [
            pygame.image.load('sprites/santa/santa_left1.png').convert_alpha(),
            pygame.image.load('sprites/santa/santa_left2.png').convert_alpha(),
            pygame.image.load('sprites/santa/santa_left3.png').convert_alpha(),
            # Add more frames as needed
        ]

        self.player_images_right = [
            pygame.image.load(
                'sprites/santa/santa_right1.png').convert_alpha(),
            pygame.image.load(
                'sprites/santa/santa_right2.png').convert_alpha(),
            pygame.image.load(
                'sprites/santa/santa_right3.png').convert_alpha(),
            # Add more frames as needed
        ]
        self.player_image_front = pygame.image.load(
            'sprites/santa/santa_front2.png').convert()

        # Resize Santa images
        self.player_images_left = [
            pygame.transform.scale(
                image, (new_width,
                        new_height)) for image in self.player_images_left]
        self.player_images_right = [
            pygame.transform.scale(image, (
                new_width, new_height)) for image in self.player_images_right]
        self.player_image_front = [
            pygame.transform.scale(
                self.player_image_front, (new_width, new_height))]

        self.current_frame = 0
        self.image = self.player_images_left[self.current_frame]
        self.rect = self.image.get_rect()

        self.pos = pygame.math.Vector2((25, 500))  # Adjust the height
        self.vel = pygame.math.Vector2(0, 0)
        self.acc = pygame.math.Vector2(0, 0)
        self.facing_right = True  # Initialize facing direction

        self.animation_speed = 150  # Adjust animation speed
        self.animation_timer = pygame.time.get_ticks()
        self.clock = pygame.time.Clock()

    def move(self):
        self.acc = pygame.math.Vector2(0, 0.5)

        pressed_keys = pygame.key.get_pressed()

        if pressed_keys[K_a]:
            self.acc.x = -ACC
            self.facing_right = False
        if pressed_keys[K_d]:
            self.acc.x = ACC
            self.facing_right = True

        self.acc.x += self.vel.x * FRIC
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc

        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH

        self.rect.midbottom = self.pos

    def update(self):
        # Control sprite animation speed
        current_time = pygame.time.get_ticks()
        dt = current_time - self.animation_timer

        if dt >= self.animation_speed:
            self.animation_timer = current_time

            # Define the animation pattern for left and right
            animation_pattern = [0, 1, 2, 1]

            # Update animation frames based on facing direction and pattern
            if (self.vel.x != 0 or self.vel.y != 0) and (
                 pygame.key.get_pressed()[K_a] or
                 pygame.key.get_pressed()[K_d]):
                if self.facing_right:
                    self.current_frame = (self.current_frame + 1) % len(
                        animation_pattern)
                    self.image = self.player_images_right[animation_pattern[
                        self.current_frame]]
                else:
                    self.current_frame = (self.current_frame + 1) % len(
                        animation_pattern)
                    self.image = self.player_images_left[
                        animation_pattern[self.current_frame]]
            else:
                # Player is not holding A or D, set the default frame
                self.current_frame = 1
                if self.facing_right:
                    self.image = self.player_images_right[self.current_frame]
                else:
                    self.image = self.player_images_left[self.current_frame]

        # Collision handling
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        if self.vel.y > 0:
            if hits:
                self.vel.y = 0
                self.pos.y = hits[0].rect.top + 1

    def jump(self):
        hits = pygame.sprite.spritecollide(self, self.platforms, False)
        if hits:
            self.vel.y = -15
