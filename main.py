import pygame

from basic import *
pygame.init()
screen = pygame.display.set_mode(GAME_SCREEN_SIZE)
pygame.display.set_caption(GAME_TITLE)
pygame.event.set_grab(True)

from runner import *
game_runner = runner(screen)
game_runner.run()



