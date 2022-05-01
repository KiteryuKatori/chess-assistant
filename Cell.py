# Cell.py

class Cell:
  
  
	def __init__(self, loc):
		# Parameters:
		# 	- loc: list of 2 integers 
		# 		tells the location of the cells

		self.loc 				= loc
		self.isOccupied			= False
		self.isTransformable 	= False
		self.Score 				= 0 		# transformable = 100, 
		self.isAvailable		= False
		self.isBlack			= ((loc[0] + loc[1]) % 2) == 0
		self.piece				= None # chess piece objects
	
	def setPiece(self, Piece):
		self.isOccupied = True
		self.piece = Piece

	def removePiece(self):
		self.isOccupied = True
		self.piece = None


	def showPossibleMoves(self, currentBoardState):
		"""
		Parameters:
			- currentBoardState: Board object
				shows the current state of the chess board
		Return:
			- `listOfPossibleMoves`: list<list<2 integers>>
				tells all the possible moves of a piece ON this CELL
		Extra: #for further use
			- `listOfCapturableCell`: list<list<2 integers>>
				tells ONLY the capturable cells from the upper list
		Logic:
			`listOfLegalMoves` is a MUST-HAVE parameter 
			in the main area of the function, `listOfLegalMoves`
			will be used to check if it is any conflict like,
			move on the same cell or eat the same color piece.
		"""
		if self.isOccupied == False:
			return list()

		listOfLegalMoves = list()
		listOfCapturableCell = list()
		name = self.piece.name

		def rookMoves(forRange, counter, direction): #append Cells that are Legal for Rook
			for i in range(forRange):
				if direction == "v" or direction == "V": #vertical			
					listOfLegalMoves.append(currentBoardState.board[counter][self.loc[1]])
					if currentBoardState.board[counter][self.loc[1]].isOccupied == 1:
						break
				if direction == "h" or direction == "H": #horizontal				
					listOfLegalMoves.append(currentBoardState.board[self.loc[0]][counter])
					if currentBoardState.board[self.loc[0]][counter].isOccupied == 1:
						break


		if name == "king":
			listOfLegalMoves = list(
				set(
					[max(self.loc[0] - 1, 1), max(self.loc[1] - 1, 1)], # top 	 left  cell
					[max(self.loc[0] - 1, 1),     self.loc[1]        ], # top 	       cell	
					[max(self.loc[0] - 1, 1), min(self.loc[1] + 1, 8)], # top 	 right cell
					[	 self.loc[0]        , max(self.loc[1] - 1, 1)], #        left  cell
					[	 self.loc[0]        , max(self.loc[1] + 1, 8)], #     	 right cell
					[min(self.loc[0] + 1, 8), max(self.loc[1] - 1, 1)], # bottom left  cell
					[min(self.loc[0] + 1, 8), 	  self.loc[1]		 ],	# bottom       cell
					[min(self.loc[0] + 1, 8), min(self.loc[1] + 1, 8)]	# bottom right cell
				)
			)


		elif name == "knight":
			delta = ["1","2"]
			operator = ["+", "-"]
			for i in range(len(delta)):
				i_ = (i+1)%2 # get the other delta number
				for j in range(len(operator)):
					for k in range(len(operator)):
						pairLoc = [
							eval(f"{self.loc[0]} {operator[k]} {delta[i]}"),
							eval(f"{self.loc[1]} {operator[j]} {delta[i_]}")]
						if (1 <= pairLoc[0] <= 8) and (1 <= pairLoc[1] <= 8):
							listOfLegalMoves.append(pairLoc)


		elif name == "rook":
			rookMoves(8 - self.loc[0], self.loc[0] + i, "v") #Up
			rookMoves(	  self.loc[0], self.loc[0] - i, "v") #Down
			rookMoves(8 - self.loc[1], self.loc[1] + i, "h") #Right
			rookMoves(	  self.loc[1], self.loc[1] - i, "h") #Left
					

		elif name == "bishop":
			pass


		elif name == "queen":
			pass


		elif name == "pawn":
			pass


		listOfPossibleMoves = list()
		for cellLoc in listOfLegalMoves:
			if cellLoc == self.loc:
				continue

			possibleCell = currentBoardState.board[cellLoc[0] - 1][cellLoc[1] - 1]

			listOfPossibleMoves.append(possibleCell)

			# if not possibleCell.isOccupied:
			# 	listOfPossibleMoves.append(possibleCell)
			# elif possibleCell.piece.isBlack != self.piece.isBlack:
			# 	listOfPossibleMoves.append(possibleCell)

		return listOfPossibleMoves
