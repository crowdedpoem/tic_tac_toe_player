from enum import IntEnum

class Player(IntEnum):
    Empty = 0
    Maximizer = 1
    Minimizer = -1

    def otherPlayer(self):
        if self == Player.Maximizer:
            return Player.Minimizer
        elif self == Player.Minimizer:
            return Player.Maximizer
        raise ValueError("Empty does not have other player")
        