import pytest

from board.state import State
from tests.boardCreate import makeBoard


@pytest.mark.parametrize("layout, expected", [
    pytest.param("""
        XXX
        OO.
        ...
    """, State.Maximizer, id="row-win"),

    pytest.param("""
        O.X
        OX.
        O..
    """, State.Minimizer, id="column-win"),

    pytest.param("""
        X.O
        .XO
        ..X
    """, State.Maximizer, id="diagonal-win"),

    pytest.param("""
        XOX
        XOO
        OXX
    """, State.Empty, id="draw"),

    pytest.param("""
        X..
        .O.
        ...
    """, State.Empty, id="in-progress"),
])

def test_winner(layout, expected):
    assert makeBoard(layout).terminalValue() == expected