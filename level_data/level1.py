# level_data/level1.py

from level import Level, Platform


def create_level(WIDTH, HEIGHT, COLOR):
    level = Level(WIDTH + 500, 20, COLOR, 0, 800, 500, 100, '/Users/puzzle/Desktop/Holberton_School_Projects/Present_Popper/sprites/background/mountains.jpeg')
    level.add_platform(Platform(WIDTH, 20, COLOR, WIDTH/2, HEIGHT - 20, 'rectangle'))  # Rectangle platform
    level.add_platform(Platform(12, 12, COLOR, 200, HEIGHT - 50, 'square'))  # Square platform
    return level
