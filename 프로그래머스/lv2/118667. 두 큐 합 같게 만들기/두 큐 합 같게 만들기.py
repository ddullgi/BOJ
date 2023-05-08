from collections import deque

def solution(queue1, queue2):
    Q1 = deque(queue1)
    Q2 = deque(queue2)
    l = len(queue1) + len(queue2)
    Q1s =sum(queue1)
    Q2s =sum(queue2)
    
    if (Q1s + Q2s) % 2 == 1:
        return - 1
    
    count = 0
    while Q1s != Q2s:
        if count >= l:
            return -1
        
        while Q1 and Q1s > Q2s:
            tmp = Q1.popleft()
            Q2.append(tmp)
            count += 1
            Q1s -= tmp
            Q2s += tmp
            
        while Q2 and Q1s < Q2s:
            tmp = Q2.popleft()
            Q1.append(tmp)
            count += 1
            Q2s -= tmp
            Q1s += tmp
            
    return count