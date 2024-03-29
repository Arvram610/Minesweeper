import pygame

from modules.Board import Board, show_piece, flag_piece, unflag_piece
from modules.constants import WIDTH, HEIGHT, SQSX, SQSY


def main():
    """Setup"""
    pygame.init()
    WIN = pygame.display.set_mode((HEIGHT, WIDTH))
    running = True
    board = Board()
    turn = 0

    """Initialise main loop"""
    while running:

        """Checks for Keypress"""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:  # Quit Action
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:

                """ Checks left mouse button """
                if pygame.mouse.get_pressed()[0]:
                    x, y = pygame.mouse.get_pos()
                    piece = board.get_piece(int(x // SQSX), int(y // SQSY))
                    if not piece.type or piece.number != 0:
                        if not turn:
                            Start_Loop = True
                            while Start_Loop:
                                board.make_board()
                                piece = board.get_piece(int(x // SQSX), int(y // SQSY))
                                if piece.type and not piece.number:
                                    Start_Loop = False

                                    board.turn_near(piece, int(x // SQSX), int(y // SQSY))
                                    turn = 1

                    if not piece.flagged:

                        turn = 1
                        if piece.type and not piece.number:
                            board.turn_near(piece, int(x // SQSX), int(y // SQSY))
                        else:
                            show_piece(piece)

                            if not piece.type:
                                running = False

                """ Checks right mouse button """
                if pygame.mouse.get_pressed()[2] and turn:
                    x, y = pygame.mouse.get_pos()
                    piece = board.get_piece(int(x // SQSX), int(y // SQSY))
                    if not piece.flagged and not piece.show:
                        flag_piece(piece)
                    elif piece.flagged and not piece.show:
                        unflag_piece(piece)

        """ Draws board and updates """
        board.draw_board(WIN)
        pygame.display.update()

    pygame.quit()


if __name__ == "__main__":
    main()
