def solution(players, callings):
    answer = []
    l = len(players)
    player = {string : i for i,string in enumerate(players)}
    for name in callings:
        pre, idx = player[name] - 1, player[name]
        players[pre], players[idx] = players[idx] , players[pre]
        player[players[pre]] , player[players[idx]] = player[players[pre]] - 1 , player[players[idx]] + 1

    return players