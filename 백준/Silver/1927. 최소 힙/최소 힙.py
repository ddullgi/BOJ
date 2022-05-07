import sys
from heapq import heappop, heappush
Q = []

for _ in range(int(sys.stdin.readline())):
    X = int(sys.stdin.readline())
    if X:
        heappush(Q, X)
    else:
        if Q:
            print(heappop(Q))
        else:
            print(0)