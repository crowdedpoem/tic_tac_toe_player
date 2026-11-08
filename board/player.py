from enum import IntEnum

class Player(IntEnum):
    Empty = 0
    Maximizer = 1
    Minimizer = -1

    @classmethod
    def otherPlayer(cls, player):
        if player == Player.Maximizer:
            return Player.Minimizer
        elif player == Player.Minimizer:
            return Player.Maximizer
        raise ValueError("Empty does not have other player")
        