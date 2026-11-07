from board.board import Board
from board.state import State
from computer.minimax import Minimax

class Computer:

    def __init__(self, player):
        self.player = player

    def play(self, board):
        mmTree = Minimax()
        return mmTree.buildTree(self.player, board)

