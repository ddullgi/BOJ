N = int(input())
memo = [0, 0]
for i in range(2, N+1):
    if i % 6 == 0:
        if memo[i//3] > memo[i-1] and memo[i//2] > memo[i-1]:
            memo += [memo[i - 1] + 1]
        elif memo[i//3] > memo[i//2] and memo[i-1] > memo[i//2]:
            memo += [memo[i // 2] + 1]
        else:
            memo += [memo[i//3] + 1]
    elif i % 3 == 0:
        if memo[i//3] > memo[i-1]:
            memo += [memo[i - 1] + 1]
        else:
            memo += [memo[i//3] + 1]
    elif i % 2 == 0:
        if memo[i//2] > memo[i-1]:
            memo += [memo[i - 1] + 1]
        else:
            memo += [memo[i//2] + 1]
    else:
        memo += [memo[i-1] + 1]

print(memo[N])