from computer.child import Child
from computer.node import Node
from board.state import State


class Minimax:
    def __init__(self):
        self.iter = 0

    def buildTree(self, currPlayer, currBoard):
        self.iter += 1
        if currBoard.isTerminal():
            return Node(currBoard, currBoard.terminalValue(), None)
        # branch 
        # if(currPlayer == State.Maximizer):
            # children should be a 2D list with [[move, Node] ...]
        
        children = self.iterThroughChildren(currBoard, currPlayer)
        best = self.bestChild(children, currPlayer)
        print('iter is ' + str(self.iter))
        return Node(best.board, best.value, children)
        
        
    def iterThroughChildren(self, currBoard, currPlayer):
        li = []
        exploreMoves = currBoard.possibleMoves()
        print('exploring these moves ' + str(exploreMoves))
        for move in exploreMoves:
            print('move is ' + str(move))
            print('player is ' + str(currPlayer))
            newBoard = currBoard.select(move.index, currPlayer)
            print('newBoard is ' + str(newBoard))
            li.append(
                Child(
                    move, 
                    self.buildTree(
                        State.otherPlayer(currPlayer), newBoard
                    )
                )
            )
        return li

    def bestChild(self, children, currPlayer):
        # TODO make a child object with (move, Node)
        bestDiff = abs(children[0].node.value - currPlayer.value)
        best = children[0].node
        for index, child in enumerate(children):
            diff = abs(child.node.value - currPlayer.value)
            if diff < bestDiff:
                bestDiff = diff
                best = children[index]
        return best


    def printTree(self, node):
        print('node: ' + str(node))
        for child in node.children:
            self.printTree(child)