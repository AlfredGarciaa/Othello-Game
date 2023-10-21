import numpy as np
from heuristiFunctionCollection import HeuristicFunctionCollection

class Settings:
    p1_token = 'o'
    p2_token = '0'
    new_option_token = "."
    empty_token = '_'
    min = "min"
    max = "max"
    lowest_value = - np.inf
    highest_value = np.inf
    max_depth = 4
    heuristic = HeuristicFunctionCollection().movility_strategy
    token_color = "\033[0;37m"  # white
    p1_color ="\033[1;37m"  # bold white
    p2_color = "\033[1;30m"  # bold black
    empty_token_color = "\033[1;32m"  # bold green
    new_option_color = "\033[1;35m"  # bold purple
    index_color = "\033[1;34m\033[1m"  # blue with bold
    letters_color = "\033[0;33m"  # dark yellow / brown
    board_size = 8
    letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H']
    actions = ["UP", "UP-RIGHT", "RIGHT", "DOWN-RIGHT", "DOWN", "LEFT-DOWN", "LEFT", "LEFT-UP"]
