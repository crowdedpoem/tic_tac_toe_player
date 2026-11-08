from board.board import Board
from computer.node import Node
from board.player import Player


class Minimax:
    def __init__(self):
        self.iter = 0

    def buildTree(self, currPlayer: Player, currBoard: Player) -> Node:
        self.iter += 1
        if currBoard.isTerminal():
            return Node(currBoard.terminalValue())
        
        children = self.iterThroughChildren(currBoard, currPlayer)
        print('iter is ' + str(self.iter))
        return self.bestChild(children, currPlayer)
        

    #TODO add alpha beta pruning here
    def iterThroughChildren(self, currBoard: Board, currPlayer: Player) -> list[Node]:
        li = []
        exploreMoves = currBoard.possibleMoves()
        print('exploring ' + str(len(exploreMoves)) + ' moves')
        for square in exploreMoves:
            print('move is ' + str(square))
            newBoard = currBoard.createBoardInstancesForNode(square.index, currPlayer)
            print('newBoard is:\n' + str(newBoard))
            childNode = self.buildTree(currPlayer.otherPlayer(), newBoard)
            childNode.setMove(square)
            print(f"this is child node: {str(childNode)}")
            li.append(childNode)
        return li

    def bestChild(self, children: list[Node], currPlayer: Player) -> Node:
        bestDiff = 100
        best = None
        for child in children:
            diff = abs(child.value - currPlayer.value)
            if diff < bestDiff:
                bestDiff = diff
                best = child
        return best


    def printTree(self, node):
        print('node: ' + str(node))
        for child in node.children:
            self.printTree(child)