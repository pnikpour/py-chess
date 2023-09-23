from piece import Piece

class Space:
    def __init__(self, x = 0, y = 0, piece = Piece()):
        self.piece = piece
        self.x = x
        self.y = y

    def tostring(self):
        return '[' + self.piece.character + ']'
