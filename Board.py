# Board.py
from xmlrpc.client import FastMarshaller
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


        pieceList = ["rook", "knight", "bishop", "pawn", "queen", "king"]
        #Kings always stays on the E Collumn
        for i in range(2):
            self.board[0][3 + i].setPiece(Piece(pieceList[4 + i], True), False)
            self.board[7][3 + i].setPiece(Piece(pieceList[4 + i], False), False)

        for i in range(3):
            self.board[0][i].setPiece(Piece(pieceList[i], True), False)
            self.board[0][7-i].setPiece(Piece(pieceList[i], True), False)
            self.board[7][i].setPiece(Piece(pieceList[i], False), False)
            self.board[7][7-i].setPiece(Piece(pieceList[i], False), False)

        for i in range(8):
            self.board[1][i].setPiece(Piece(pieceList[3], True), False)
            self.board[6][7-i].setPiece(Piece(pieceList[3], False), False) 


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
