N = int(input())
memo = [0, 1]

for i in range(2, N + 1):
    min_v = 1e9
    j = 1

    while (j ** 2) <= i:
        min_v = min(min_v, memo[i - (j ** 2)])
        j += 1

    memo.append(min_v + 1)

print(memo[N])