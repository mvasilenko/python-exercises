import copy


def isValidChessBoard(board):
    validBlackFigures = {'king': 1, 'queen': 1,
                         'rook': 2, 'bishop': 2, 'knight': 2, 'pawn': 8}
    validWhiteFigures = copy.deepcopy(validBlackFigures)
    validNumberPositions = [i for i in range(1, 8+1)]
    validAlphaPositions = [chr(j) for j in range(ord('a'), ord('h')+1)]

    for k, v in board.items():
        if int(k[0]) in validNumberPositions and k[1] in validAlphaPositions:
            figure = v[1:]
            if v[0] == 'b' and figure in validBlackFigures:
                if validBlackFigures[figure] > 0:
                    validBlackFigures[figure] -= 1
                else:
                    return False
            elif v[0] == 'w' and figure in validWhiteFigures:
                if validWhiteFigures[figure] > 0:
                    validWhiteFigures[figure] -= 1
                else:
                    return False
            else:
                return False
        else:
            return False
    return True


board = {'1h': 'bking', '6c': 'wqueen',
         '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}
print(isValidChessBoard(board))

# return False
board = {'1h': 'bking', '6c': 'wqueen',
         '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', '1a': "wking"}
print(isValidChessBoard(board))
