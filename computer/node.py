class Node:
    def __init__(self, board, value, children):
        self.board = board
        self.value = value
        self.children = children

    def setParent(self, parent):
        self.parent = parent

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
    