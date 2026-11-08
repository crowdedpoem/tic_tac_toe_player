import pytest

from board.player import Player
from board.square import Square
from computer.computer import Computer
from tests.boardCreate import makeBoard

# input:
# - board
# - who it is: min or max
# computer needs to find: 
# - correct score
# - correct move

@pytest.mark.parametrize("layout, assignedValue, expected, move", [
    pytest.param("""
        XX.
        OO.
        ...
    """, Player.Maximizer, Player.Maximizer, Square(2), id="max-win-top-right"),

     pytest.param("""
         O.X
         O..
         X..
     """, Player.Minimizer, Player.Minimizer, Square(4), id="column-win"),

    # pytest.param("""
    #     X.O
    #     .XO
    #     ..X
    # """, State.Maximizer, id="diagonal-win"),

    # pytest.param("""
    #     XOX
    #     XOO
    #     OXX
    # """, State.Empty, id="draw"),

    # pytest.param("""
    #     X..
    #     .O.
    #     ...
    # """, State.Empty, id="in-progress"),
])

def test_minimax(layout, assignedValue, expected, move):
    board = makeBoard(layout)
    computer = Computer(assignedValue)
    bestState = computer.play(board)
    print('printing what beststate value is ' + str(bestState))
    assert bestState.value == expected
    # skip for now on what the best square is
   # bestMove = computer.getMoveFromBestBoard(board, bestState.board)
   # assert bestState.move.index == move.index