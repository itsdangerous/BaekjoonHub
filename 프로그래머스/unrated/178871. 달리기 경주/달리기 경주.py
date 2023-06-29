def solution(players, callings):
    player_dict = {name: index for index, name in enumerate(players)}
    for name in callings:
        index = player_dict[name]
        players[index - 1], players[index] = players[index], players[index - 1]
        player_dict[players[index - 1]] = index - 1
        player_dict[players[index]] = index
    return players
