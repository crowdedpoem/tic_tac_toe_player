
# Press the green button in the gutter to run the script.
from board.board import Board
from computer.computer import Computer
from board.player import Player


if __name__ == '__main__':
    b = Board()
    c = Computer(Player.Maximizer)
    print(c.play(b))
