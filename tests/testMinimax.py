import pytest

from board.state import State
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
    """, State.Maximizer, State.Maximizer, 2, id="max-win-top-right"),

    # pytest.param("""
    #     O.X
    #     OX.
    #     O..
    # """, State.Minimizer, id="column-win"),

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
    print('printing what beststate value is ' + str(bestState.value))
    assert bestState.value == expected
    # skip for now on what the best move is
    # assert bestState.move == 