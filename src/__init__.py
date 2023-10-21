from board import Board
from game import Game

if __name__ == "__main__":
    board = Board()
    board.create_empty_board()
    print("\033[1;37m\033[1mReady, who starts with the 'BLACK' tile first?\033[0m") 
    print("\033[1;37m\033[1m1. Computer\033[0m") 
    print("\033[1;37m\033[1m2. Human\033[0m") 
    answer = input("\033[1;37m\033[1mEnter answer: \033[0m") 
    answer = int(answer)
    human_starts = True
    if answer == 1:
        human_starts = False

    game = Game(board, human_starts)
    game.play()
