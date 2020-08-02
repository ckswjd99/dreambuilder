import pygame
from basic import *

#========================= PRIMITIVE CLASS =========================#

# Primitive Class: <CAMREA>
class camera:
    def __init__(self, page):
        self.page = page
        self.focus = [GAME_SCREEN_SIZE[0]/2, GAME_SCREEN_SIZE[1]/2]
        self.limit_x = [GAME_SCREEN_SIZE[0]/2, self.page.w - GAME_SCREEN_SIZE[0]/2]
        self.limit_y = [GAME_SCREEN_SIZE[1]/2, self.page.h - GAME_SCREEN_SIZE[1]/2]
        self.padding = self.page.padding
        self.offset = [0, 0]
        self.speed = [0,0]
        self.max_speed = 12
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


# Primitive Class: <BUTTON>
class button:
    def __init__(self, page, image, image_hover, x, y, w, h):
        self.page = page
        self.image_normal = pygame.image.load(image)
        self.image = self.image_normal
        self.image_hover = pygame.image.load(image_hover)
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


# Primitive Class: <PAGE>
class page:
    def __init__(self, runner):
        self.w = 1000
        self.h = 600
        self.runner = runner
        self.padding = [200, 200]
        self.camera = camera(self)
        self.buttons = []
        self.mouse_coord = [0,0]

        self.tick = 0
        self.state = PAGE_LOAD
        self.escape_time = None
        self.new_page = None
        self.timer = {}

    def refresh(self):
        self.tick = 0
        self.state = PAGE_LOAD
        pass

    def update(self):
        self.tick += 1
        pass

    def render(self):
        pass





#========================= FOR USE CLASS =========================#

# For Use Class: <CAMERA_REVERSEMOUSE>
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

# For Use Class: <BUTTON_NEXTTURN>
class button_nextturn(button):
    def __init__(self, page, image, image_hover, x, y, w, h, nextpage):
        button.__init__(self, page, image, image_hover, x, y, w, h)
        self.nextpage = nextpage

    def operate(self):
        self.page.new_page = self.nextpage
        self.page.state = PAGE_ESCAPE
        self.page.runner.system.turn += 1
        self.page.runner.system.phase = TURN_END
        self.page.escape_time = self.page.tick + PAGE_LOAD_DELAY

    def hover(self, pos):
        realpos = self.page.camera.coord_screen_to_game(pos)
        if self.x < realpos[0] and realpos[0] < self.x+self.w and self.y < realpos[1] and realpos[1] < self.y+self.h:
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    def click(self, pos):
        realpos = self.page.camera.coord_screen_to_game(pos)
        if self.x < realpos[0] and realpos[0] < self.x+self.w and self.y < realpos[1] and realpos[1] < self.y+self.h:
            self.operate()
    def render(self):
        self.page.runner.screen.blit(self.image, (self.x-self.page.camera.offset[0], self.y-self.page.camera.offset[1]))

# For Use Class: <BUTTON_MOVEPAGE_FIX>
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


# For Use Class: <BUTTON_QUIT_FIX>
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


# For Use Class: <BOX>
class box(button):
    def __init__(self, page, image, image_hover, x, y, w, h, lines):
        button.__init__(self, page, image, image_hover, x, y, w, h)
        self.next_icon = pygame.image.load("images/box_next.png")
        self.next_icon.set_colorkey((255,0,0))
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
        self.page.runner.screen.blit(middle_font.line(self.lines[self.now_line], RED), (self.x+self.offset[0], self.y+self.offset[1]))
        if self.now_line != len(self.lines)-1:
            offset = [50,35]
            self.next_icon.set_colorkey((255,0,0))
            self.page.runner.screen.blit(self.next_icon, (self.x+self.w-offset[0], self.y+self.h-offset[1]))
        pass


