from board.square import Square
from .state import State

class Board:

    def __init__(self, squares, emptySquares):
        self.squares = squares
        self.emptySquares = emptySquares

    def possibleMoves(self):
        empty = list()
        for square in self.squares:
            if square.value == State.Empty:
                empty.append(square)
        return empty

    def select(self, index, player):
        print('select player is: ' + str(player))
        print('index is ' + str(index))
        if(self.squares[index].value == State.Empty and player != State.Empty):
            print('select is setting state: ' + str(player))
            self.squares[index].set(player)
            self.emptySquares -= 1
            print('after select, num empty squares: ' + str(self.emptySquares))
        else:
            print('did not select anything')
        return Board(self.squares, self.emptySquares)

    def setChecker(self, player, start, end, increment):
        for i in range(start, end, increment):
            square = self.squares[i].value
            if square != player:
                return False
        return True

    def checkCol(self, player, colIndex):
        return self.setChecker(player, colIndex, 9, 3)

    def checkRow(self, player, rowIndex):
        return self.setChecker(player, rowIndex * 3, (rowIndex * 3) + 3, 1)

    def checkDiagonal(self, player, downwards):
        start = 0
        increment = 4
        if not downwards:
            start = 2
            increment = 2
        return self.setChecker(player, start, 9, increment)
    
    def isWinner(self, player):
        # NOTE current: 3 rows, 3 cols, 2 diagonals
        for i in range(3):
            if self.checkRow(player, i) or self.checkCol(player, i):
                return True
        return self.checkDiagonal(player, True) or self.checkDiagonal(player, False)

    def isTerminal(self):
        if self.isWinner(State.Maximizer) or self.isWinner(State.Minimizer):
            print('someone won')
            return True
        if self.emptySquares == 0:
            return True
        return False

    def terminalValue(self):
        # check if we can still play or check winner
        if self.isWinner(State.Minimizer):
            return State.Minimizer.value
        if self.isWinner(State.Maximizer):
            return State.Maximizer.value
        if self.emptySquares == 0:
            return 0

    def __str__(self):
        string = ""
        i = 0
        for _ in range(3):
            for _ in range(3):
                print(i)
                string += '%s ' % str(self.squares[i])
                i += 1
            string += '\n'
        return string
