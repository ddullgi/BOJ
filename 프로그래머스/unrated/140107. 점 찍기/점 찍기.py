def solution(k, d):
    answer = 0
    for x in range(0, d + 1, k):
        yl = (d ** 2 - x ** 2) ** 0.5
        y = yl // k
        answer += 1 + y
    return answer