
class Piece:
    
##    imageDatabase = {
##        'king': ('♔', '♚'),
##        'queen': ('♕', '♛'),
##        'rook': ('♖', '♜'),
##        'knight': ('♘', '♞'),
##        'bishop': ('♗', '♝'),
##        'pawn': ('♙', '♟')
##    }

    imageDatabase = {
        'king': ('♔', 'BK'),
        'queen': ('♕', 'BQ'),
        'rook': ('♖', 'BR'),
        'knight': ('♘', 'Bk'),
        'bishop': ('♗', 'BB'),
        'pawn': ('♙', 'BP')
    }

    def __init__(self, name, isBlack):

        self.name = name
        self.isBlack = int(isBlack) # 1 if Black, 0 if White

        # Raise KeyError if `name` not in `imageDatabase`
        self.image = Piece.imageDatabase[self.name][self.isBlack] # ♔ ♚ ♕ ♛ ♗ ♝ ♘ ♞ ♙ ♟ ♖ ♜
        self.isAlive = True

    def getImage(self):
        return self.image

    def printImage(self): 
        print(self.image)


# def printBoard() -> None:
#     print('    ' + '   '.join([str(col) for col in range(8)]) )
#     for row in range(8):
#         print('  ' + ' ---' * 8) 
#         print(str(row) + ' ' + '|   ' * 8 + '|' )
#     print('  ' + ' ---' * 8) 

def printBoardWPiece(board) -> None:
    BOARD_SIDE= range(8)
    print('   ' + '   '.join([str(col_num) for col_num in BOARD_SIDE]) )
    row_num = 0
    for row in board:
        print(' ' + ' ---' * 8) 
        print(str(row_num) + '', end='')
        for piece in row:
            if piece == '':
                print('|   ', end='')
            else:
                print(f'| {piece} ', end='')
        print('|')
        row_num += 1
    print('  ' + ' ---' * 8) 
    

board = [[" "] * 8 for _ in range(8)]

pieceList = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']

for i in range(3):
    #Black
    board[7][i]=Piece(f"{pieceList[i + 2]}", 1)
    board[7][7-i]=Piece(f"{pieceList[i + 2]}", 1)
    #White
    board[0][i]=Piece(f"{pieceList[i + 2]}", 0)
    board[0][7-i]=Piece(f"{pieceList[i + 2]}", 0)

for i in range(8):
    #Black
    board[6][i]=Piece("pawn", 1)
    #White
    board[1][i]=Piece("pawn", 0)

board[0][3] = Piece("queen", 0)
board[0][4] = Piece("king", 0)
board[7][3] = Piece("king", 1)
board[7][4] = Piece("queen", 1)

board_update = []

for row in board:
    row_visualized = []
    for piece in row:
        if isinstance(piece, Piece):
            row_visualized.append(piece.getImage())
        else:
            row_visualized.append('')
    
    board_update.append(row_visualized)

# printBoard()
# print()
printBoardWPiece(board_update)
