import pygame, os
from random import randint, choice
pygame.mixer.init()

# constants for screen size
WIDTH = 800
HEIGHT = 600

# constants for game stats
FRAMERATE = 60
ENEMY_DELAY = 2500

# constants for player stats
SPACE_PRESSABLE = True

# constants for sounds

SOUNDS = {
    "alien-death": pygame.mixer.Sound(os.path.join("assets/sounds", "alien-death.wav")),
    "hit": pygame.mixer.Sound(os.path.join("assets/sounds", "hit.wav")),
    "lose-life": pygame.mixer.Sound(os.path.join("assets/sounds", "lose-life.wav")),
    "shoot": pygame.mixer.Sound(os.path.join("assets/sounds", "shoot.wav"))
}

# constants for colors
RED = [0xe3, 0x1b, 0x23]
ORANGE = [0xf1, 0x9d, 0x28]
YELLOW = [0xf2, 0xe8, 0x29]
GREEN = [0x0b, 0xae, 0x44]
BLUE = [0x0a,0x4c,0xad]
PURPLE = [0x8a, 0x28, 0x9e]
PINK = [0xfc, 0x88, 0xd9]
BROWN = [0x6c, 0x51, 0x39]
GREY = [0xA2, 0xAA, 0xAD]
WHITE = [0xFF, 0xFF, 0xFF]
BLACK = [0x00, 0x00, 0x00]

COLORS = {
    "red": RED,
    "orange": ORANGE,
    "yellow": YELLOW,
    "green": GREEN,
    "blue": BLUE,
    "purple": PURPLE,
    "pink": PINK,
    "brown": BROWN,
    "grey": GREY,
    "white": WHITE,
    "black": BLACK
}

# keys from pygame
from pygame.locals import (
    RLEACCEL,
    K_UP,
    K_DOWN,
    K_LEFT,
    K_RIGHT,
    K_ESCAPE,
    KEYDOWN,
    QUIT,
    K_SPACE,
)