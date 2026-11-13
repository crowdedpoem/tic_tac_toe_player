from board.board import Board
from computer.node import Node
from board.player import Player


class Minimax:
    def __init__(self):
        
        self.iter = 0

    def buildTree(self, currPlayer: Player, currBoard: Board, alpha: int, beta: int) -> Node:
        if currBoard.isTerminal():
            self.iter += 1
            return Node(currBoard.terminalValue())
        
        children = self.iterThroughChildren(currBoard, currPlayer, alpha, beta)
        return self.bestChild(children, currPlayer)

    def iterThroughChildren(self, currBoard: Board, currPlayer: Player, alpha: int, beta: int) -> list[Node]:
        li = []
        exploreMoves = currBoard.possibleMoves()
        for square in exploreMoves:
            newBoard = currBoard.createBoardInstancesForNode(square.index, currPlayer)
            childNode = self.buildTree(currPlayer.otherPlayer(), newBoard, alpha, beta)
            childNode.setMove(square)
            li.append(childNode)
            # potentially break, iter is 457
            childVal = childNode.value
            if currPlayer.isMaximizer():
                alpha = max(alpha, childVal)
            else:
                beta = min(beta, childVal)

            if alpha >= beta:
                print(f'beta {beta} less than child value {childVal}, quit. Move: '+ str(childNode.move) + ' curr player:' + str(currPlayer) +  '\n' + str(newBoard))
                # self.printChildren(li)
                return li
       # self.printChildren(li)
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
        print('node children ' + str(len(node.children)))
        for child in node.children:
            self.printTree(child)


    def printChildren(self, liNodes: list[Node]):
        if len(liNodes) == 0:
            return
        node = liNodes.pop(0)
        print('\nroot node: ' + str(node))
        li = node.children
        print('children length: ' + str(len(li)))
        for child in li:
            print(child)
            if child != node:
                liNodes.append(child)
        self.printChildren(liNodes)