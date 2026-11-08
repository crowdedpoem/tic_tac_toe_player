from __future__ import annotations
from board.board import Board
from board.square import Square

class Node:

    def __init__(self, move: Square, value: int):
        self.value = value
        self.children = list()
        self.move = move

    def setMove(self, move: Square):
        self.move = move

    def __lt__(self, other):
        return self.value < other.value
    
    def __gt__(self, other):
        return self.value > other.value

    def __eq__(self, other):
        return self.value == other.value

    def __le__(self, other):
        return self.value <= other.value

    def __ge__(self, other):
        return self.value >= other.value

    def __str__(self):
        return f"Node -> value: {str(self.value).ljust(3)}, move: {self.move}"