
class Piece:
    def __init__(self, character = ' ', alliance = ''):
        self.character = character
        self.alliance = alliance
        self.moveDirections = []
    def tostring(self):
        return 'Character: ' + self.character + '\nAlliance:' + self.alliance

    def printUnrestrictedMoves(self):
        for i in self.moveDirections:
            print(i)
