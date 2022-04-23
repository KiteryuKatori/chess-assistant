# Piece.py
class Piece:
	def __init__(self, name, isBlack):
		# Parameters
		# 	- name: string
		# 		accepted: [king, queen, pawn, rook, bishop, knight]
		# 	- isBlack: bool
		# 		accepted: []
		# Attributes:
		# 	- name: 		string
		#   - isBlack: 		bool
		# 	- image: 		string, accept one of special char
		# 	- isAlive:		bool
		# 	- isAvailable:	bool, used to tell if this the turn to move
		# 	- isSelected:	bool, used to tell if player choose to move
		# 	- SCORE:		integer, used for Minimax algo
		# Method:
		# 	- move()
		
		self.name = name
		self.isBlack = isBlack

		self.image = str() # ♔ ♚ ♕ ♛ ♗ ♝ ♘ ♞ ♙ ♟ ♖ ♜
		self.isAlive = True
		