def solution(name, yearning, photo):
    answer = []
    scores = {}
    rng = len(name)

    for i in range(rng) :
        scores[name[i]] = yearning[i]
        
    for p in photo :
        ans = 0
        for person in p :
            if person not in name :
                continue
            ans += scores[person]
        answer.append(ans)

    return answer