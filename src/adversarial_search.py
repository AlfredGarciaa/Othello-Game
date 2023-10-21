from moves_helper import MoveHelper
from copy import deepcopy
from settings import Settings

class AdversarialSearch:
    computer = None
    beta = None
    alpha = None

    @staticmethod
    def min_max_with_depth(current_player, board, player_enemy, unique_values):
        AdversarialSearch.beta = Settings.highest_value
        AdversarialSearch.alpha = Settings.lowest_value

        AdversarialSearch.computer = deepcopy(current_player)
        p_moves = MoveHelper.get_possible_moves(AdversarialSearch.computer, deepcopy(board))

        if len(p_moves) > 1:
            heuristic_values = []
            for a in deepcopy(unique_values):
                new_board = deepcopy(board)
                new_move = deepcopy(a)
                new_enemy = deepcopy(player_enemy)
                adv_search = AdversarialSearch._max_value(0, new_board, new_move, deepcopy(AdversarialSearch.computer ), new_enemy)
                heuristic_values.append(adv_search)
            return heuristic_values.index(min(heuristic_values)) + 1
        elif len(p_moves) == 1:
            return 1
        else:
            return None

    @staticmethod
    def _min_value(state, board, possible_moves, current_player, player_enemy):
        # print("Board received------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        MoveHelper.apply_move(board, current_player, player_enemy, possible_moves)
        # print("Board final------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        if AdversarialSearch._cut_off(state):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(board, computer, possible_moves)
        v = Settings.highest_value
        p_moves = MoveHelper.get_possible_moves(player_enemy, board)

        actions, _ = MoveHelper.get_unique_final_pos(p_moves)
        for a in actions:
            # print("state"---------------------------------------------")
            copied_enemy = deepcopy(player_enemy)
            copied_current_player = deepcopy(current_player)
            new_board = deepcopy(board)
            new_possible_moves = deepcopy(a)
            v = min(v, AdversarialSearch._max_value(state + 1, new_board, new_possible_moves, copied_enemy, copied_current_player))
            if v <= AdversarialSearch.alpha:
                return v
            AdversarialSearch.beta = min(AdversarialSearch.beta, v)
        return v

    @staticmethod
    def _max_value(state, board, possible_moves, current_player, player_enemy):
        # print("Board received------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        MoveHelper.apply_move(board, current_player, player_enemy, possible_moves)
        # print("Board final------------------------------------------")
        # board.display(0, 0, current_player, player_enemy)

        if AdversarialSearch._cut_off(state):
            computer = current_player if current_player.token == AdversarialSearch.computer.token else player_enemy
            return - AdversarialSearch._eval(board, computer,possible_moves)

        v = Settings.lowest_value
        p_moves = MoveHelper.get_possible_moves(player_enemy, board )

        actions, _ = deepcopy(MoveHelper.get_unique_final_pos(p_moves))

        for a in actions:
            # print("state"---------------------------------------------")
            new_enemy = deepcopy(player_enemy)
            new_c_player = deepcopy(current_player)
            new_board = deepcopy(board)
            new_possible_moves = deepcopy(a)
            v = max(v, AdversarialSearch._min_value(state + 1, new_board, new_possible_moves, new_enemy, new_c_player))
            if v >= AdversarialSearch.beta:
                return v
            AdversarialSearch.alpha = max(AdversarialSearch.alpha, v)
        return v

    @staticmethod
    def _eval(state, computer, possible_moves):
        return Settings.heuristic(state, computer, possible_moves)

    @staticmethod
    def _cut_off(depth):
        return depth == Settings.max_depth
