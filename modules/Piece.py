class Piece:
    def __init__(self):
        self.show = False
        self.number = None
        self.flagged = False
        self.type = 1

    def make_mine(self):
        self.type = 0

    def show_piece(self):
        self.show = True

    def flag_piece(self):
        self.flagged = True

    def unflag_piece(self):
        self.flagged = False
