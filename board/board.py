from __future__ import annotations
from board.square import Square
from .player import Player
import copy

class Board:

    def __init__(self, squares: list[Square], emptySquares: int):
        self.squares = squares
        # TODO calculate empty squares within board
        self.emptySquares = emptySquares

    def possibleMoves(self):
        empty = list()
        for square in self.squares:
            if square.value == Player.Empty:
                empty.append(square)
        return empty

    def select(self, index: int, player: Player) -> Board:
        if(self.squares[index].value == Player.Empty and player != Player.Empty):
            self.squares[index].set(player)
            self.emptySquares -= 1
        elif self.squares[index].value != Player.Empty:
            print('BUG TRYING TO WRITE OVER PLAYER')

    def createBoardInstancesForNode(self, index: int, player: Player) -> Board:
        if(self.squares[index].value == Player.Empty and player != Player.Empty):
            newBoardSquares = copy.deepcopy(self.squares)
            newBoardSquares[index].set(player)
            newBoardEmptySquares = self.emptySquares - 1
        elif self.squares[index].value != Player.Empty:
            raise ValueError('BUG TRYING TO WRITE OVER PLAYER')
        return Board(newBoardSquares, newBoardEmptySquares)

    #TODO optimize the 3 of a kind checker. Can do both players at once and less checks
    def setChecker(self, player: Player, start: int, end: int, increment: int) -> bool:
        for i in range(start, end, increment):
            square = self.squares[i].value
            if square != player:
                return False
        return True

    def checkCol(self, player: int, colIndex: int) -> bool:
        return self.setChecker(player, colIndex, 9, 3)

    def checkRow(self, player: Player, rowIndex: int) -> bool:
        return self.setChecker(player, rowIndex * 3, (rowIndex * 3) + 3, 1)

    def checkDiagonal(self, player: Player, downwards: bool) -> bool:
        start = 0
        increment = 4
        if not downwards:
            start = 2
            increment = 2
        return self.setChecker(player, start, 9, increment)
    
    def isWinner(self, player: Player) -> bool:
        # NOTE current: 3 rows, 3 cols, 2 diagonals
        # TODO check the 5 middle squares for wins for both players at once
        for i in range(3):
            if self.checkRow(player, i) or self.checkCol(player, i):
                return True
        return self.checkDiagonal(player, True) or self.checkDiagonal(player, False)

    def isTerminal(self) -> bool:
        if self.isWinner(Player.Maximizer) or self.isWinner(Player.Minimizer):
            print('someone won')
            return True
        if self.emptySquares == 0:
            return True
        return False

    def terminalValue(self) -> int:
        # check if we can still play or check winner
        if self.isWinner(Player.Minimizer):
            return Player.Minimizer.value
        if self.isWinner(Player.Maximizer):
            return Player.Maximizer.value
        if self.emptySquares == 0:
            return 0

    def __str__(self):
        string = ""
        i = 0
        for _ in range(3):
            for _ in range(3):
                string += '%s ' % str(self.squares[i])
                i += 1
            string += '\n'
        return string
