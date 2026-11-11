from __future__ import annotations
from board.board import Board
from board.square import Square

class Node:

    def __init__(self, value: int):
        self.value = value
        self.move = None
        self.children = list()

    def setMove(self, move: Square):
        self.move = move

    def addChildren(self, children: list[Node]):
        self.children = children

    def __str__(self):
        return f"N(move: {self.move.index}, expected: {str(self.value).ljust(2)})"