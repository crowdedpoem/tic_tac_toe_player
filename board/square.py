
from math import floor

from board.player import Player


class Square:

    def __init__(self, index: int):
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.value = Player.Empty

    def set(self, value) -> None:
        if(self.isAvailable()):
            self.value = value

    def isAvailable(self) -> bool:
        return self.value == Player.Empty

    def __str__(self):
        return ('[index: %d state: %s]' % (self.index, str(self.value).ljust(2)))

    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        if self.index == other.index and self.value == other.value:
            return True
        return False