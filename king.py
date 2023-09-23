from piece import Piece

class King(Piece):
    def __init__(self, alliance):
        super().__init__('K', alliance)
        self.canCastle = False
        self.isInCheck = False
        self.moveDirections = ['1 0', '-1 0', '1 1', '1 -1', '0 1', '0 -1',
                               '-1 -1', '-1 1']
