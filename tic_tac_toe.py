from game_base import GameBase


class TicTagToe(GameBase):
    def check_winners(self, puzzle):
        winners = [{0: 0, 1: 1, 2: 2}, {0: 2, 1: 1, 2: 0}]
        player_1 = {}
        player_2 = {}
        vertical_winner = {}
        for index, metric in enumerate(puzzle):
            vertical_winner[index] = metric[0]

            # winner is in line horizontal
            if metric[0] == metric[1] == metric[2]:
                return True, metric[0]
            for index_sub, node in enumerate(metric):
                # winner is in line horizontal
                if puzzle[0][index_sub] == puzzle[1][index_sub] == puzzle[2][index_sub]:
                    return True, metric[0][index_sub]
                if node == 'X':
                    player_1[index] = index_sub
                elif node == 'O':
                    player_2[index] = index_sub

        if player_1 in winners:
            return True, 'X'
        if player_2 in winners:
            return True, 'O'

        return False, None

    def reset_player(self, player_1, player_2, next_player):
        return player_1 if next_player != player_1 else player_2

    def start_game(self):
        print('Welcome to TicTacToe')
        total_choices = 1
        metric_array = [['A', 'B', 'C'], ['D', 'E', 'F'], ['G', 'H', 'I']]
        player_1 = 'X'
        player_2 = 'O'
        next_player = ''
        while total_choices < 10:
            is_winner, who_is_winner = self.check_winners(metric_array)
            if is_winner:
                print(f'Wow, {player_1 if who_is_winner == "X" else player_2} won !!!')
                break

            for array in metric_array:
                printable = ''
                for item in array:
                    printable = printable + f"[ {item} ] "
                print(printable)

            next_player = self.reset_player(player_1, player_2, next_player)
            choice = input(f'Pick a letter to mark {next_player}: ').upper()
            if choice not in ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I']:
                next_player = self.reset_player(player_1, player_2, next_player)
                continue
            for metric in metric_array:
                for node in range(len(metric)):
                    if metric[node] == choice:
                        metric[node] = next_player

            total_choices += 1
