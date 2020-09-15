class Piece:
    def __init__(self, chance):
        self.show = False
        self.number = None
        self.flagged = False
        if chance < 9:
            self.type = 1  # Normal
        else:
            self.type = 0  # Mine

    def show_piece(self):
        self.show = True

    def flag_piece(self):
        self.flagged = True

    def unflag_piece(self):
        self.flagged = False
