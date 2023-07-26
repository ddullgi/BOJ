def solution(x, y, z):
    comb = ((9, 3, 1), (9, 1, 3), (3, 9, 1), (3, 1, 9), (1, 9, 3), (1, 3, 9))
    x = 0 if x <= 0 else x
    y = 0 if y <= 0 else y
    z = 0 if z <= 0 else z

    if (x, y, z) == (0, 0, 0):
        return 0

    if dp[x][y][z]:
        return dp[x][y][z]

    dp[x][y][z] = 1 + min([solution(x - i, y - j, z - k) for i, j, k in comb])

    return dp[x][y][z]

N = int(input())
arr = list(map(int, input().split()))
while len(arr) < 3:
    arr += [0]

dp = [[[0] * (max(arr) + 1) for _ in range(max(arr) + 1)] for _ in range(max(arr) + 1)]

print(solution(arr[0], arr[1], arr[2]))