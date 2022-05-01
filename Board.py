# Board.py
from Cell import *
from Piece import *
class Board:

	def __init__(self):
		pieceList = ['king', 'queen', 'rook', 'knight', 'bishop', 'pawn']

		self.board = list()
		for x in range(8):
			row = list()
			for y in range(8):
				row.append(Cell([x + 1, y + 1]))

			self.board.append(row)

		# self.board[0][0].setPiece(Piece("rook", True))
		# self.board[0][1].setPiece(Piece("knight", True))
		# self.board[0][2].setPiece(Piece("bishop", True))
		# self.board[0][3].setPiece(Piece("queen", True))
		# self.board[0][4].setPiece(Piece("king", True))
		# self.board[0][5].setPiece(Piece("bishop", True))
		# self.board[0][6].setPiece(Piece("knight", True))
		# self.board[0][7].setPiece(Piece("rook", True))		
		# self.board[1][0].setPiece(Piece("pawn", True))
		# self.board[1][1].setPiece(Piece("pawn", True))
		# self.board[1][2].setPiece(Piece("pawn", True))
		# self.board[1][3].setPiece(Piece("pawn", True))
		# self.board[1][4].setPiece(Piece("pawn", True))
		# self.board[1][5].setPiece(Piece("pawn", True))
		# self.board[1][6].setPiece(Piece("pawn", True))
		# self.board[1][7].setPiece(Piece("pawn", True))

		# self.board[7][0].setPiece(Piece("rook", False))
		# self.board[7][1].setPiece(Piece("knight", False))
		# self.board[7][2].setPiece(Piece("bishop", False))
		# self.board[7][3].setPiece(Piece("king", False))
		# self.board[7][4].setPiece(Piece("queen", False))
		# self.board[7][5].setPiece(Piece("bishop", False))
		# self.board[7][6].setPiece(Piece("knight", False))
		# self.board[7][7].setPiece(Piece("rook", False))		
		# self.board[6][0].setPiece(Piece("pawn", False))
		# self.board[6][1].setPiece(Piece("pawn", False))
		# self.board[6][2].setPiece(Piece("pawn", False))
		# self.board[6][3].setPiece(Piece("pawn", False))
		# self.board[6][4].setPiece(Piece("pawn", False))
		# self.board[6][5].setPiece(Piece("pawn", False))
		# self.board[6][6].setPiece(Piece("pawn", False))
		# self.board[6][7].setPiece(Piece("pawn", False))

		for i in range(3):
				#White
			self.board[0][i].setPiece(Piece(f"{pieceList[i + 2]}", 0))
			self.board[0][7-i].setPiece(Piece(f"{pieceList[i + 2]}", 0))
			#Black
			self.board[7][i].setPiece(Piece(f"{pieceList[i + 2]}", 1))
			self.board[7][7-i].setPiece(Piece(f"{pieceList[i + 2]}", 1))

		for i in range(8):
			self.board[1][i].setPiece(Piece("pawn", 0))
			self.board[6][i].setPiece(Piece("pawn", 1))
			
		self.board[0][3].setPiece(Piece("queen", 0))
		self.board[0][4].setPiece(Piece("king", 0))
		self.board[7][3].setPiece(Piece("king", 1))
		self.board[7][4].setPiece(Piece("queen", 1))
		#You can check it in "another_scrap.py"

	def getBoard(self):
		return self.board


	def visualize(self):
		pass