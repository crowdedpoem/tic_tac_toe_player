from __future__ import annotations
from board.board import Board
from board.square import Square

class Node:

    def __init__(self, value: int):
        self.value = value
        self.move = None

    def setMove(self, move: Square):
        self.move = move

    def __str__(self):
        return f"Node -> value: {str(self.value).ljust(3)}, move: {self.move}"