# For Use Class: <BUTTON_QUIT_FIX>
class button_resource(button):
    def __init__(self, page, image, image_hover, x, y, w, h, kind):
        button.__init__(self, page, image, image_hover, x, y, w, h)
        self.kind = kind
        if self.kind == RESOURCE_JOY:
            self.image_normal = pygame.image.load("images/resource_joy.png")
            self.image_hover = pygame.image.load("images/resource_joy_hover.png")
        elif self.kind == RESOURCE_SADNESS:
            self.image_normal = pygame.image.load("images/resource_sadness.png")
            self.image_hover = pygame.image.load("images/resource_sadness_hover.png")
        elif self.kind == RESOURCE_ANGER:
            self.image_normal = pygame.image.load("images/resource_anger.png")
            self.image_hover = pygame.image.load("images/resource_anger_hover.png")
        elif self.kind == RESOURCE_FEAR:
            self.image_normal = pygame.image.load("images/resource_fear.png")
            self.image_hover = pygame.image.load("images/resource_fear_hover.png")
        self.image_normal.set_colorkey((60,60,60))
        self.image_hover.set_colorkey((60,60,60))
    
    def hover(self, pos):
        if self.x < pos[0] and pos[0] < self.x+self.w and self.y < pos[1] and pos[1] < self.y+self.h:
            self.image = self.image_hover
        else:
            self.image = self.image_normal

    def click(self, pos):
        realpos = self.page.camera.coord_screen_to_game(pos)
        if self.x < realpos[0] and realpos[0] < self.x+self.w and self.y < realpos[1] and realpos[1] < self.y+self.h:
            self.operate()
    
    def operate(self):
        print("HI")
        if self.page.runner.system.player.add_resource(self.kind):
            index = self.page.resources.index(self)
            self.page.runner.system.dispenser.pop(index)
            self.page.runner.system.dispenser.fill()
            self.page.resources.pop(index)

    def update(self):
        pass

    def render(self):
        self.page.runner.screen.blit(self.image, (self.x-self.page.camera.offset[0], self.y-self.page.camera.offset[1]))
        
        
        


# For Use Class: <PAGE_TITLE>
class page_title(page):
    def __init__(self,runner):
        page.__init__(self, runner)
        self.w = 1100
        self.h = 700
        self.padding = [480, 280]
        self.camera = camera_reversemouse(self)
        self.image = pygame.image.load("images/title.png")

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


# For Use Class: <PAGE_CHOOSE_TUTORIAL>
class page_choose_tutorial(page):
    def __init__(self, runner):
        page.__init__(self, runner)
        self.w = 1100
        self.h = 700
        self.padding = [480, 280]

        self.buttons.append( box(self, "images/box.png", "images/box.png", 300, 100, 400, 250, ["Hello.", "Under Construction..."]) )
        self.buttons.append( button_movepage_fix(self, "images/button_start.png", "images/button_start_hover.png", 400, 500, 200, 30, 'gameboard') )
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


