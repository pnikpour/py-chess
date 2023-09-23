from piece import Piece

class Pawn(Piece):
    def __init__(self, alliance):
        super().__init__('p', alliance)
        self.hasMoved = False
        self.canEnPassant = False
        self.canAttack = False

        if self.alliance == 'white':
            if not self.hasMoved:
                self.moveDirections += ['0 2']
            self.moveDirections += ['0 1']
            if self.canAttack:
                self.moveDirections += ['1 1','-1 1']
        else:
            if not self.hasMoved:
                self.moveDirections += ['0 -2']
            self.moveDirections += ['0 -1']
            if self.canAttack:
                self.moveDirections += ['1 -1','-1 -1']
