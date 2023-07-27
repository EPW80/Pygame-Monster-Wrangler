"""Warp the player to the next level."""

import pygame
from settings import WINDOW_HEIGHT, WINDOW_WIDTH


class Player(pygame.sprite.Sprite):
    """A class representing a player in the game."""

    def __init__(self):
        """Initialize the player."""
        super().__init__()
        self.image = pygame.image.load("assets/knight.png")
        self.rect = self.image.get_rect()
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT

        self.lives = 5
        self.warps = 2
        self.velocity = 8

        self.sounds = {
            "catch": pygame.mixer.Sound("assets/catch.wav"),
            "die": pygame.mixer.Sound("assets/die.wav"),
            "warp": pygame.mixer.Sound("assets/warp.wav"),
        }

    def update(self):
        """Update the player."""
        keys = pygame.key.get_pressed()

        # Move the player
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocity
        if keys[pygame.K_RIGHT] and self.rect.right < WINDOW_WIDTH:
            self.rect.x += self.velocity
        if keys[pygame.K_UP] and self.rect.top > 100:
            self.rect.y -= self.velocity
        if keys[pygame.K_DOWN] and self.rect.bottom < WINDOW_HEIGHT - 100:
            self.rect.y += self.velocity

    def warp(self):
        """Warp the player back to safe position."""
        if self.warps > 0:
            self.warps -= 1
            self.warp_sound.play()
            self.rect.bottom = WINDOW_HEIGHT

    def reset(self):
        """Reset the player."""
        self.rect.centerx = WINDOW_WIDTH // 2
        self.rect.bottom = WINDOW_HEIGHT