# For Use Class: <PAGE_GAMEBOARD>
class page_gameboard(page):
    def __init__(self, runner):
        page.__init__(self, runner)
        self.image = pygame.image.load("images/gameboard_bg.png")

        self.w = 2800
        self.h = 800
        self.padding = [350,200]
        self.camera.set_padding(self.padding)
        self.mouse_coord = [0,0]
        self.camera.set_limit(-9999,9999, -9999,9999)

        self.buttons.append( button_nextturn(self, "images/button_start.png", "images/button_start_hover.png", 400, 500, 200, 30, 'gameboard') )

        self.resources = []

        self.overlay = False
        self.overlay_buttons = []
        self.overlay_buttons.append( button_quit_fix(self, "images/button_quit.png", "images/button_quit_hover.png", 400, 300, 200, 30) )

        self.turn_display = pygame.image.load("images/turn_display.png")

    def refresh(self):
        self.tick = 0
        self.state = PAGE_LOAD
        self.turn_display = pygame.image.load("images/turn_display.png")
        self.runner.system.phase = TURN_START
        self.timer['turn_display_tick'] = 60
        self.camera.set_limit(-9999,9999, -9999,9999)
        self.camera.focus = [0, 9999]

        # Fill Dispenser
        self.runner.system.dispenser.fill()
        for i in range(len(self.runner.system.dispenser.queue)):
            if self.runner.system.dispenser.queue[i] == RESOURCE_JOY:
                self.resources.append( button_resource(self, "images/null.png", "images/null.png", i*50, 600, 50, 50, RESOURCE_JOY) )
            elif self.runner.system.dispenser.queue[i] == RESOURCE_SADNESS:
                self.resources.append( button_resource(self, "images/null.png", "images/null.png", i*50, 600, 50, 50, RESOURCE_SADNESS) )
            elif self.runner.system.dispenser.queue[i] == RESOURCE_ANGER:
                self.resources.append( button_resource(self, "images/null.png", "images/null.png", i*50, 600, 50, 50, RESOURCE_ANGER) )
            elif self.runner.system.dispenser.queue[i] == RESOURCE_FEAR:
                self.resources.append( button_resource(self, "images/null.png", "images/null.png", i*50, 600, 50, 50, RESOURCE_FEAR) )
    
    def update(self):
        self.tick += 1
        # Input Process
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.runner.gameIsEnd = True
            if event.type == pygame.KEYDOWN:
                if event.key == 27:    # Key ESC
                    self.overlay = not self.overlay
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:   # Left Click
                    for b in self.buttons:
                        b.click(event.pos)
                    for r in self.resources:
                        r.click(event.pos)
            if event.type == pygame.MOUSEMOTION:
                # Update mouse_coord
                self.mouse_coord[0] = event.pos[0]
                self.mouse_coord[1] = event.pos[1]

                # Check buttons hover
                for b in self.buttons:
                    b.hover(event.pos)
                
                for r in self.resources:
                    r.hover(event.pos)
        
        # Overlay Case
        if self.overlay:
            overlay_bg = pygame.Surface(GAME_SCREEN_SIZE)
            overlay_bg.fill(WHITE)
            overlay_bg.set_alpha(127)
            self.runner.screen.blit(overlay_bg,(0,0))

            overlay_done = False
            while not overlay_done:
                self.runner.clock.tick(GAME_FPS)
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN and event.key == 27:
                        self.overlay = False
                        overlay_done = True
                    if event.type == pygame.MOUSEBUTTONDOWN:
                        if event.button == 1:   # Left Click
                           for b in self.overlay_buttons:
                               b.click(event.pos)
                    if event.type == pygame.MOUSEMOTION:
                        # Check buttons hover
                        for b in self.overlay_buttons:
                            b.hover(event.pos)
                if self.runner.gameIsEnd:
                    break



                for b in self.overlay_buttons:
                    b.render()
                pygame.display.flip()
                
        
        
        
        self.camera.update()

        self.render()
    
    def render(self):
        # STATE: PAGE_LOAD
        if self.state == PAGE_LOAD:
            self.camera.focus = [0, -GAME_SCREEN_SIZE[1]*100]
        else:
            self.camera.set_limit(GAME_SCREEN_SIZE[0]/2, self.w-GAME_SCREEN_SIZE[0]/2, GAME_SCREEN_SIZE[1]/2, self.h-GAME_SCREEN_SIZE[1]/2)
        
        # STATE: ALL
        self.runner.screen.fill(SKY_BLUE)
        self.runner.screen.blit(self.image, (0-self.camera.get_offset()[0] ,0-self.camera.get_offset()[1]))

        for b in self.buttons:
            b.render()
        
        for r in self.resources:
            r.render()

        # STATE: PAGE_LOAD
        if self.state == PAGE_LOAD:
            curtain = pygame.Surface(GAME_SCREEN_SIZE)
            curtain.fill(CURTAIN_BLUE)
            curtain.set_alpha(255*(PAGE_LOAD_DELAY-self.tick)/PAGE_LOAD_DELAY)
            self.runner.screen.blit(curtain, (0,0))
            if self.tick == PAGE_LOAD_DELAY:
                self.state = PAGE_RUNNING
                self.runner.system.state = TURN_START
                self.turn_display_tick = 60

        # STATE: PAGE_LOAD
        if self.state == PAGE_ESCAPE:
            curtain = pygame.Surface(GAME_SCREEN_SIZE)
            curtain.fill(CURTAIN_BLUE)
            curtain.set_alpha(255*(PAGE_LOAD_DELAY-self.escape_time+self.tick)/PAGE_LOAD_DELAY)
            self.runner.screen.blit(curtain, (0,0))
            if self.tick == self.escape_time:
                self.runner.change_page(self.new_page)

        # PHASE: TURN_START
        if self.runner.system.phase == TURN_START:
            self.timer['turn_display_tick'] -= 1
            offset = [220,10]
            self.turn_display.blit(times_new_roman.line(str(self.runner.system.turn), (221,148,49)), (offset[0],offset[1]))
            self.runner.screen.blit(self.turn_display, (GAME_SCREEN_SIZE[0]/2-self.turn_display.get_width()/2, GAME_SCREEN_SIZE[1]/2-self.turn_display.get_height()/2))

            if self.timer['turn_display_tick'] == 0:
                self.runner.system.phase = CHOOSE_ACTION


        pygame.display.flip()
        pass






def standard(runner):
    pool_standard = {}
    pool_standard['title'] = page_title(runner)
    pool_standard['choose_tutorial'] = page_choose_tutorial(runner)
    pool_standard['gameboard'] = page_gameboard(runner)
    return pool_standard