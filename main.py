# main.py

from Board import *
from Cell import *
from Piece import *

# board = Board()
if __name__ == "__main__":
	board = Board()
	board.visualize()

	boardState = board.copy()

	for state in boardState.historyBoards:
		state.printBoardWPieceTerminal()

