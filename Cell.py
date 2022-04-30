# Cell.py

class Cell:
	def __init__(self, loc):
		# Parameters:
		# 	- loc: list of 2 integers 
		# 		tells the location of the cells
		self.loc 				= loc
		self.isOccupied			= False
		self.isTransformable 	= False
		self.Score 				= 0
		self.isAvailable		= False
		self.isBlack			= ((loc[0] + loc[1]) % 2) == 0
		self.piece				= None # chess piece objects
	
	def setPiece(self, Piece):
		self.isOccupied = True
		self.piece = Piece

	def removePiece(self):
		self.isOccupied = True
		self.piece = None