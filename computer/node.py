from __future__ import annotations
from board.board import Board
from board.square import Square

class Node:
    #TODO does node even need board? Can it just be move, value and children?
    def __init__(self, board: Board, value: int, children: list[Node]):
        self.board = board
        self.value = value
        self.children = children
        self.move = None

    def setParent(self, parent):
        self.parent = parent

    def setMove(self, move: Square):
        self.move = move

    def addChild(self, child):
        self.children.append(child)

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