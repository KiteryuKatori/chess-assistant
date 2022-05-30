# Board.py
from Piece import *
from Cell import Cell
from tkinter import *
from tkinter import ttk

class Board:

    mainPanel = Tk()
    frm = ttk.Frame(mainPanel)
    frm.grid()

    currentSelectedCell  = None
    currentSelectedPiece = None
    isSelected           = False
    def __init__(self):

        self.board = list()
        for x in range(8):
            row = list()
            for y in range(8):
                cell = Cell(self, [x + 1, y + 1], [0, 0])
                row.append(cell)

            self.board.append(row)

        self.board[0][0].setPiece(Piece("rook", True), False)
        self.board[0][1].setPiece(Piece("knight", True), False)
        self.board[0][2].setPiece(Piece("bishop", True), False)
        self.board[0][3].setPiece(Piece("queen", True), False)
        self.board[0][4].setPiece(Piece("king", True), False)
        self.board[0][5].setPiece(Piece("bishop", True), False)
        self.board[0][6].setPiece(Piece("knight", True), False)
        self.board[0][7].setPiece(Piece("rook", True), False)      
        self.board[1][0].setPiece(Piece("pawn", True), False)
        self.board[1][1].setPiece(Piece("pawn", True), False)
        self.board[1][2].setPiece(Piece("pawn", True), False)
        self.board[1][3].setPiece(Piece("pawn", True), False)
        self.board[1][4].setPiece(Piece("pawn", True), False)
        self.board[1][5].setPiece(Piece("pawn", True), False)
        self.board[1][6].setPiece(Piece("pawn", True), False)
        self.board[1][7].setPiece(Piece("pawn", True), False)

        self.board[7][0].setPiece(Piece("rook", False), False)
        self.board[7][1].setPiece(Piece("knight", False), False)
        self.board[7][2].setPiece(Piece("bishop", False), False)
        self.board[7][3].setPiece(Piece("king", False), False)
        self.board[7][4].setPiece(Piece("queen", False), False)
        self.board[7][5].setPiece(Piece("bishop", False), False)
        self.board[7][6].setPiece(Piece("knight", False), False)
        self.board[7][7].setPiece(Piece("rook", False), False)     
        self.board[6][0].setPiece(Piece("pawn", False), False)
        self.board[6][1].setPiece(Piece("pawn", False), False)
        self.board[6][2].setPiece(Piece("pawn", False), False)
        self.board[6][3].setPiece(Piece("pawn", False), False)
        self.board[6][4].setPiece(Piece("pawn", False), False)
        self.board[6][5].setPiece(Piece("pawn", False), False)
        self.board[6][6].setPiece(Piece("pawn", False), False)
        self.board[6][7].setPiece(Piece("pawn", False), False)

    def resetBoardColor(self):
        boardCell = self.board
        for row in  boardCell:
            for cell in row:
                cell.resetColor()

    def getBoard(self):
        return self.board

    def visualize(self):
        self.mainPanel.mainloop()
        pass
