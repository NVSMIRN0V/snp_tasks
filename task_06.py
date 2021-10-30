class WrongNumberOfPlayersError(Exception):
    '''Класс исключения при обработке количества игроков'''

    def __init__(self):
        self.message = 'Число игроков не соответствует правилам игры.'

    def __str__(self):
        return f'WrongNumberOfPlayersError: {self.message}'


class NoSuchStrategyError(Exception):
    '''Класс исключения при обработке выбора игроков'''

    def __init__(self, *args):
        self.message = args[0] if args else None

    def __str__(self):
        return f'NoSuchStrategyError: {self.message}'


def rps_game_winner(play_list):
    decisions = ['R', 'P', 'S']
    player_1, player_2 = play_list[0][0], play_list[1][0]
    decision_player_1, decision_player_2 = play_list[0][1], play_list[1][1]
    try:
        if len(play_list) != 2:
            raise WrongNumberOfPlayersError()
        elif not decision_player_1 in decisions or not decision_player_2 in decisions:
            raise NoSuchStrategyError('Убедитесь в корректности выбора игрока.')
    except WrongNumberOfPlayersError as error:
        print(error)
    except NoSuchStrategyError as error:
        print(error)
    else:
        determine_the_winner(player_1, player_2, decision_player_1, decision_player_2)


def determine_the_winner(player_1, player_2, decision_player_1, decision_player_2):
    if (decision_player_1 == 'R' and decision_player_2 == 'S') \
        or (decision_player_1 == 'P' and decision_player_2 == 'R') \
            or (decision_player_1 == 'S' and decision_player_2 == 'P'):
        print(player_1, decision_player_1)  # play_list[0] ?
    elif (decision_player_1 == 'S' and decision_player_2 == 'R') \
        or (decision_player_1 == 'R' and decision_player_2 == 'P') \
            or (decision_player_1 == 'P' and decision_player_2 == 'S'):
        print(player_2, decision_player_2)  # play_list[1] ?
    else:
        print(player_1, decision_player_1)
