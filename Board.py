# Board.py
from Piece import *
from Cell import Cell
from tkinter import *
from tkinter import ttk
import copy
import random

class BoardAI:
    historyBoards = list()

    #Lists(to prevent re-declaration over and over again to preserve memory)

    def __init__(self):
        self.board = list()
        self.isBlackTurn = None

    def updateHistory(self):
        self.historyBoards.append(self)

    def printBoardWPieceTerminal(self) -> None:

        BOARD_SIDE = range(8)
        print('   ' + '   '.join([str(col_num) for col_num in BOARD_SIDE]) )
        row_num = 0
        for row in self.board:
            print(' ' + ' ---' * 8) 
            print(str(row_num) + '', end='')
            for cell in row:
                if cell.isOccupied == False:
                    print('|   ', end='')
                else:
                    print(f'| {cell.piece.getImage()} ', end='')
            print('|')
            row_num += 1
        print('  ' + ' ---' * 8) 
        print()

    def moveAI(self, oldLoc, newLoc, optionPromotion=None):
        oldCell = self.board[oldLoc[0]][oldLoc[1]]
        newCell = self.board[newLoc[0]][newLoc[1]]

        newCell.type = oldCell.isSpecialMove(newCell)
        newCell.setPiece(oldCell.piece)
        oldCell.removePiece()

        if newCell.type > 0:
            if newCell.type == 3:
                newCell.doSpecialMove(self, optionPromotion)
            else:
                newCell.doSpecialMove(self)


    def getScore(self):
        totalScoreWhite = 0
        totalScoreBlack = 0
        pawnMultiplier = [1, 1.1, 1.3, 1.8, 2.1, 2.6, 3.3]


        for row in self.board:
            for cell in row:
                if not cell.isOccupied:
                    continue
                if cell.piece.isBlack: 
                    if cell.piece.name == "pawn":
                        totalScoreBlack += cell.piece.SCORE * pawnMultiplier[cell.loc[0] - 2] #Black -> increasing index
                        # [might need this] print(f"This {cell.piece.name} is currently at {cell.loc[0]}-{cell.loc[1]} and have a score of {cell.piece.SCORE * pawnMultiplier[cell.loc[0] - 2]}")
                    else:
                        totalScoreBlack += cell.piece.SCORE
                else:
                    if cell.piece.name == "pawn":
                        totalScoreWhite += cell.piece.SCORE * pawnMultiplier[7 - cell.loc[0]] #White -> decreasing index
                    else:
                        totalScoreWhite += cell.piece.SCORE

        return (totalScoreBlack - totalScoreWhite) / totalScoreBlack

class Board(BoardAI):

    mainPanel = Tk()

    def __init__(self):
        self.frm = ttk.Frame(self.mainPanel)
        self.frm.grid()
        self.board = list()
        self.isSelected = False
        self.previousSelectedCell  = None
        self.currentSelectedPiece = None
        self.isBlackTurn = False
        
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

    def resetEnPasse(self):
        boardCell = self.board
        for row in  boardCell:
            for cell in row:
                if cell.isOccupied:
                    cell.piece.isEdibleEnPasse = False

    def getBoard(self):
        return self.board

    def visualize(self):
        self.mainPanel.mainloop()
        pass

    def moveGUI(self, oldLoc, newLoc, optionPromotion=None):

        oldCell = self.board[oldLoc[0]][oldLoc[1]]
        newCell = self.board[newLoc[0]][newLoc[1]]
        
        oldCell.click()
        newCell.click(optionPromotion)

    def saveState(self):

        newBoardState = self.copy()
        newBoardState.updateHistory()

    def freeze(self):
        for row in self.board:
            for cell in row:
                cell.button['state'] = "disabled"

    def release(self):
        for row in self.board:
            for cell in row:
                cell.button['state'] = "normal"

    def printBoardWPieceTerminal(self) -> None:

        
        BOARD_SIDE = range(8)
        print('   ' + '   '.join([str(col_num) for col_num in BOARD_SIDE]) )
        row_num = 0
        for row in self.board:
            print(' ' + ' ---' * 8) 
            print(str(row_num) + '', end='')
            for cell in row:
                if cell.isOccupied == False:
                    print('|   ', end='')
                else:
                    print(f'| {cell.piece.getImage()} ', end='')
            print('|')
            row_num += 1
        print('  ' + ' ---' * 8) 
        print()

    def copy(self):
        """
        return: BoardAI Object
        """
        boardAI = BoardAI()
        boardAI.isBlackTurn = self.isBlackTurn
        for row in self.board:
            newRow = list()
            for cell in row:
                newRow.append(cell.copy())
            boardAI.board.append(newRow)

        return boardAI

    def MakesRanDomMove(self, currState):

        rawBoardState = currState.copy()

        listOfInputForMoves = []
        for i, row in enumerate(rawBoardState.board):
            for j, cell in enumerate(row):
                if (cell.isOccupied) and \
                   (cell.piece.isBlack == True):
                    oldLoc = [i, j] #-> all Loc -1
                    listOfMoveableCell = cell.showPossibleMoves(rawBoardState)
                    for newCell in listOfMoveableCell:
                        newLoc = [newCell.loc[0] - 1 , newCell.loc[1] - 1]
                        listOfInputForMoves.append([oldLoc, newLoc])

        successor = list()
        for eachSuggestion in listOfInputForMoves:
            copiedVersion = copy.deepcopy(rawBoardState)
            oldLoc = eachSuggestion[0]
            newLoc = eachSuggestion[1]
            # check if the is promotion move
            if rawBoardState.board[oldLoc[0]][oldLoc[1]]\
                .isSpecialMove(rawBoardState.board[newLoc[0]][newLoc[1]]) == 3:
                # version for Knight
                copiedVersion.moveAI(oldLoc, newLoc, 0)
                successor.append([eachSuggestion, copiedVersion.getScore(), 0])
                # version for Queen
                copiedVersion2 = copy.deepcopy(rawBoardState)
                copiedVersion2.moveAI(oldLoc, newLoc, 3)
                successor.append([eachSuggestion, copiedVersion2.getScore(), 3])
                continue
            copiedVersion.moveAI(oldLoc, newLoc)
            
            successor.append([eachSuggestion, copiedVersion.getScore(), None])

        successor.sort(key = lambda x: x[1], reverse = True)
        optimalScore = successor[0][1]
        listOfEqualMoves = [s for s in successor if s[1] == optimalScore]
        return random.choice(listOfEqualMoves)