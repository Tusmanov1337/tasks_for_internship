class WrongNumberOfPlayersError(Exception):
    pass


class NoSuchStrategyError(Exception):
    pass


def rps_game_winner(players_info = None):
    if players_info is None or not players_info or not players_info[0] or len(players_info) > 2:
        raise WrongNumberOfPlayersError
    elif len(players_info) == 1:
        return ' '.join(players_info[0])
    Strategies = Strategies = {'RR': players_info[0],
                               'RS': players_info[0],
                               'RP': players_info[1],
                               'PP': players_info[0],
                               'PS': players_info[1],
                               'PR': players_info[0],
                               'SS': players_info[0],
                               'SP': players_info[0],
                               'SR': players_info[1], }

    if not (players_info[0][1] in 'RSP') or not (players_info[1][1] in 'RSP'):
        raise NoSuchStrategyError

    return ' '.join(Strategies[players_info[0][1] + players_info[1][1]])

