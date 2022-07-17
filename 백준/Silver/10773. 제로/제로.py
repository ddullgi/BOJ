K = int(input())
lis = []
for _ in range(K):
    N = int(input())
    if N == 0:
        lis.pop()
    else:
        lis.append(N)
print(sum(lis))