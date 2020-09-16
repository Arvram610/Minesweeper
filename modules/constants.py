import pygame

pygame.init()

"""Simple Setup"""
difficulty = 20  # 1 to rows * rows
ROWS = 10  # How many rows that will display on board
screensize = 1000  # in pixels

"""Defining colours"""

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (122, 122, 122)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
PURPLE = (128, 0, 128)
MAROON = (128, 0, 0)
TURQUOISE = (64, 224, 208)
GRAYISH = (200, 200, 200)

"""Setting screen sizes"""

WIDTH = screensize
HEIGHT = WIDTH
COLS = ROWS
SQSY = HEIGHT / ROWS
SQSX = WIDTH / COLS

"""Some Settings"""
BOMBS = difficulty

"""Loading Bomb image"""
BOMB = pygame.image.load("assets/bomb.png")
PADDING = 1
BOMB = pygame.transform.scale(BOMB, (int(SQSX - PADDING), int(SQSY - PADDING)))

"""Loading Flag image"""
FLAG = pygame.image.load("assets/flag.png")
FLAG = pygame.transform.scale(FLAG, (int(SQSX - PADDING), int(SQSY - PADDING)))

"""Making list of all number"""
NUMBERS = []
colours = [GRAY, BLUE, GREEN, RED, PURPLE, MAROON, TURQUOISE, BLACK, GRAYISH]
for N in range(9):
    myFont = pygame.font.Font('freesansbold.ttf', 999)
    NUMBERS.append(myFont.render(str(N), 1, colours[N]))
for position, number in enumerate(NUMBERS):
    NUMBERS[position] = pygame.transform.scale(number, (int(SQSX - PADDING), int(SQSY - PADDING)))
