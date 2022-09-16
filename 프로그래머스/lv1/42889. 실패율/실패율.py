def solution(N, stages):
    dict = {}
    for i in range(N):
        cur = 0
        tot = 0
        for j in stages:
            if j >= i + 1:
                tot += 1
                if j == i + 1:
                    cur += 1
        if tot == 0:
            dict[i + 1] = 0
        else:
            dict[i + 1] = cur/tot
    answer = [x[0] for x in sorted(dict.items(), key = lambda x: x[1], reverse=True)]
    return answer