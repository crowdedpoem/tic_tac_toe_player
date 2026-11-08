import pytest

from board.player import Player
from tests.boardCreate import makeBoard


@pytest.mark.parametrize("layout, expected", [
    pytest.param("""
        XXX
        OO.
        ...
    """, Player.Maximizer, id="row-win"),

    pytest.param("""
        O.X
        OX.
        O..
    """, Player.Minimizer, id="column-win"),

    pytest.param("""
        X.O
        .XO
        ..X
    """, Player.Maximizer, id="diagonal-win"),

    pytest.param("""
        XOX
        XOO
        OXX
    """, Player.Empty, id="draw"),

    pytest.param("""
        X..
        .O.
        ...
    """, Player.Empty, id="in-progress"),
])

def test_winner(layout, expected):
    assert makeBoard(layout).terminalValue() == expected