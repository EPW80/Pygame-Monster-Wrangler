import random
import pygame

# Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700


class Monster(pygame.sprite.Sprite):
    """A class to create enemy monster objects"""

    def __init__(self, x, y, image, monster_type):  # pylint: disable=C0103
        """Initialize the monster"""
        super().__init__()
        self.image = image
        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

        self.type = monster_type

        # Set random motion
        # pylint: disable=C0103
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
