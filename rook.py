from piece import Piece

class Rook(Piece):
    def __init__(self, alliance):
        super().__init__('R', alliance)
        for i in range(-8, 8, 1):
            self.moveDirections += ['0 ' + str(i)]
            self.moveDirections += [str(i) + ' 0']
