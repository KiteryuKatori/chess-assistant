# Cell.py
class Cell:
	def __init__(self, loc):
		# Parameters:
		# 	- loc: list of 2 integers
		# 		tells the location of the cells
		self.loc 				= loc
		self.isOccupied 		= False
		self.isTransformable 	= False
		self.Score 				= 0
		self.isAvailable		= False
		self.isBlack			= ((loc[0] + loc[1]) % 2) == 0

		self.piece				= "" # chess piece objects
		
