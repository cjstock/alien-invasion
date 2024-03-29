import pygame
from pygame.sprite import Group

from settings import Settings
from ship import Ship
from game_stats import GameStats
import game_functions as gf
from button import Button
from scoreboard import Scoreboard


def run_game():
    """Initialize game"""
    pygame.init()
    pygame.mixer.music.load("sounds/phys_ed.mp3")
    ai_settings = Settings()

    screen = pygame.display.set_mode((ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")

    # Make the Play button
    play_button = Button(screen=screen, msg="Play")

    stats = GameStats(ai_settings=ai_settings)
    sb = Scoreboard(ai_settings=ai_settings, screen=screen, stats=stats)

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

        gf.check_events(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets, play_button=play_button,
                        stats=stats, aliens=aliens, sb=sb)

        if stats.game_active:
            ship.update()
            gf.update_bullets(ai_settings=ai_settings, screen=screen, ship=ship, aliens=aliens, bullets=bullets, sb=sb,
                              stats=stats)
            gf.update_aliens(stats=stats, ship=ship, ai_settings=ai_settings, aliens=aliens, screen=screen,
                             bullets=bullets, sb=sb)

        gf.update_screen(ai_settings=ai_settings, screen=screen, ship=ship, bullets=bullets, aliens=aliens,
                         play_button=play_button, stats=stats, sb=sb)


run_game()
