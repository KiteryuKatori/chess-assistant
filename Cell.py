# Cell.py

class Cell:
	def __init__(self, loc):
		# Parameters:
		# 	- loc: list of 2 integers 
		# 		tells the location of the cells
		self.loc 				= loc
		print(f"Cell class says hi at {self.loc}")
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

	def defineSelf(self):
		# assert self.piece == None, "The Cell is empty" 
		# the code above didn't work, why?

		if self.piece == None:
			print(f"Loc = {self.loc}, The cell is empty")
			return
		print(f"Loc = {self.loc}, Piece = {self.piece.name}")

