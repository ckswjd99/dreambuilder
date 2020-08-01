import pygame
from basic import *

class camera:   # Primitive Class
    def __init__(self, page):
        self.page = page
        self.focus = [GAME_SCREEN_SIZE[0]/2, GAME_SCREEN_SIZE[1]/2]
        self.limit_x = [GAME_SCREEN_SIZE[0]/2, self.page.w - GAME_SCREEN_SIZE[0]/2]
        self.limit_y = [GAME_SCREEN_SIZE[1]/2, self.page.h - GAME_SCREEN_SIZE[1]/2]
        self.padding = self.page.padding
        self.offset = [0, 0]
        self.speed = [0,0]
        self.max_speed = 6
        self.acc = 1

    def coord_screen_to_game(self, pos):
        return [pos[0]+self.offset[0], pos[1]+self.offset[1]]

    def move_focus(self, x, y):
        self.focus[0] += x
        self.focus[1] += y

        if self.focus[0] < self.limit_x[0]:
            self.focus[0] = self.limit_x[0]
        if self.focus[0] > self.limit_x[1]:
            self.focus[0] = self.limit_x[1]
        if self.focus[1] < self.limit_y[0]:
            self.focus[1] = self.limit_y[0]
        if self.focus[1] > self.limit_y[1]:
            self.focus[1] = self.limit_y[1]

    def set_limit(self, x1, x2, y1, y2):
        self.limit_x[0] = x1
        self.limit_x[1] = x2
        self.limit_y[0] = y1
        self.limit_y[1] = y2
    
    def set_padding(self, padding):
        self.padding = padding

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
        if self.page.mouse_coord[0] < self.padding[0]:
            self.speed[0] -= self.acc
        elif self.page.mouse_coord[0] > GAME_SCREEN_SIZE[0] - self.padding[0]:
            self.speed[0] += self.acc
        else:
            if self.speed[0] > 0:
                self.speed[0] -= 1
            elif self.speed[0] < 0:
                self.speed[0] += 1
        if self.page.mouse_coord[1] < self.padding[1]:
            self.speed[1] -= self.acc
        elif self.page.mouse_coord[1] > GAME_SCREEN_SIZE[1] - self.padding[1]:
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

        
        self.move_focus(self.speed[0], self.speed[1])

        focus_smoothe = 10
        self.offset[0] -= (self.offset[0]-self.focus[0]+GAME_SCREEN_SIZE[0]/2)/focus_smoothe
        self.offset[1] -= (self.offset[1]-self.focus[1]+GAME_SCREEN_SIZE[1]/2)/focus_smoothe

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
        if self.x < self.page.camera.coord_screen_to_game(pos)[0] and self.page.camera.coord_screen_to_game(pos)[0] < self.x+self.w and self.y < self.page.camera.coord_screen_to_game(pos)[1] and self.page.camera.coord_screen_to_game(pos)[1] < self.y+self.h:
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    def click(self, pos):
        if self.x < self.page.camera.coord_screen_to_game(pos)[0] and self.page.camera.coord_screen_to_game(pos)[0] < self.x+self.w and self.y < self.page.camera.coord_screen_to_game(pos)[1] and self.page.camera.coord_screen_to_game(pos)[1] < self.y+self.h:
            self.operate()

    def render(self):
        self.page.runner.screen.blit(self.image, (self.x-self.page.camera.get_offset()[0], self.y-self.page.camera.get_offset()[1]))


class page:     # Primitive Class
    def __init__(self, runner):
        self.w = 1000
        self.h = 600
        self.runner = runner
        self.padding = [200, 200]
        self.camera = camera(self)
        self.buttons = []

        self.tick = 0
        self.state = PAGE_LOAD
        self.escape_time = None
        self.new_page = None

    def refresh(self):
        self.tick = 0
        self.state = PAGE_LOAD
        pass

    def update(self):
        self.tick += 1
        pass

    def render(self):
        pass





# USE CLASS

