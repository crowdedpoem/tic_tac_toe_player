from board.board import Board
from board.square import Square
from computer.minimax import Minimax
from computer.node import Node

class Computer:

    def __init__(self, player):
        self.player = player

    def play(self, board: Board) -> Node:
        mmTree = Minimax()
        topNode = mmTree.buildTree(self.player, board, -1000, 1000)
        print('trying to show children at top level')
        mmTree.printChildren([topNode])
        return topNode