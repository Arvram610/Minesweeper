import pygame
import random
from .Piece import piece
from .constants import WIDTH, ROWS, COLS, SQSY, SQSX, GRAY, BLACK, BOMB, BLUE, PADDING, NUMBERS, FLAG

""" Tells the piece to show itself """


def show_piece(pieces):
    pieces.show_piece()


""" Tells the piece to make itself flagged """


def flag_piece(pieces):
    pieces.flag_piece()


""" Tells the piece to make itself UnFlagged """


def unflag_piece(pieces):
    pieces.unflag_piece()


""" The board class """


class Board:
    """ The init """

    def __init__(self):
        self.board = []
        self.make_board()
        self.give_number()

    """ Makes the board array and puts in the pieces """

    def make_board(self):
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(piece(random.randint(0, 10)))

    """ Checking all boxes in a 3x3 radius """

    def give_number(self):
        for i in range(ROWS):
            for j in range(COLS):
                if not self.board[i][j].type:
                    self.board[i][j].number = None

                # Finds neighbours
                else:  # Finds neighbours
                    summer = 0
                    if not i == 0:
                        if not j == 0:
                            if self.board[i - 1][j - 1].type == 0:
                                summer += 1
                        if self.board[i - 1][j].type == 0:
                            summer += 1
                        if not j + 1 == COLS:
                            if self.board[i - 1][j + 1].type == 0:
                                summer += 1
                    if not j == 0:
                        if self.board[i][j - 1].type == 0:
                            summer += 1
                    if not j + 1 == COLS:
                        if self.board[i][j + 1].type == 0:
                            summer += 1
                    if not j == 0 and not i + 1 == ROWS:
                        if self.board[i + 1][j - 1].type == 0:
                            summer += 1
                    if not i + 1 == ROWS:
                        if self.board[i + 1][j].type == 0:
                            summer += 1
                    if not j + 1 == COLS and not i + 1 == ROWS:
                        if self.board[i + 1][j + 1].type == 0:
                            summer += 1
                    self.board[i][j].number = summer  # Finds neighbours

    """ Draws the Squares """

    def draw_squares(self, win):
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col].show:
                    pygame.draw.rect(win, GRAY, (SQSY * row, SQSX * col, SQSX, SQSY))
                else:
                    pygame.draw.rect(win, BLUE, (SQSY * row, SQSX * col, SQSX, SQSY))

    """ Returns the piece """

    def get_piece(self, x, y):
        return self.board[x][y]

    """ Draws the squares and lines separating them as well as putting the image on it """

    def draw_board(self, win):
        # Draws Lines
        self.draw_squares(win)
        for row in range(ROWS + 1):
            pygame.draw.line(win, BLACK, (row * SQSY, 0), (row * SQSY, WIDTH), 5)
        for col in range(COLS + 1):
            pygame.draw.line(win, BLACK, (0, col * SQSX), (WIDTH, col * SQSY), 5)

        # Image putting on
        for row in range(ROWS):
            for col in range(COLS):
                if self.board[row][col].show:
                    if not self.board[row][col].type and self.board[row][col].show:
                        win.blit(BOMB, (row * SQSX + PADDING, col * SQSY + PADDING))

                    if self.board[row][col].type and self.board[row][col].show:
                        win.blit(NUMBERS[self.board[row][col].number], (row * SQSX + PADDING, col * SQSY + PADDING))

                if self.board[row][col].flagged:
                    win.blit(FLAG, (row * SQSX + PADDING, col * SQSY + PADDING))