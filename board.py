import yaml
import collections
from space import Space
from piece import Piece
from pawn import Pawn
from rook import Rook
from knight import Knight
from bishop import Bishop
from queen import Queen
from king import King

from termcolor import colored, cprint

class Board:
    def __init__(self):
        config = yaml.safe_load(open('config/config.yaml'))
        self.boardDimensionMax = config['values']['boardDimensionMax']
        self.boardLetters = ['A','B','C','D','E','F','G','H']
        self.spaces = [
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()], 
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()], 
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()],  
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()], 
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()], 
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()], 
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()],  
           [Space(),Space(),Space(),Space(),Space(),Space(),Space(),Space()], 
        ]
 #       for i in range(self.boardDimensionMax):
  #          for k in range(self.boardDimensionMax):
   #             self.spaces.append(Space(k,i))


    def setPieceAt(self, x, y, piece):
        self.spaces[x][y].piece = piece

    def getPieceAt(self, x, y):
        return self.spaces[int(x)][int(y)].piece

    def lookupPiece(self, x, y):
        return self.getPieceAt(x, y).tostring()

    def setupPiecesInitial(self):
        # Start at "8" row and move downward
        # Black's key pieces
        self.setPieceAt(0, 0, Rook('black'))
        self.setPieceAt(1, 0, Knight('black'))
        self.setPieceAt(2, 0, Bishop('black'))
        self.setPieceAt(3, 0, Queen('black'))
        self.setPieceAt(4, 0, King('black'))
        self.setPieceAt(5, 0, Bishop('black'))
        self.setPieceAt(6, 0, Knight('black'))
        self.setPieceAt(7, 0, Rook('black'))

        # Black's pawns
        for i in range(int(self.boardDimensionMax)):
            self.setPieceAt(i, 1, Pawn('black'))
        # White's pawns
        for i in range(int(self.boardDimensionMax)):
            self.setPieceAt(i, 6, Pawn('white'))

        # Set the Board's space coordinates
        for i in range(int(self.boardDimensionMax)):
            for k in range(int(self.boardDimensionMax)):
                self.spaces[k][i].x = k
                self.spaces[k][i].y = i

        # White's key pieces
        self.setPieceAt(0, 7, Rook('white'))
        self.setPieceAt(1, 7, Knight('white'))
        self.setPieceAt(2, 7, Bishop('white'))
        self.setPieceAt(3, 7, Queen('white'))
        self.setPieceAt(4, 7, King('white'))
        self.setPieceAt(5, 7, Bishop('white'))
        self.setPieceAt(6, 7, Knight('white'))
        self.setPieceAt(7, 7, Rook('white'))

    def getSpacesBetweenTwoSquares(self, source, destination):
        # 0 0 ; 0 2
        spaces = []
        sourceX = int(source[0])
        sourceY = int(source[1])
        destX = int(destination[0])
        destY = int(destination[1])
        if destX > sourceX:
            print('destX > sourceX')
            difference = destX - sourceX
            inBetweenX = 0
            for i in range(destX-1, sourceX-1, -1):
                inBetweenY = sourceY
                inBetweenX = i
                spaces.append(self.spaces[inBetweenX][inBetweenY])
        elif destY > sourceY: 
            print('destY > sourceY')
            difference = destY - sourceY
            inBetweenY = 0
            for i in range(sourceY+1, destY+1, 1):
                inBetweenY = i
                inBetweenX = sourceX
                spaces.append(self.spaces[inBetweenX][inBetweenY])
        elif sourceY > destY: 
            print('sourceY > destY')
            difference = sourceY - destY
            inBetweenY = 0
            for i in range(sourceY-1, destY-1, -1):
                inBetweenY = i
                inBetweenX = sourceX
                spaces.append(self.spaces[inBetweenX][inBetweenY])
        elif sourceX > destX:
            print('sourceX > destX')
            difference = sourceX - destX
            inBetweenX = 0
            for i in range(sourceX-1, destX-1, -1):
                inBetweenX = i
                inBetweenY = sourceY
                spaces.append(self.spaces[inBetweenX][inBetweenY])
        else:
            print('Something wrong comparing two coordinates')
        return spaces

    def printPiece(self, piece, color, onColor, matchingOnColor):
            print(colored('[', matchingOnColor, onColor), end='')
            print(colored(piece.character, color, onColor), end='')
            print(colored(']', matchingOnColor, onColor), end='')
    def tostring(self):
        result = ''
        initialBottomRow = False
        row = 8
        for i in range(self.dimensionMax):
            result += str(row) + ' '
            for k in range(self.dimensionMax):
                result += (self.spaces[k][i].tostring())
                #result += ('[ ]'
            result += '\n'
            row -= 1
        # Print the last row containing A-H
        for c in self.boardLetters:
            if not initialBottomRow:
                result += '   ' + c
                initialBottomRow = True
            else:
                result += '  ' + c

        return result
    
    def printColorfulBoard(self): 
        onColor = ''
        initialBottomRow = False
        row = 8
        for i in range(self.boardDimensionMax):
            print(colored(str(row) + ' ', 'blue'), end='')
            for k in range(self.boardDimensionMax):
                # Calculate the board square color
                if k % 2 == 0 and i % 2 != 0:
                    onColor = 'on_dark_grey'
                    matchingOnColor = 'dark_grey'
                elif k % 2 != 0 and i % 2 == 0:
                    onColor = 'on_dark_grey'
                    matchingOnColor = 'dark_grey'
                elif k % 2 == 0 and i % 2 == 0:
                    onColor = 'on_green'
                    matchingOnColor = 'green'
                elif k % 2 != 0 and i % 2 != 0:
                    onColor = 'on_green'
                    matchingOnColor = 'green'

                pieceColor = 'white'
                if self.spaces[k][i].piece.alliance != 'white':
                    pieceColor = 'black'
#                print(colored(self.spaces[k][i].tostring(), pieceColor), end='')
                self.printPiece(self.spaces[k][i].piece, pieceColor, onColor, matchingOnColor)
                #result += ('[ ]'
            row -= 1
            print('\n', end='')
        # Print the last row containing A-H
        for c in self.boardLetters:
            if not initialBottomRow:
                print(colored('   ' + c, 'blue' ), end='')
                initialBottomRow = True
            else:
                print(colored('  ' + c, 'blue'), end='')
        print()

if __name__ == '__main__': 
    chessBoard = Board()
    chessBoard.setupPiecesInitial()
    #print(chessBoard.tostring())
    chessBoard.printColorfulBoard()
