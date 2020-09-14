import pygame
pygame.init()

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
WIDTH = 1000
HEIGHT = 1000
ROWS = 15
COLS = ROWS
SQSY = HEIGHT/ROWS
SQSX = WIDTH/COLS

"""Loading Bomb image"""
BOMB = pygame.image.load("assets/bomb.png")
PADDING = 10
BOMB = pygame.transform.scale(BOMB, (int(SQSX-PADDING*2), int(SQSY-PADDING*2)))

"""Loading Flag image"""
FLAG = pygame.image.load("assets/flag.png")
FLAG = pygame.transform.scale(FLAG, (int(SQSX-PADDING*2), int(SQSY-PADDING*2)))

"""Making list of all number"""
NUMBERS = []
colours = [GRAY, BLUE, GREEN, RED, PURPLE, MAROON, TURQUOISE, BLACK, GRAYISH]
for N in range(9):
    myFont = pygame.font.Font('freesansbold.ttf', 999)
    NUMBERS.append(myFont.render(str(N), 1, colours[N]))
for position, number in enumerate(NUMBERS):
    NUMBERS[position] = pygame.transform.scale(number, (int(SQSX-PADDING*2), int(SQSY-PADDING*2)))


