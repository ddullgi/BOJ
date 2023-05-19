from heapq import heappop, heappush, heapify

def solution(scoville, K):
    answer = 0
    heapify(scoville)
    while scoville[0] < K:
        answer += 1
        a = heappop(scoville)
        b = heappop(scoville)
        c = a + b * 2
        heappush(scoville, c)
        if len(scoville) == 1:
            if scoville[0] < K:
                return - 1
            break
    
    
    return answer