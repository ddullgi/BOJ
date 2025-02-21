def solution(t, p):
    answer = 0

    for idx in range(0, len(t) - len(p) + 1):
        num = t[idx:idx + len(p)]
        if num <= p:
            answer += 1

    return answer