class camera_reversemouse(camera):
    def __init__(self, page):
        camera.__init__(self, page)

    def coord_screen_to_game(self, pos):
        return [pos[0]+self.offset[0], pos[1]+self.offset[1]]

    def move_focus(self, x, y):
        self.focus[0] += x
        self.focus[1] += y

        if self.focus[0] < self.limit_x[0]:
            self.focus[0] = self.limit_x[0]
        if self.focus[0] > self.limit_x[1]:
            self.focus[0] = self.limit_x[1]
        if self.focus[1] < self.limit_y[0]:
            self.focus[1] = self.limit_y[0]
        if self.focus[1] > self.limit_y[1]:
            self.focus[1] = self.limit_y[1]

    def set_limit(self, x1, x2, y1, y2):
        self.limit_x[0] = x1
        self.limit_x[1] = x2
        self.limit_y[0] = y1
        self.limit_y[1] = y2
    
    def set_padding(self, padding):
        self.padding = padding

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
        self.focus[0] = GAME_SCREEN_SIZE[0]/2 + (self.page.mouse_coord[0] - GAME_SCREEN_SIZE[0]/2) / GAME_SCREEN_SIZE[0] * (self.page.w - GAME_SCREEN_SIZE[0])/2
        self.focus[1] = GAME_SCREEN_SIZE[1]/2 + (self.page.mouse_coord[1] - GAME_SCREEN_SIZE[1]/2) / GAME_SCREEN_SIZE[1] * (self.page.h - GAME_SCREEN_SIZE[1])/2

        focus_smoothe = 10
        self.offset[0] -= (self.offset[0]-self.focus[0]+GAME_SCREEN_SIZE[0]/2)/focus_smoothe
        self.offset[1] -= (self.offset[1]-self.focus[1]+GAME_SCREEN_SIZE[1]/2)/focus_smoothe
        
