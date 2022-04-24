
class Piece:
    
    imageDatabase = {
        'king': ('♔', '♚'),
        'queen': ('♕', '♛'),
        'rook': ('♖', '♜'),
        'knight': ('♘', '♞'),
        'bishop': ('♗', '♝'),
        'pawn': ('♙', '♟')
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


def printBoard() -> None:
    print('    ' + '   '.join([str(col) for col in range(8)]) )
    for row in range(8):
        print('  ' + ' ---' * 8) 
        print(str(row) + ' ' + '|   ' * 8 + '|' )
    print('  ' + ' ---' * 8) 
    
    

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
    

imageDict = {
    'king': ['♔', '♚'],
    'queen': ['♕', '♛'],
    'rook': ['♖', '♜'],
    'knight': ['♘', '♞'],
    'bishop': ['♗', '♝'],
    'pawn': ['♙', '♟']
}

board = [[" "] * 8 for _ in range(8)]

board[0][0] = Piece("rook",   True)
board[0][1] = Piece("knight", True)
board[0][2] = Piece("bishop", True)
board[0][3] = Piece("queen",  True)
board[0][4] = Piece("king",   True)
board[0][5] = Piece("bishop", True)
board[0][6] = Piece("knight", True)
board[0][7] = Piece("rook",   True)		
board[1][0] = Piece("pawn",   True)
board[1][1] = Piece("pawn",   True)
board[1][2] = Piece("pawn",   True)
board[1][3] = Piece("pawn",   True)
board[1][4] = Piece("pawn",   True)
board[1][5] = Piece("pawn",   True)
board[1][6] = Piece("pawn",   True)
board[1][7] = Piece("pawn",   True)

board[7][0] = Piece("rook",   False)
board[7][1] = Piece("knight", False)
board[7][2] = Piece("bishop", False)
board[7][3] = Piece("king",   False)
board[7][4] = Piece("queen",  False)
board[7][5] = Piece("bishop", False)
board[7][6] = Piece("knight", False)
board[7][7] = Piece("rook",   False)		
board[6][0] = Piece("pawn",   False)
board[6][1] = Piece("pawn",   False)
board[6][2] = Piece("pawn",   False)
board[6][3] = Piece("pawn",   False)
board[6][4] = Piece("pawn",   False)
board[6][5] = Piece("pawn",   False)
board[6][6] = Piece("pawn",   False)
board[6][7] = Piece("pawn",   False)

board_visualized = []

for row in board:
    row_visualized = []
    for piece in row:
        if isinstance(piece, Piece):
            row_visualized.append(piece.getImage())
        else:
            row_visualized.append('')
    
    board_visualized.append(row_visualized)

# for row in board_update:
#     for piece in row:
#         if piece == '': piece = '*'
#         print(piece, end = ' ')
#     print()    
    
printBoardWPiece(board_visualized)