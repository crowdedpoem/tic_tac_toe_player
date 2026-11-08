from board.board import Board
from computer.node import Node
from board.player import Player


class Minimax:
    def __init__(self):
        self.iter = 0

    def buildTree(self, currPlayer: Player, currBoard: Player) -> Node:
        self.iter += 1
        if currBoard.isTerminal():
            return Node(None, currBoard.terminalValue())
        
        children = self.iterThroughChildren(currBoard, currPlayer)
        best = self.bestChild(children, currPlayer)
        print('iter is ' + str(self.iter))
        return Node(best.move, best.value)
        

    #TODO add alpha beta pruning here
    def iterThroughChildren(self, currBoard: Board, currPlayer: Player) -> list[Node]:
        li = []
        exploreMoves = currBoard.possibleMoves()
        print('exploring ' + str(len(exploreMoves)) + ' moves')
        for square in exploreMoves:
            print('move is ' + str(square))
            newBoard = currBoard.createBoardInstancesForNode(square.index, currPlayer)
            print('newBoard is:\n' + str(newBoard))
            childNode = self.buildTree(Player.otherPlayer(currPlayer), newBoard)
            childNode.setMove(square)
            print(f"this is child node: {str(childNode)}")
            li.append(childNode)
            # already found a winning move 
            if childNode.value == currPlayer.value:
                break
        return li

    def bestChild(self, children: list[Node], currPlayer: Player) -> Node:
        # TODO make a child object with (Square, Node)
        bestDiff = abs(children[0].value - currPlayer.value)
        best = children[0]
        for index, child in enumerate(children):
            diff = abs(child.value - currPlayer.value)
            if diff < bestDiff:
                bestDiff = diff
                best = children[index]
        return best


    def printTree(self, node):
        print('node: ' + str(node))
        for child in node.children:
            self.printTree(child)