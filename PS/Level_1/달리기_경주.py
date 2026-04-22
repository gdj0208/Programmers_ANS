
def solution(players, callings):
    answer = []
    runners = {player : i for i, player in enumerate(players)}

    for call in callings :
        p_idx = runners[call]
        front_player = players[p_idx-1]
        players[p_idx-1], players[p_idx] =players[p_idx], players[p_idx-1]

        runners[call] -= 1
        runners[front_player] += 1
    answer = players

    return answer

players = ["mumu", "soe", "poe", "kai", "mine"]
callings = ["kai", "kai", "mine", "mine"]
print(solution(players, callings))