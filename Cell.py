# Cell.py


from Piece import Piece
from Board import Board


class Cell:
	def __init__(self, loc):
		# Parameters:
		# 	- loc: list of 2 integers 
		# 		tells the location of the cells

		self.loc 				= loc		#[row, collumn]
		self.isOccupied			= False
		self.isTransformable 	= False
		self.Score 				= 0 		# transformable = 100, stepToTransformable = ? -> self.Score -= stepToTransformable * aNumber
		self.isAvailable		= False
		self.isBlack			= ((loc[0] + loc[1]) % 2) == 0
		self.piece				= None	# chess piece objects
	

	def setPiece(self, Piece: Piece):
		self.isOccupied = True
		self.piece = Piece


	def removePiece(self):
		self.isOccupied = True
		self.piece = None


	def showPossibleMoves(self, currentBoardState: Board) -> list:

		"""
		Parameters:
		- currentBoardState: Board object
		shows the current state of the chess board
		Return:
			- `listOfPossibleMoves`: list<list<2 integers>>
				tells all the possible moves of a piece ON this CELL
		Logic:
		`listOfLegalMoves` is a MUST-HAVE parameter 
		in the main area of the function, `listOfLegalMoves`
		will be used to check if it is any conflict like,
		move on the same cell or eat the same color piece.
		"""
		if self.isOccupied == False:
			return list()

		listOfLegalMoves = list()
		name = self.piece.name


		if name == "king":
			listOfLegalMoves = list(
				set([
					[max(self.loc[0] - 1, 1), max(self.loc[1] - 1, 1)], # top 	 left  cell
					[max(self.loc[0] - 1, 1),     self.loc[1]        ], # top 	       cell	
					[max(self.loc[0] - 1, 1), min(self.loc[1] + 1, 8)], # top 	 right cell
					[	 self.loc[0]        , max(self.loc[1] - 1, 1)], #        left  cell
					[	 self.loc[0]        , max(self.loc[1] + 1, 8)], #     	 right cell
					[min(self.loc[0] + 1, 8), max(self.loc[1] - 1, 1)], # bottom left  cell
					[min(self.loc[0] + 1, 8), 	  self.loc[1]		 ],	# bottom       cell
					[min(self.loc[0] + 1, 8), min(self.loc[1] + 1, 8)]	# bottom right cell
					]
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
							eval(f"{self.loc[1]} {operator[j]} {delta[i_]}")
       					]
						if (1 <= pairLoc[0] <= 8) and (1 <= pairLoc[1] <= 8):
							listOfLegalMoves.append(pairLoc)


		elif name == "pawn":
			pawn: Piece = self.piece
			orgRow = self.loc[0] - 1 # index of current row
			orgCol = self.loc[1] + 1 # index of current column
			
			# Pawn generally can only move one step a time
			# At starting position, pawn can take two steps forward.
			legalStep = 1 if pawn.hasTakenFirstMove else 2
	
			if not pawn.isBlack:
				# I. MOVE
				# White pawn moves from row 2 (of index 1), towards row 8 (of index 7),
				# The row increases while the column stays the same
				# When the Cell ahead is occupied, pawn cannot travel.
				for step in range(1, legalStep + 1):
					if currentBoardState.board[orgRow + step][orgCol].isOccupied:
						break
					listOfLegalMoves.append([orgRow + step, orgCol]) 

				# II. ATTACK
				# White pawn can attack diagonally,
				# if the diagonal Cell contains a Piece of opposite color
				cellDiagnonalUpRight: Cell = currentBoardState[orgRow + 1][orgCol + 1]
				cellDiagnonalUpLeft: Cell = currentBoardState[orgRow + 1][orgCol - 1]
    
				if cellDiagnonalUpRight.isOccupied  \
    				and cellDiagnonalUpRight.piece.isBlack :
					listOfLegalMoves.append([orgRow + 1, orgCol + 1])
	
				elif cellDiagnonalUpLeft.isOccupied \
        			and cellDiagnonalUpLeft.piece.isBlack:
					listOfLegalMoves.append([orgRow + 1, orgCol - 1])
     
			else:
				# I. MOVE
				# Black pawn moves from row 8 (of index 7), towards row 1 (of index 0),
				# The row decreases while the column stays the same
				# When the Cell ahead is occupied, pawn cannot travel.
				for step in range(legalStep, 0, -1):
					if currentBoardState.board[orgRow - step][orgCol].isOccupied:
						break
					listOfLegalMoves.append([orgRow - step, orgCol]) 

				# II. ATTACK
				cellDiagnonalDownRight: Cell = currentBoardState[orgRow + 1][orgCol + 1]
				cellDiagnonalDownLeft: Cell = currentBoardState[orgRow + 1][orgCol - 1]
    
				if cellDiagnonalDownRight.isOccupied \
    				and not cellDiagnonalDownRight.piece.isBlack :
					listOfLegalMoves.append([orgRow - 1, orgCol + 1])
	
				elif cellDiagnonalDownLeft.isOccupied \
        			and not cellDiagnonalDownLeft.piece.isBlack:
					listOfLegalMoves.append([orgRow - 1, orgCol - 1])
				
			# WAITING "EN PASSE" situation

		else:
			#remove excess space + time defining the same functions
			orgRow = self.loc[0] - 1 #original Row Index
			orgColumn = self.loc[1] - 1 #original Collumn Index


			def rookMoves(): #append Cells that are Legal for Rook (Tried to make a function but no use -> hardcode instead)
				#toUp
				for i in range(8 - orgRow - 1): #subtract 1 from the loop range to ensure everything is in the board
					listOfLegalMoves.append(currentBoardState.board[orgRow + i + 1][orgColumn].loc) #exclude it's own loc (loop start from 0 so we have to + 1)
					if currentBoardState.board[orgRow + i + 1][orgColumn].isOccupied: #End the loop when the last Cell is occupied(still take it's loc)
						break
				
				# listOfLegalMoves.append([99, 99])

				#toDown
				for i in range(orgRow): #skip self.loc[0] by adding "-1"
					listOfLegalMoves.append(currentBoardState.board[orgRow - i - 1][orgColumn].loc)
					if currentBoardState.board[orgRow - i - 1][orgColumn].isOccupied:
						break

				#toRight
				for i in range(8 - orgColumn - 1):
					listOfLegalMoves.append(currentBoardState.board[orgRow][orgColumn + i + 1].loc)
					if currentBoardState.board[orgRow][orgColumn + i + 1].isOccupied:
						break

				#toLeft
				for i in range(orgColumn):
					listOfLegalMoves.append(currentBoardState.board[orgRow][orgColumn - i - 1].loc)
					if currentBoardState.board[orgRow][orgColumn - i - 1].isOccupied:
						break

			
			def bishopMoves():
				tempRow = orgRow
				tempCol = orgColumn

				# toUpperRight
				while tempRow < 8 and tempCol < 8:
					tempCol += 1
					tempRow += 1
					if tempRow == 8 or tempCol == 8 or tempRow == -1 or tempCol == -1:
						break
					listOfLegalMoves.append(currentBoardState.board[tempRow][tempCol].loc)
					if currentBoardState.board[tempRow][tempCol].isOccupied:
						break

				#toUpperLeft
				tempRow = orgRow
				tempCol = orgColumn
				while tempRow > -1 and tempCol < 8:
					tempCol -= 1
					tempRow += 1
					if tempRow == 8 or tempCol == 8 or tempRow == -1 or tempCol == -1:
						break
					listOfLegalMoves.append(currentBoardState.board[tempRow][tempCol].loc)
					if currentBoardState.board[tempRow][tempCol].isOccupied:
						break

				#toLowerRight
				tempRow = orgRow
				tempCol = orgColumn
				while tempRow < 8 and tempCol > -1:
					tempCol += 1
					tempRow -= 1
					if tempRow == 8 or tempCol == 8 or tempRow == -1 or tempCol == -1:
						break
					listOfLegalMoves.append(currentBoardState.board[tempRow][tempCol].loc)
					if currentBoardState.board[tempRow][tempCol].isOccupied:
						break

				#toLowerLeft
				tempRow = orgRow
				tempCol = orgColumn
				while tempRow > -1 and tempCol > -1:
					tempCol -= 1
					tempRow -= 1
					if tempRow == 8 or tempCol == 8 or tempRow == -1 or tempCol == -1:
						break
					listOfLegalMoves.append(currentBoardState.board[tempRow][tempCol].loc)
					if currentBoardState.board[tempRow][tempCol].isOccupied:
						break


			if name == "rook":
				rookMoves()

			elif name == "bishop":
				bishopMoves()

			elif name == "queen":
				rookMoves()
				bishopMoves()

		listOfPossibleMoves = list()
		for cellLoc in listOfLegalMoves:
			if cellLoc == self.loc:
				continue


			possibleCell = currentBoardState.board[cellLoc[0] - 1][cellLoc[1] - 1]
			
			listOfPossibleMoves.append(possibleCell)

			if not possibleCell.isOccupied:
					listOfPossibleMoves.append(possibleCell)
			elif possibleCell.piece.isBlack != self.piece.isBlack:
					listOfPossibleMoves.append(possibleCell)


		return listOfPossibleMoves
