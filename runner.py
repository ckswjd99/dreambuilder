import pygame

import system
import page


# RUNNER CLASS
class runner:
    def __init__(self, screen):
        self.screen = screen

    def run(self):

        self.system = system.standard(self)
        self.pages = page.standard(self)

        self.gameIsEnd = False
        self.page_now = self.pages['title']

        while(not self.gameIsEnd):
            self.page_now.update()
        
        pygame.display.quit()

