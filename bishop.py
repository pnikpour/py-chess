from piece import Piece

class Bishop(Piece):
    def __init__(self, alliance):
        super().__init__('B', alliance)
        self.moveDirections = ['7 7', '-7 -7','7 -7','-7 7']
