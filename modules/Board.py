import pygame
import random
from .Piece import Piece
from .constants import WIDTH, ROWS, COLS, SQSY, SQSX, GRAY, BLACK, BOMB, BLUE, PADDING, NUMBERS, FLAG, BOMBS

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
        self.turned_pieces = []
        self.make_board()

    """ Puts set amount of mines on board """

    def generate_mines(self):
        for bomb in range(BOMBS):
            run = True
            while run:
                piece = self.get_piece(random.randint(0, COLS-1), random.randint(0, ROWS-1))
                if piece.type == 1:
                    piece.type = 0
                    run = False

    """ Makes the board array and puts in the pieces """

    def make_board(self):
        self.board = []
        for row in range(ROWS):
            self.board.append([])
            for col in range(COLS):
                self.board[row].append(Piece())

        self.generate_mines()
        self.give_number()

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

    """Marks itself as turned"""

    def add_to_turned(self, piece):
        self.turned_pieces.append(piece)

    """Makes it so if its a blank piece it opens up close by pieces6"""

    def turn_near(self, piece, x, y):
        if piece.type and not piece.number:
            show_piece(piece)
            self.add_to_turned(piece)
            if x >= 1:
                if not self.board[x - 1][y] in self.turned_pieces:  # Checks to the left
                    if self.board[x - 1][y].type:
                        if not self.board[x - 1][y].number:
                            self.turn_near(self.board[x - 1][y], x - 1, y)

                        if self.board[x - 1][y].number > 0.5:
                            self.add_to_turned(self.board[x - 1][y])
                            show_piece(self.board[x - 1][y])

            if x + 1 < ROWS:
                if not self.board[x + 1][y] in self.turned_pieces:  # Checks to the right
                    if self.board[x + 1][y].type:
                        if not self.board[x + 1][y].number:
                            self.turn_near(self.board[x + 1][y], x + 1, y)

                        if self.board[x + 1][y].number > 0.5:
                            self.add_to_turned(self.board[x + 1][y])
                            show_piece(self.board[x + 1][y])

            if y >= 1:
                if not self.board[x][y - 1] in self.turned_pieces:  # Checks up
                    if self.board[x][y - 1].type:
                        if not self.board[x][y - 1].number:
                            self.turn_near(self.board[x][y - 1], x, y - 1)

                        if self.board[x][y - 1].number > 0.5:
                            self.add_to_turned(self.board[x][y - 1])
                            show_piece(self.board[x][y - 1])

            if y - 1 <= COLS:
                if not self.board[x][y + 1] in self.turned_pieces:  # Checks down
                    if self.board[x][y + 1].type:
                        if not self.board[x][y + 1].number:
                            self.turn_near(self.board[x][y + 1], x, y + 1)

                        if self.board[x][y + 1].number > 0.5:
                            self.add_to_turned(self.board[x][y + 1])
                            show_piece(self.board[x][y + 1])
