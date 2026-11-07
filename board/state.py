from enum import IntEnum

class State(IntEnum):
    Empty = 0
    Maximizer = 1
    Minimizer = -1

    @classmethod
    def otherPlayer(cls, player):
        if player == State.Maximizer:
            return State.Minimizer
        elif player == State.Minimizer:
            return State.Maximizer
        raise ValueError("Empty does not have other player")
        