class button_movepage_fix(button):
    def __init__(self, page, image, image_hover, x, y, w, h, nextpage):
        button.__init__(self, page, image, image_hover, x, y, w, h)
        self.nextpage = nextpage

    def operate(self):
        self.page.new_page = self.nextpage
        self.page.state = PAGE_ESCAPE
        self.page.escape_time = self.page.tick + PAGE_LOAD_DELAY

    def hover(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    def click(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.operate()
    def render(self):
        self.page.runner.screen.blit(self.image, (self.x, self.y))

class button_quit_fix(button):
    def __init__(self, page, image, image_hover, x, y, w, h):
        button.__init__(self, page, image, image_hover, x, y, w, h)

    def operate(self):
        self.page.runner.gameIsEnd = True

    def hover(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    def click(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.operate()
    def render(self):
        self.page.runner.screen.blit(self.image, (self.x, self.y))


class box(button):
    def __init__(self, page, image, image_hover, x, y, w, h, lines):
        button.__init__(self, page, image, image_hover, x, y, w, h)
        self.lines = lines
        self.now_line = 0
        self.loop = False
        self.offset = [30,20]

    def operate(self):
        if self.now_line < len(self.lines)-1:
            self.now_line += 1
        elif self.now_line == len(self.lines)-1 and self.loop == True:
            self.now_line = 0

    def update(self):
        pass

    def render(self):
        self.page.runner.screen.blit(self.image, (self.x, self.y))
        self.page.runner.screen.blit(middle_font.line(self.lines[self.now_line]), (self.x+self.offset[0], self.y+self.offset[1]))
        pass


class page_title(page):
    def __init__(self,runner):
        page.__init__(self, runner)
        self.w = 1100
        self.h = 700
        self.padding = [480, 280]
        self.camera = camera_reversemouse(self)
        self.image = pygame.image.load("images/title.png")
        self.mouse_coord = [0,0]
        

        self.buttons.append( button_movepage_fix(self, "images/button_start.png", "images/button_start_hover.png", 150, 340, 200, 30, 'choose_tutorial') )
        self.buttons.append( button_movepage_fix(self, "images/button_ending.png", "images/button_ending_hover.png", 225, 425, 200, 30, None) )
        self.buttons.append( button_quit_fix(self, "images/button_quit.png", "images/button_quit_hover.png", 350, 500, 200, 30) )

    def refresh(self):
        self.tick = 0
        self.state = PAGE_LOAD
        self.camera.offset = [0,0]

    def update(self):
        self.tick += 1

        # Input Process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runner.gameIsEnd = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # Left Click
                    for b in self.buttons:
                        b.click(event.pos)
            if event.type == pygame.MOUSEMOTION:
                # Update mouse_coord
                self.mouse_coord[0] = event.pos[0]
                self.mouse_coord[1] = event.pos[1]

                # Check buttons hover
                for b in self.buttons:
                    b.hover(event.pos)
        
        # Camera Position
        self.camera.update()

        self.render()

    def render(self):
        self.runner.screen.fill(BLACK)
        self.runner.screen.blit(self.image, (0-self.camera.get_offset()[0]-50 ,0-self.camera.get_offset()[1]-50))
        banner = pygame.image.load("images/banner.png")
        banner.set_colorkey((34,177,76))
        self.runner.screen.blit(banner, (450,100))

        for b in self.buttons:
            b.render()

        # CURTAIN
        if self.state == PAGE_LOAD:
            curtain = pygame.Surface(GAME_SCREEN_SIZE)
            curtain.fill(CURTAIN_BLUE)
            curtain.set_alpha(255*(PAGE_LOAD_DELAY-self.tick)/PAGE_LOAD_DELAY)
            self.runner.screen.blit(curtain, (0,0))
            if self.tick == PAGE_LOAD_DELAY:
                self.state = PAGE_RUNNING

        if self.state == PAGE_ESCAPE:
            curtain = pygame.Surface(GAME_SCREEN_SIZE)
            curtain.fill(CURTAIN_BLUE)
            curtain.set_alpha(255*(PAGE_LOAD_DELAY-self.escape_time+self.tick)/PAGE_LOAD_DELAY)
            self.runner.screen.blit(curtain, (0,0))
            if self.tick == self.escape_time:
                self.runner.change_page(self.new_page)

        pygame.display.flip()
        pass


class page_choose_tutorial(page):
    def __init__(self, runner):
        page.__init__(self, runner)
        self.w = 1100
        self.h = 700
        self.padding = [480, 280]

        self.buttons.append( box(self, "images/box.png", "images/box.png", 300, 100, 400, 250, ["Hello.", "Under Construction..."]) )
        self.buttons.append( button_quit_fix(self, "images/button_quit.png", "images/button_quit_hover.png", 400, 550, 200, 30) )

    def refresh(self):
        self.tick = 0
        self.state = PAGE_LOAD
        pass

    def update(self):
        self.tick += 1
        # Input Process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runner.gameIsEnd = True
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # Left Click
                    for b in self.buttons:
                        b.click(event.pos)
            if event.type == pygame.MOUSEMOTION:
                # Check buttons hover
                for b in self.buttons:
                    b.hover(event.pos)

        self.render()

    def render(self):
        self.runner.screen.fill(SKY_BLUE)
        for b in self.buttons:
            b.render()
        # CURTAIN
        if self.state == PAGE_LOAD:
            curtain = pygame.Surface(GAME_SCREEN_SIZE)
            curtain.fill(CURTAIN_BLUE)
            curtain.set_alpha(255*(PAGE_LOAD_DELAY-self.tick)/PAGE_LOAD_DELAY)
            self.runner.screen.blit(curtain, (0,0))
            if self.tick == PAGE_LOAD_DELAY+5:
                self.state = PAGE_RUNNING

        if self.state == PAGE_ESCAPE:
            curtain = pygame.Surface(GAME_SCREEN_SIZE)
            curtain.fill(CURTAIN_BLUE)
            curtain.set_alpha(255*(PAGE_LOAD_DELAY-self.escape_time+self.tick)/PAGE_LOAD_DELAY)
            self.runner.screen.blit(curtain, (0,0))
            if self.tick == self.escape_time:
                self.runner.change_page(self.new_page)

        pygame.display.flip()

        pygame.display.flip()









def standard(runner):
    pool_standard = {}
    pool_standard['title'] = page_title(runner)
    pool_standard['choose_tutorial'] = page_choose_tutorial(runner)
    return pool_standard