from collections import deque

def solution(n, m, x, y, r, c, k):
    answer = 'impossible'
    dxy = (("d", 1, 0), ("l", 0, -1), ("r", 0, 1), ("u", -1, 0))
    answers = []
    
    Q = deque()
    Q.append((y, x, ""))
    while Q:
        y, x, course = Q.popleft()
        if (x,y) == (r,c) and (k - len(course) ) % 2 == 1:
            return "impossible"
        if (x,y) == (r,c) and len(course) == k:
            return course
        for d, dx, dy in dxy:
            ny = y + dy
            nx = x + dx
            if nx <= 0 or nx > n or ny <= 0 or ny > m: continue
            if abs(nx - r) + abs(ny - c) + len(course) + 1 > k:
                continue
            Q.append((ny,nx,course + d))
            break
            
    print(answers)
    answers.sort()
    if answers:
        answer = answers[0]
    return answer