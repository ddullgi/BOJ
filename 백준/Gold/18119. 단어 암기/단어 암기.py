import sys
input = sys.stdin.readline


N, M = map(int, input().split())
arr = []
for _ in range(N):
    S = input().strip()
    n = 0
    for i in S:
        n |= 1 << ord(i) - 97

    arr.append(n)

A = 0b11111111111111111111111111

for _ in range(M):
    n, s = map(str, input().split())
    idx = ord(s) - 97
    if n == "1":
        A &= ~(1 << idx)
    else:
        A |= 1 << idx

    count = 0
    for j in arr:
        if A & j == j:
            count += 1

    print(count)
