n = int(input())
arr = [[0, 0]]

for _ in range(n - 1):
    small, big = map(int, input().split())
    arr.append([small, big])

k = int(input())
d = [0] * (n + 1)
d[0] = 0
        
if n == 1:
    print(0)
elif n == 2:
    print(arr[1][0])
else:
    d[1] = arr[1][0]
    d[2] = min(d[1] + arr[2][0], arr[1][1])

    for i in range(3, n):
        d[i] = min(d[i - 1] + arr[i][0], d[i - 2] + arr[i-1][1])
	
    result = d[n-1]
    
    for i in range(3,n):
        dp = d[:]
        dp[i] = d[i-3] + k
        
        for j in range(i+1,n):
            dp[j] = min(dp[j - 1] + arr[j][0], dp[j - 2] + arr[j-1][1])
		
        if result > dp[n-1]:
            result = dp[n-1]
    print(result)