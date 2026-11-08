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

    def getMoveFromBestBoard(self, currBoard: Board, bestBoard: Board) -> Square:
        # find the difference between the best and current board, that is ideal move
        diff = currBoard.getDiffFromBoards(bestBoard)
        if len(diff) != 1 or diff[0].value != self.player:
            raise ValueError("Best board has unexpected value:\n" + str(bestBoard))
        return diff[0] 
