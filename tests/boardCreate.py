# test_tictactoe.py
from board.board import Board
from board.square import Square
from board.player import Player # adjust to your API


def makeBoard(s: str) -> Board:
    """Build a board from a visual string. '.' = empty."""
    mapper = {
        'X': Player.Maximizer,
        'O': Player.Minimizer,
        '.': Player.Empty
    }
    board = Board([Square(i) for i in range(9)], 9)
    rows = s.split()

    # print(rows)
    for rowIndex, row in enumerate(rows):
        for colIndex, value in enumerate(row):
            # print('rowIndex: ' + str(rowIndex))
            # print('colIndex: ' + str(colIndex))
            # print('value: ' + str(value))
            val = mapper[value]
            board.select(rowIndex * 3 + colIndex, val)
    return board

