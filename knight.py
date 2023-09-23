from piece import Piece

class Knight(Piece):
    def __init__(self, alliance):
        super().__init__('N', alliance)
        self.moveDirections = ['2 1','2 -1','-2 1','-2 -1' \
                '1 2','1 -2','-1 -2','-1 2']
