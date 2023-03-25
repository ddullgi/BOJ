from heapq import heappush, heappop, nlargest, heapify

def solution(operations):
    answer = []
    
    
    for i in operations:
        if i[0] == "I":
            heappush(answer, int(i[2:]))
        else:
            if len(answer) == 0:
                continue
            elif i == "D -1":
                heappop(answer)
            elif i == "D 1":
                max_v = max(answer)
                answer.remove(max_v)
            
    if len(answer) == 0:
        answer = [0, 0]
    else:
        answer = [max(answer), min(answer)]
    
    return answer