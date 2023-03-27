from collections import deque
from heapq import heappush, heappop

def solution(stones, k):
    answer = 200000000
    n = len(stones)
    Q = []
    
    for i in range(k - 1):
        heappush(Q, (-stones[i], i))
    
    for i in range(k - 1, n):
        heappush(Q, (-stones[i], i))
        while Q[0][1] < i - k + 1:
            heappop(Q)
        answer = min(answer, -Q[0][0])
        
        
    return answer