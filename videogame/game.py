"""
This module contains the game class for the "Monster Wrangler" game.
"""
import random
import pygame
from monster import Monster
from settings import (
    WINDOW_HEIGHT,
    WINDOW_WIDTH,
    FPS,
    WHITE,
    COLORS,
    MONSTER_IMAGES,
)

# pylint: disable=C0103
running = True


# pylint: disable=too-few-public-methods
class GameState:
    """A class representing the current state of the game."""

    def __init__(self):
        self.running = True
        self.score = 0
        self.round_number = 0
        self.round_time = 0
        self.frame_count = 0
        self.target_monster_type = None
        self.target_monster_image = None


# pylint: disable=too-few-public-methods
# Define Classes
class Game:
    """A class to control gameplay"""

    def __init__(self, player, monster_group, surface):
        """Initialize the game object."""
        self.state = GameState()
        self.display_surface = surface
        self.entities = {
            "player": player,
            "monster_group": monster_group,
        }
        self.sounds = {
            "next_level": pygame.mixer.Sound("./assets/next_level.wav"),
        }
        self.font = pygame.font.Font("freesansbold.ttf", 24)

        # initial target monster choice
        self.choose_new_target()

    def choose_new_target(self):
        """Choose a new target monster"""
        target_monster = random.choice(self.monster_group.sprites())
        self.target_monster_type = target_monster.type
        self.target_monster_image = target_monster.image

    def update(self):
        """Update our game object"""
        self.game_stats["frame_count"] += 1
        if self.game_stats["frame_count"] == FPS:
            self.game_stats["round_time"] += 1
            self.game_stats["frame_count"] = 0

        # Check for collisions
        self.check_collisions()

    def draw(self):
        """Set textures and draw the game"""
        catch_text = self.font.render("Current Catch", True, WHITE)
        catch_rect = catch_text.get_rect()
        catch_rect.centerx = WINDOW_WIDTH // 2
        catch_rect.top = 5

        score_text = self.font.render(
            "Score: " + str(self.game_stats["score"]), True, WHITE
        )
        score_rect = score_text.get_rect()
        score_rect.topleft = (5, 5)

        self.display_surface.blit(catch_text, catch_rect)
        self.display_surface.blit(score_text, score_rect)

        lives_text = self.font.render("Lives: " + str(self.player.lives), True, WHITE)
        lives_rect = lives_text.get_rect()
        lives_rect.topleft = (5, 35)

        round_text = self.font.render(
            "Current Round: " + str(self.game_stats["round_number"]), True, WHITE
        )
        round_rect = round_text.get_rect()
        round_rect.topleft = (5, 65)

        time_text = self.font.render("Round Time: " + str(self.round_time), True, WHITE)
        time_rect = time_text.get_rect()
        time_rect.topright = (WINDOW_WIDTH - 10, 5)

        warp_text = self.font.render("Warps: " + str(self.player.warps), True, WHITE)
        warp_rect = warp_text.get_rect()
        warp_rect.topright = (WINDOW_WIDTH - 10, 35)

        # Blit the HUD
        self.display_surface.blit(catch_text, catch_rect)
        self.display_surface.blit(score_text, score_rect)
        self.display_surface.blit(round_text, round_rect)
        self.display_surface.blit(lives_text, lives_rect)
        self.display_surface.blit(time_text, time_rect)
        self.display_surface.blit(warp_text, warp_rect)
        self.display_surface.blit(self.target_monster_image, self.target_monster_rect)

        pygame.draw.rect(
            self.display_surface,
            COLORS[self.target_monster_type],
            (WINDOW_WIDTH // 2 - 32, 30, 64, 64),
            2,
        )
        pygame.draw.rect(
            self.display_surface,
            COLORS[self.target_monster_type],
            (0, 100, WINDOW_WIDTH, WINDOW_HEIGHT - 200),
            4,
        )

    def check_collisions(self):
        """Check for collisions between the player and the monsters"""
        collided_monster = pygame.sprite.spritecollideany(
            self.entities["player"], self.entities["monster_group"]
        )
        if collided_monster:
            if collided_monster.type == self.state.target_monster_type:
                self.state.score += 100 * self.state.round_number
                collided_monster.remove(self.entities["monster_group"])
                self.handle_monster_collision()
            else:
                self.handle_wrong_monster_collision()

    def handle_monster_collision(self):
        """Handle a collision between the player and a monster"""
        if self.monster_group:
            self.player.catch_sound.play()
            self.choose_new_target()
        else:
            self.start_new_round()

    def handle_wrong_monster_collision(self):
        """Handle a collision between the player and a wrong monster"""
        self.player.die_sound.play()
        self.player.lives -= 1
        if self.player.lives <= 0:
            self.end_game()
        else:
            self.player.reset()

    def start_new_round(self):
        """Start a new round"""
        self.state.score += int(
            10000 * self.state.round_number / (1 + self.state.round_time)
        )
        self.state.round_time = 0
        self.state.frame_count = 0
        self.state.round_number += 1
        self.entities["player"].warps += 1

        self.entities["monster_group"].empty()
        for _ in range(self.state.round_number):
            for idx, image in enumerate(MONSTER_IMAGES):
                self.entities["monster_group"].add(
                    Monster(
                        random.randint(0, WINDOW_WIDTH - 64),
                        random.randint(100, WINDOW_HEIGHT - 164),
                        image,
                        idx,
                    )
                )

            self.choose_new_target()
            self.sounds["next_level"].play()

    def pause_game(self, main_text, sub_text):
        """Pause the game, display the main text, and display the sub text."""

        # Set color
        white = (255, 255, 255)
        black = (0, 0, 0)

        # Create the main pause text
        main_text = self.font.render(main_text, True, white)
        main_rect = main_text.get_rect()
        main_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2)

        self.display_surface.fill(black)
        self.display_surface.blit(main_text, main_rect)

        # Create the sub pause text
        sub_text = self.font.render(sub_text, True, white)
        sub_rect = sub_text.get_rect()
        sub_rect.center = (WINDOW_WIDTH // 2, WINDOW_HEIGHT // 2 + 64)

        # Display the pause text
        self.display_surface.fill(black)
        self.display_surface.blit(main_text, main_rect)
        self.display_surface.blit(sub_text, sub_rect)
        pygame.display.update()

        # Pause the game
        is_paused = True
        while is_paused:
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        is_paused = False
                if event.type == pygame.QUIT:
                    is_paused = False
                    pygame.quit()

    def end_game(self):
        """End the game, reset the game, and display the final score."""
        self.pause_game(
            "Final Score: " + str(self.state.score),
            "Press 'Enter' to play again",
        )
        self.reset_game()

    def reset_game(self):
        """Reset the game to its initial state."""
        self.state.score = 0
        self.state.round_number = 0
        self.entities["player"].lives = 5
        self.entities["player"].warps = 2
        self.entities["player"].reset()
        self.start_new_round()
