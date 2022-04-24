def LCS(a, b):
    global memo, maxL
    if a*b == 0:
        return
    elif A[a] == B[b]:
        memo[a][b] = memo[a-1][b-1] + 1
        maxL = max(maxL, memo[a][b])

A = '.' + input()
B = '.' + input()

LA = len(A)
LB = len(B)
maxL = 0
memo = [[0] * LB for _ in range(LA)]
for i in range(LA):
    for j in range(LB):
        LCS(i, j)

print(maxL)