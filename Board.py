# Board.py
from Cell import *
from Piece import *
class Board:
	def __init__(self):
		print("Hello from Board class")

		self.board = list()
		for x in range(8):
			row = list()
			for y in range(8):
				row.append(Cell([x + 1, y + 1]))

			self.board.append(row)

		self.board[0][0].piece = Piece("rook", 	 True)
		self.board[0][1].piece = Piece("knight", True)
		self.board[0][2].piece = Piece("bishop", True)
		self.board[0][3].piece = Piece("queen",  True)
		self.board[0][4].piece = Piece("king", 	 True)
		self.board[0][5].piece = Piece("bishop", True)
		self.board[0][6].piece = Piece("knight", True)
		self.board[0][7].piece = Piece("rook", 	 True)		
		self.board[1][0].piece = Piece("pawn", 	 True)
		self.board[1][1].piece = Piece("pawn", 	 True)
		self.board[1][2].piece = Piece("pawn",   True)
		self.board[1][3].piece = Piece("pawn",   True)
		self.board[1][4].piece = Piece("pawn", 	 True)
		self.board[1][5].piece = Piece("pawn", 	 True)
		self.board[1][6].piece = Piece("pawn", 	 True)
		self.board[1][7].piece = Piece("pawn",   True)

		self.board[7][0].piece = Piece("rook", 	 True)
		self.board[7][1].piece = Piece("knight", True)
		self.board[7][2].piece = Piece("bishop", True)
		self.board[7][3].piece = Piece("king",   True)
		self.board[7][4].piece = Piece("queen",  True)
		self.board[7][5].piece = Piece("bishop", True)
		self.board[7][6].piece = Piece("knight", True)
		self.board[7][7].piece = Piece("rook", 	 True)		
		self.board[6][0].piece = Piece("pawn", 	 True)
		self.board[6][1].piece = Piece("pawn", 	 True)
		self.board[6][2].piece = Piece("pawn",   True)
		self.board[6][3].piece = Piece("pawn",   True)
		self.board[6][4].piece = Piece("pawn", 	 True)
		self.board[6][5].piece = Piece("pawn", 	 True)
		self.board[6][6].piece = Piece("pawn", 	 True)
		self.board[6][7].piece = Piece("pawn",   True)

	def getBoard(self):
		return self.board
		