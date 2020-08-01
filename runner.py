import pygame

from basic import *
import system
import page


# RUNNER CLASS
class runner:
    def __init__(self, screen):
        self.screen = screen

        self.system = system.standard(self)
        self.pages = page.standard(self)
        self.clock = pygame.time.Clock()

    def run(self):

        self.gameIsEnd = False
        self.page_now = self.pages['title']

        while(not self.gameIsEnd):
            self.clock.tick(GAME_FPS)
            self.page_now.update()
        
        pygame.display.quit()

    def change_page(self, map_name):
        self.new_page = self.pages[map_name]
        self.new_page.refresh()
        self.page_now = self.new_page
        self.clock.tick(GAME_FPS/3)

