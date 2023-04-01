from heapq import heappop, heappush, heapify

def solution(n, works):
    answer = 0
    if sum(works)<=n:
        return 0
    for i in range(len(works)):
        works[i] = -works[i]
    heapify(works)
    for _ in range(n):
        work = heappop(works)
        work += 1
        heappush(works, work)

    return sum([w ** 2 for w in works])