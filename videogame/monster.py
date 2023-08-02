"""This is th monster class of the game."""
import random
import pygame

from game import WINDOW_WIDTH, WINDOW_HEIGHT


class Monster(pygame.sprite.Sprite):
    def __init__(self, x, y, image, monster_type):
        """Initialize the monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        # Monster type is an int 0 -> blue, 1 -> green, 2 -> purple, 3 -> yellow
        self.type = monster_type

        # Set random motion
        self.dx = random.choice([-1, 1])
        self.dy = random.choice([-1, 1])
        self.velocity = random.randint(1, 5)

    def update(self):
        """Update the monster"""
        self.rect.x += self.dx * self.velocity
        self.rect.y += self.dy * self.velocity

        # Bounce the monster off the edges of the display
        if self.rect.left <= 0 or self.rect.right >= WINDOW_WIDTH:
            self.dx = -1 * self.dx
        if self.rect.top <= 100 or self.rect.bottom >= WINDOW_HEIGHT - 100:
            self.dy = -1 * self.dy
