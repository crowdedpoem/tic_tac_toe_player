from board.board import Board
from board.square import Square
from computer.minimax import Minimax
from computer.node import Node

class Computer:

    def __init__(self, player):
        self.player = player

    def play(self, board: Board) -> Node:
        mmTree = Minimax()
        return mmTree.buildTree(self.player, board)