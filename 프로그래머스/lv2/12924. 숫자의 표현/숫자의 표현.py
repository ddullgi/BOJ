def solution(n):
    answer = 0
    i = 1

    while (i * (i - 1) / 2) < n:
        if (n - i * (i - 1) / 2) % i == 0:
            answer += 1
        i += 1
    return answer