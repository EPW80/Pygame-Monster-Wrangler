"""
This module contains the settings for the "Monster Wrangler" game.

It includes configurations for the game window, game colors, game FPS,
monster images, and fonts.
"""

import pygame

# Initialize pygame
pygame.init()

# Set display window
WINDOW_WIDTH = 1200
WINDOW_HEIGHT = 700
display_surface = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
pygame.display.set_caption("Monster Wrangler")

# Set FPS and Clock
FPS = 60
clock = pygame.time.Clock()

"""Draw the HUD and other to the display"""
# Set colors
WHITE = (255, 255, 255)
BLUE = (20, 176, 235)
GREEN = (87, 201, 47)
PURPLE = (226, 73, 243)
YELLOW = (243, 157, 20)

# Add the monster colors to a list where the index of the color matches target_monster_images
COLORS = [BLUE, GREEN, PURPLE, YELLOW]

try:
    MONSTER_IMAGES = [
        pygame.image.load("blue_monster.png"),
        pygame.image.load("green_monster.png"),
        pygame.image.load("purple_monster.png"),
        pygame.image.load("yellow_monster.png"),
    ]
except Exception as e:  # pylint: disable=broad-except
    print(f"Error loading images: {e}")
    MONSTER_IMAGES = []

# Load the font
FONT = pygame.font.Font("freesansbold.ttf", 24)
