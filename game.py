from board import Board
from menu import Menu
from common import Common
from actions import Actions

def processMove(move):
    arr = move.split(' ')
    if not arr[1]:
        print('Incomplete move')
        return
    print('The move you entered: ' + move)
    coordinate = mapCoordinateToArray(arr[0])
    coordinateDest = mapCoordinateToArray(arr[1])
    spacesBetween = chessBoard.getSpacesBetweenTwoSquares(coordinate, coordinateDest)
    legalMove = True
    for i in spacesBetween:
        print('SPACE: ' + str(i.x) + ' ' + str(i.y))
        piece = chessBoard.getPieceAt(i.x, i.y)
        print(piece.tostring())
#        print('Piece alliance: ' + piece.alliance)
 #       print('Current mover' + currentMove)
        if piece.alliance.lower() == currentMove.lower():
            legalMove = False
            print('There are pieces in the way and this is not a legal move')
            return Actions.ILLEGAL
        # Check destination to see if it is an enemy piece    
    
    movingPiece = chessBoard.getPieceAt(coordinate[0], coordinate[1])
    if movingPiece.alliance.lower() != currentMove.lower():
        if (movingPiece.alliance.lower() == 'white'):
            print('It is not White\'s turn...')
            return Actions.ILLEGAL
        else:
            print('It is not Black\'s turn...')
            return Actions.ILLEGAL
    
    # Capture enemy piece
    returnedPiece = chessBoard.getPieceAt(coordinateDest[0], coordinateDest[1])
    if returnedPiece.alliance and returnedPiece.alliance.lower() != currentMove.lower():
        print('Piece is an enemy and may attack')
        capturedPieces.append(returnedPiece)
        chessBoard.clearPieceAt(coordinate[0], coordinate[1])
        chessBoard.setPieceAt(coordinateDest[0], coordinateDest[1], movingPiece)
        return Actions.CAPTURE
    
    return Actions.MOVE

#print('The coordinate ' + coordinate)
    #print('The destination: ' + coordinateDest)
#    returnedPiece = chessBoard.getPieceAt(coordinateDest[0], Destcoordinate[1])
    
# print(returnedPiece.printUnrestrictedMoves())
   # print('Originating piece: ' + arr[0])
   # print('Destination: ' + arr[1])

    #print(returnedPiece.tostring())

def mapCoordinateToArray(coordinates):
    letters = Common.boardLetters
    letter = coordinates[0]
    number = 8 - int(coordinates[1])
    numberTranslation = int(number) 
    letterIndex = letters.index(letter)
  #  print(letter + str(number))
  #  print(str(letterIndex) + str(numberTranslation))
    return str(letterIndex) + str(numberTranslation)

if __name__ == '__main__':
    menu = Menu()
    option = menu.getInput()
    whiteWinner = False
    blackWinner = False
    quitGame = False
    currentMove = 'Black'
    command = ''

    match option:
        case '1':
            # Setup two player game
            chessBoard = Board()
            chessBoard.setupPiecesInitial()
            chessBoard.printColorfulBoard()
            capturedPieces = []
            while not quitGame and (not whiteWinner and not blackWinner):
                command = input(currentMove + '\'s move: ')
                if command.startswith('lookup'):
                    space = command.split(' ')[1]
                    coordinate = mapCoordinateToArray(space)
                    print(chessBoard.getPieceAt(coordinate[0],coordinate[1]).tostring())
                elif command == 't':
                    # Toggle turn for debugging
                    if currentMove.lower() == 'white':
                        currentMove = 'Black'
                        print('Black\'s turn')
                    elif currentMove.lower() == 'black':
                        currentMove = 'White'
                        print('White\'s turn')
                    else:
                        print('Error switching turn')
                elif command == 'q':
                    prompt = input('Are you sure you want to quit? ')
                    if prompt == 'y':
                        print('Goodbye')
                        quitGame = True
                if not quitGame and command != 't' and not command.startswith('lookup'):
                    moveResult = processMove(command)
                    print(moveResult)
                    chessBoard.printColorfulBoard()

        case 'q':
            print('Goodbye')
            exit
