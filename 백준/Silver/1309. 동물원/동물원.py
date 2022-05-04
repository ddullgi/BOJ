DP = [(0, 0), (2, 1)]
N = int(input())
for i in range(2, N+1):
    A, B = DP[i-1]
    DP.append(((A+B*2)%9901, (A+B)%9901))

print(sum(DP[N])%9901)