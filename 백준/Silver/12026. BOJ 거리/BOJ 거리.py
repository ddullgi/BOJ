n = int(input())
block = input()
dp = [0xffffff] * n
dp[0] = 0

for i in range(n):    
    for j in range(i + 1, n):
            if dp[i] == -1:
                continue
            
            if block[i] == 'B' and block[j] == 'O':
                dp[j] = min(dp[i] + (j - i) ** 2, dp[j])
            
            if block[i] == 'O' and block[j] == 'J':
                dp[j] = min(dp[i] + (j - i) ** 2, dp[j])

            if block[i] == 'J' and block[j] == 'B':
                dp[j] = min(dp[i] + (j - i) ** 2, dp[j])

if dp[n-1] == 0xffffff:
    print(-1)
else:
    print(dp[n-1])