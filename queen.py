from piece import Piece

class Queen(Piece):
    def __init__(self, alliance):
        super().__init__('Q', alliance)
        self.moveDirections = ['7 7', '-7 -7','7 -7','-7 7',
                               '0 7', '7 0', '-7 0', '0 -7']
