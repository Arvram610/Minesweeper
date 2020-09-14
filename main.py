import pygame
from modules.constants import WIDTH, HEIGHT, SQSX, SQSY
from modules.Board import Board, show_piece, flag_piece, unflag_piece


def main():
    """Setup"""
    pygame.init()
    WIN = pygame.display.set_mode((HEIGHT, WIDTH))
    running = True
    board = Board()

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
                    piece = board.get_piece(int(x//SQSX), int(y//SQSY))
                    if not piece.flagged:
                        show_piece(piece)
                        if not piece.type:
                            running = False

                """ Checks right mouse button """
                if pygame.mouse.get_pressed()[2]:
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
