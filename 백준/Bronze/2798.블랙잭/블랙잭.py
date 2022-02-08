N, M = map(int, input().split())
numlist = list(map(int, input().split()))
result = 0
for i in range(N):
    for j in range(i+1,N):
        for k in range(j+1,N):
            if numlist[i] + numlist[j] + numlist[k] > M:
                continue
            else:
                result = max(result,  numlist[i] + numlist[j] + numlist[k])

print(result)