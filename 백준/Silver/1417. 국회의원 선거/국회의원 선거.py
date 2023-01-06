from heapq import heappop, heappush

Q = []
M = 0
for i in range(int(input())):
    if i == 0:
        M = int(input())
        continue
    heappush(Q, -int(input()))

count = 0
while Q:
    n = heappop(Q)
    if -n < M:
        break
    else:
        heappush(Q, n + 1)
        count += 1
        M += 1


print(count)