def solution(n):
    answer = 0
    memo = [1, 2]
    if n > 1:
        for i in range(2, n):
            memo.append((memo[i - 2] + memo[i - 1]) % 1000000007)

    answer = memo[-1]
    return answer