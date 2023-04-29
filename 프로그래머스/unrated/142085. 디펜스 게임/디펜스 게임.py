from heapq import heappush, heappop

def solution(n, k, enemy):
    Q = []
    l = len(enemy)
    answer = l
    for i in range(l):
        if len(Q) < k:
            heappush(Q, enemy[i])
        elif enemy[i] <= Q[0]:
            n -= enemy[i]
        else:
            n -= heappop(Q)
            heappush(Q, enemy[i])
        
        if n < 0:
            answer = i
            break
            
            
    
    return answer