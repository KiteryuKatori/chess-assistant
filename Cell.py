# Cell.py
from curses.ascii import EM
from queue import Empty


class Cell:
	def __init__(self, loc):
		print("Cell class says hi.")
		# Parameters:
		# 	- loc: list of 2 integers
		# 		tells the location of the cells
		self.loc 				= loc
		self.isTransformable 	= False
		self.Score 				= 0
		self.isAvailable		= False
		self.isBlack			= ((loc[0] + loc[1]) % 2) == 0
		self.piece				= "" # chess piece objects
	
	def setPiece(self, Piece):
		self.piece = Piece

	def removePiece(self):
		self.piece = ""

	def showPiece(self):
		return self.piece

	def defineSelf(self):
		print(f"Loc = {self.loc}, Piece = {self.piece.name}")
		# print(f"Loc = {self.loc}, Piece = {self.piece.name}") how to return self.piece as an empty object without importing EM? 

