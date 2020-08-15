import pygame
from pygame.sprite import Group
import game_functions as gf
from settings import Settings
from ship import Ship
from game_stats import Game_stats
from button import Button
from scoreboard import Scoreboard


# def check_events():
#     #check for keypress and mouse events


def run_game():

    # intialize the game and create the screen object
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption('Alien invasion')

    # make a ship, groupe to store all bullets and a group to store all aliens
    ship = Ship(ai_settings, screen)
    bullets = Group()
    aliens = Group()

    stats = Game_stats(ai_settings)
    play_button = Button(ai_settings, screen, 'Play')
    sb = Scoreboard(ai_settings, screen, stats)
    gf.create_fleet(ai_settings, screen, ship, aliens, sb)

    # start the main loop for the game
    while True:
        gf.check_events(ai_settings, screen, stats, sb,
                        play_button, ship, aliens, bullets)
        if stats.game_active:
            ship.update()
            bullets.update()
            gf.update_bullets(ai_settings, screen, stats,
                              sb, ship, aliens, bullets)
            gf.check_bullet_alien_collision(
                ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, stats, sb,
                             screen, ship, aliens, bullets)
        gf.update_sreen(ai_settings, screen, stats, sb, ship,
                        aliens, bullets, play_button)


run_game()
