"""This is the monster class of the game."""
import random
import pygame

from settings import WINDOW_WIDTH, WINDOW_HEIGHT


# Disable pylint warning for too few public methods in this class
# pylint: disable=too-few-public-methods
class Monster(pygame.sprite.Sprite):
    """Initialize the monster"""

    def __init__(self, position_x, position_y, image, monster_type):
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (position_x, position_y)

        # Monster type is an int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        # Set random motion
        self.delta_x = random.choice([-1, 1])
        self.delta_y = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    def update(self):
        """Update the monster"""
        self.rect.x += self.delta_x * self.velocity
        self.rect.y += self.delta_y * self.velocity

        # Bounce the monster off the edges of the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.delta_x = -1 * self.delta_x
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.delta_y = -1 * self.delta_y
