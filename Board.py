# Board.py
from Cell import Cell
from Piece import Piece

class Board:
	BOARD_SIDE = 8
    
	def __init__(self):
		print("Hello from Board class")

		self.board = list()
		for x in range(Board.BOARD_SIDE):
			row = list()
			for y in range(Board.BOARD_SIDE):
				# NOTE: Cell loc is the index+1, so reflect on our past codes to see if we use the location/index appropriately
				row.append(Cell([x + 1, y + 1]))

			self.board.append(row)

		self.board[0][0].setPiece(Piece("rook", True))
		self.board[0][1].setPiece(Piece("knight", True))
		self.board[0][2].setPiece(Piece("bishop", True))
		self.board[0][3].setPiece(Piece("queen", True))
		self.board[0][4].setPiece(Piece("king", True))
		self.board[0][5].setPiece(Piece("bishop", True))
		self.board[0][6].setPiece(Piece("knight", True))
		self.board[0][7].setPiece(Piece("rook", True))		
		self.board[1][0].setPiece(Piece("pawn", True))
		self.board[1][1].setPiece(Piece("pawn", True))
		self.board[1][2].setPiece(Piece("pawn", True))
		self.board[1][3].setPiece(Piece("pawn", True))
		self.board[1][4].setPiece(Piece("pawn", True))
		self.board[1][5].setPiece(Piece("pawn", True))
		self.board[1][6].setPiece(Piece("pawn", True))
		self.board[1][7].setPiece(Piece("pawn", True))

		self.board[7][0].setPiece(Piece("rook", False))
		self.board[7][1].setPiece(Piece("knight", False))
		self.board[7][2].setPiece(Piece("bishop", False))
		self.board[7][3].setPiece(Piece("king", False))
		self.board[7][4].setPiece(Piece("queen", False))
		self.board[7][5].setPiece(Piece("bishop", False))
		self.board[7][6].setPiece(Piece("knight", False))
		self.board[7][7].setPiece(Piece("rook", False))		
		self.board[6][0].setPiece(Piece("pawn", False))
		self.board[6][1].setPiece(Piece("pawn", False))
		self.board[6][2].setPiece(Piece("pawn", False))
		self.board[6][3].setPiece(Piece("pawn", False))
		self.board[6][4].setPiece(Piece("pawn", False))
		self.board[6][5].setPiece(Piece("pawn", False))
		self.board[6][6].setPiece(Piece("pawn", False))
		self.board[6][7].setPiece(Piece("pawn", False))

	def getBoard(self):
		return self.board

	def visualize(self) -> None:
		"""
		   0    1    2    3   4    5   6    7
		  --- --- --- --- --- --- --- --- --- --
		0| ♜ | ♞ | ♝ | ♛ | ♚ | ♝ | ♞ | ♜ |
		  --- --- --- --- --- --- --- --- --- --
		1| ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ | ♟ |
		  --- --- --- --- --- --- --- --- --- --
		2|    |   |    |    |    |   |    |    |
		  --- --- --- --- --- --- --- --- --- --
		3|    |   |    |    |    |   |    |    |
		  --- --- --- --- --- --- --- --- --- --
		4|    |   |    |    |    |   |    |    |
		  --- --- --- --- --- --- --- --- --- --
		5|    |   |    |    |    |   |    |    |
		  --- --- --- --- --- --- --- --- --- --
		6| ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ | ♙ |
	  	  --- --- --- --- --- --- --- --- --- --
		7| ♖ | ♘ | ♗ | ♔ | ♕ | ♗ | ♘ | ♖ |
	  	  --- --- --- --- --- --- --- --- --- --
		"""
		boardToVisualize = []
  
		for row in self.board:
			rowVisualized = []
			for cell in row:
				piece = cell.piece
				if isinstance(piece, Piece):
					rowVisualized.append(piece.getImage())
				else:
					rowVisualized.append('')
			boardToVisualize.append(rowVisualized)
		
		def printBoardWPiece(currentBoardState: list) -> None:
			"""Print the Board with Piece image, row divison '---', index for rows and columns

			Args:
				currentBoardState (list): current state of the board array
			"""
			print('   ' + '   '.join([str(colNumber) for colNumber in range(Board.BOARD_SIDE)]) )
			rowNumber = 0
			for row in currentBoardState:
				print(' ' + ' ---' * Board.BOARD_SIDE) 
				print(str(rowNumber) + '', end='')
				for piece in row:
					if piece == '':
						print('|   ', end='')
					else:
						print(f'| {piece} ', end='')
				print('|')
				rowNumber += 1
			print('  ' + ' ---' * Board.BOARD_SIDE) 
			
		printBoardWPiece(boardToVisualize)
	
	
  
board_init = Board()
board_init.visualize()