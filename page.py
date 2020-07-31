import pygame
from basic import *

class camera:
    def __init__(self, page):
        self.page = page
        self.offset = [0, 0]
        self.limit_x = [0, GAME_SCREEN_SIZE[0] - self.page.w]
        self.limit_y = [0, GAME_SCREEN_SIZE[1] - self.page.h]
        self.speed = [0,0]
        self.max_speed = 6
        self.acc = 1

    def coord_screen_to_game(self, pos):
        return [pos[0]+self.offset[0], pos[1]+self.offset[1]]

    def move(self, x, y):
        self.offset[0] += x
        self.offset[1] += y

        if self.offset[0] < self.limit_x[0]:
            self.offset[0] = self.limit_x[0]
        if self.offset[0] > self.limit_x[1]:
            self.offset[0] = self.limit_x[1]
        if self.offset[1] < self.limit_y[0]:
            self.offset[1] = self.limit_y[0]
        if self.offset[1] > self.limit_y[1]:
            self.offset[1] = self.limit_y[1]

    def set_limit(self, x1, x2, y1, y2):
        self.limit_x[0] = x1
        self.limit_x[1] = x2
        self.limit_y[0] = y1
        self.limit_y[1] = y2
    
    def get_offset(self):
        result = self.offset
        if self.offset[0] > 0:
            result[0] = int(self.offset[0])
        elif self.offset[0] < 0:
            result[0] = -int(-self.offset[0])
        if self.offset[1] > 0:
            result[1] = int(self.offset[1])
        elif self.offset[1] < 0:
            result[1] = -int(-self.offset[1])
        return result
        

    def update(self):
        padding = 100
        if self.page.mouse_coord[0] < padding:
            self.speed[0] -= self.acc
        elif self.page.mouse_coord[0] > GAME_SCREEN_SIZE[0] - padding:
            self.speed[0] += self.acc
        else:
            if self.speed[0] > 0:
                self.speed[0] -= 1
            elif self.speed[0] < 0:
                self.speed[0] += 1
        if self.page.mouse_coord[1] < padding:
            self.speed[1] -= self.acc
        elif self.page.mouse_coord[1] > GAME_SCREEN_SIZE[1] - padding:
            self.speed[1] += self.acc
        else:
            if self.speed[1] > 0:
                self.speed[1] -= 0.5
            elif self.speed[1] < 0:
                self.speed[1] += 0.5

        if self.speed[0] > self.max_speed:
            self.speed[0] = self.max_speed
        if self.speed[0] < -self.max_speed:
            self.speed[0] = -self.max_speed
        if self.speed[1] > self.max_speed:
            self.speed[1] = self.max_speed
        if self.speed[1] < -self.max_speed:
            self.speed[1] = -self.max_speed


        self.move(self.speed[0], self.speed[1])

        
        


class button:      # Primitive Class
    def __init__(self, page, image, image_hover, x, y, w, h):
        self.page = page
        self.image_normal = pygame.image.load(image)
        self.image_hover = pygame.image.load(image_hover)
        self.image = self.image_normal
        self.x = x
        self.y = y
        self.w = w
        self.h = h

    def operate(self):
        print("hi")

    def hover(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    def click(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.operate()

    def render(self):
        self.page.runner.screen.blit(self.image, (self.x-self.page.camera.get_offset()[0], self.y-self.page.camera.get_offset()[1]))


class page:     # Primitive Class
    def __init__(self, runner):
        self.w = 1000
        self.h = 600
        self.runner = runner
        self.camera = camera(self)
        self.buttons = []

    def refresh(self):
        pass

    def update(self):
        pass

    def render(self):
        pass





class page_title(page):
    def __init__(self,runner):
        page.__init__(self, runner)
        self.w = 1100
        self.h = 700
        self.camera.set_limit(-50, 50, -50, 50)
        self.image = pygame.image.load("images/title.png")
        self.mouse_coord = [0,0]
        

        self.buttons.append( button(self, "images/button.png", "images/button_hover.png", 200, 300, 300, 50) )

    def refresh(self):
        self.camera.offset = [0,0]

    def update(self):

        # Input Process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runner.gameIsEnd = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # Left Click
                    for b in self.buttons:
                        b.click(self.camera.coord_screen_to_game(event.pos))
            if event.type == pygame.MOUSEMOTION:
                # Update mouse_coord
                self.mouse_coord[0] = event.pos[0]
                self.mouse_coord[1] = event.pos[1]

                # Check buttons hover
                for b in self.buttons:
                    b.hover(self.camera.coord_screen_to_game(event.pos))
        
        # Camera Position
        self.camera.update()

        self.render()

    def render(self):
        self.runner.screen.fill(BLACK)
        self.runner.screen.blit(self.image, (0-self.camera.get_offset()[0],0-self.camera.get_offset()[1]))

        for b in self.buttons:
            b.render()

        pygame.display.flip()
        pass

            






def standard(runner):
    pool_standard = {}
    pool_standard['title'] = page_title(runner)
    return pool_standard