N, K = map(int, input().split())

result = 1
for i in range(K):
    result *= N
    N -= 1

d = 1
for i in range(2, K + 1):
    d *= i

print((result // d) % 10007)