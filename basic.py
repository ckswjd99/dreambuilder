# PYGAME
GAME_FPS            = 60
GAME_SCREEN_SIZE    = (1000, 600)
GAME_TITLE          = "Dream Builder?"

# COLORS
BLACK           = (  0,   0,   0)
WHITE           = (255, 255, 255)
BLUE            = (  0,   0, 255)
GREEN           = (  0, 255,   0)
RED             = (255,   0,   0)
YELLOW          = (255, 212,   0)
ORANGE          = (255, 127,   0)

SKY_BLUE        = (109, 151, 237)
CURTAIN_BLUE    = (216, 226, 250)



# NAME CONSTANTS

# PAGE STATE
PAGE_LOAD_DELAY         = 8

PAGE_LOAD               = 0
PAGE_RUNNING            = 1
PAGE_ESCAPE             = 2
PAGE_END                = 3

# PHASE
GAME_START              = -1
TURN_START              = 0
CHOOSE_ACTION           = 1
ACTION_COLLECT          = 2
ACTION_MINE             = 3
ACTION_MANUFACTURE      = 4
ACTION_RESEARCH         = 5
TURN_END                = 6

# RESOURCES
RESOURCE_JOY        = 1
RESOURCE_SADNESS    = 2
RESOURCE_ANGER      = 3
RESOURCE_FEAR       = 4


# FONTS
import font
middle_font = font.font("fonts/middle.png")
times_new_roman = font.font("fonts/times_new_roman.png")

