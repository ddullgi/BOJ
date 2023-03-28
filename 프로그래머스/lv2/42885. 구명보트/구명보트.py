from collections import deque

def solution(people, limit):
    answer = 0
    Q = deque(sorted(people))
    while Q:
        if len(Q) == 1:
            answer += 1
            break
        if Q[0] + Q[-1] <= limit:
            Q.pop()
            Q.popleft()
        else:
            Q.pop()
        answer += 1
    return answer