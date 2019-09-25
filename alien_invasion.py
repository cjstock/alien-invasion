import sys
import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from alien import Alien
from game_stats import GameStats
import game_functions as gf

def run_game():
    """Inititalize game"""
    pygame.init()
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    stats = GameStats(ai_settings=ai_settings)

    # Make an alien
    aliens = Group()

    # Make a ship
    ship = Ship(ai_settings=ai_settings, screen=screen)

    # Make a gropu to store bullets in
    bullets = Group()

    # Create a fleet of aliens
    gf.create_fleet(ai_settings=ai_settings, screen=screen, aliens=aliens, ship=ship)

    # Start main game loop
    while True:

        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets)
        ship.update()
        gf.update_bullets(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens, bullets=bullets)
        gf.update_aliens(stats=stats, ship=ship, ai_settings=ai_settings, aliens=aliens)

        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets, aliens=aliens)


run_game()