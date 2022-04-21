N, M = map(int, input().split())
A = set()
B = set()
for _ in range(N):
    A.add(input())
for _ in range(M):
    B.add(input())

result = sorted(list(A & B))

print(len(result))
for i in result:
    print(i)