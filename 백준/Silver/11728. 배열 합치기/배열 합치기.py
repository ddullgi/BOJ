N, M = map(int, input().split())
A = list(map(int, input().split()))
for i in list(map(int, input().split())):
    A.append(i)
A.sort()
print(*A)