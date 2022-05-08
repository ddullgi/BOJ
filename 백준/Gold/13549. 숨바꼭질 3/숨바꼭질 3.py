from heapq import heappop, heappush

N, K = map(int, input().split())


arr = [False] * 200001
D = [0xfffffff] * 200001

D[N] = 0
Q = [(0, N)]
while Q:
    W, X = heappop(Q)
    if arr[X]:
        continue

    arr[X] = True

    for w, NX in ((W + 1, X - 1), (W + 1, X + 1), (W, X * 2)):
        if 0 <= NX < 200001 and not arr[NX] and D[NX] > w:
            D[NX] = w
            heappush(Q, (w, NX))

print(D[K])