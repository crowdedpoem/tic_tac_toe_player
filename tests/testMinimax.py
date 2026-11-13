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
        ...
        ...
        ...
    """, Player.Minimizer, Player.Empty, Square(4), id='play-middle-for-best-chance'),

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
# we are not valuing winning quicker, leads to unexpected results
    pytest.param("""
        .OO
        .XX
        ...
    """, Player.Maximizer, Player.Maximizer, Square(0), id="diagonal-win"),
    # square is 1 because the program knows a draw is inevitable and just picks the first option
    pytest.param("""
        X..
        .O.
        ...
    """, Player.Maximizer, Player.Empty, Square(1), id="in-progress"), 
])

def test_minimax(layout, assignedValue, expected, move):
    board = makeBoard(layout)
    computer = Computer(assignedValue)
    bestState = computer.play(board)
    # print('printing what beststate value is ' + str(bestState))
    assert bestState.value == expected
    assert bestState.move.index == move.index