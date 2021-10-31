class WrongNumberOfPlayersError(Exception):
    '''Класс исключения при обработке количества игроков'''
    pass


class NoSuchStrategyError(Exception):
    '''Класс исключения при обработке выбора игроков'''
    pass


def rps_game_winner(play_list):
    decisions = ['R', 'P', 'S']
    player_1, player_2 = play_list[0][0], play_list[1][0]
    decision_player_1, decision_player_2 = play_list[0][1], play_list[1][1]

    if len(play_list) != 2:
        raise WrongNumberOfPlayersError('Количество игроков не соответствует правилам игры.')
    elif not decision_player_1 in decisions or not decision_player_2 in decisions:
        raise NoSuchStrategyError('Убедитесь в корректности выбора игрока.')
    else:
       return determine_the_winner(player_1, player_2, decision_player_1, decision_player_2)


def determine_the_winner(player_1, player_2, decision_player_1, decision_player_2):
    winner = ''
    if (decision_player_1 == 'R' and decision_player_2 == 'S') \
        or (decision_player_1 == 'P' and decision_player_2 == 'R') \
            or (decision_player_1 == 'S' and decision_player_2 == 'P'):
        winner += player_1 + ' ' + decision_player_1
    elif (decision_player_1 == 'S' and decision_player_2 == 'R') \
        or (decision_player_1 == 'R' and decision_player_2 == 'P') \
            or (decision_player_1 == 'P' and decision_player_2 == 'S'):
        winner += player_2 + ' ' + decision_player_2
    else:
        winner += player_1 + ' ' + decision_player_1

    return winner
