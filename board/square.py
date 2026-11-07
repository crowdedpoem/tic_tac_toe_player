
from math import floor

from board.state import State


class Square:

    def __init__(self, index):
        self.index = index
        self.x = index % 3
        self.y = floor(index / 3)
        self.value = State.Empty

    def set(self, value):
        if(self.isAvailable()):
            self.value = value

    def isAvailable(self):
        return self.value == State.Empty

    def __str__(self):
        return ('|x: %d y: %d state: %s|' % (self.x, self.y, str(self.value).ljust(10)))

    def __repr__(self):
        return str(self)
