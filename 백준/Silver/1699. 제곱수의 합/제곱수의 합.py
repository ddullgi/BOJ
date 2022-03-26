N = int(input())

memo = [0] + [-1] * N
square = [i * i for i in range(316, 0, -1)]

def dp(n):
    arr = []
    for i in square:
        if i > n:
            continue
        k = n - i
        if memo[k] != -1:
            arr.append(1 + memo[k])
        else:
            arr.append(1 + dp(k))
    memo[n] = min(arr)
    return memo[n]

dp(N)
print(memo[N])