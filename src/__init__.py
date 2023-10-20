from board import Board
from game import Game

if __name__ == "__main__":
    board = Board()
    board.create_empty_board()
    print("Ready, who starts first?")
    print("1. Computer")
    print("2. Human")
    print("Enter answer: ")
    answer = int(input())
    human_starts = True
    if answer == 1:
        human_starts = False

    game = Game(board, human_starts)
    game.play()
