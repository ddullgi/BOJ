def solution(dirs):
    answer = 0
    arr = [[0] * 11 for _ in range(11)]
    y, x = 5, 5
    visit = []
    d = {"U": (-1, 0), "D": (1, 0), "L": (0, -1), "R": (0, 1)}
    for i in dirs:
        dy, dx = d[i]
        ny = y + dy
        nx = x + dx
        if 0 <= ny < 11 and 0 <= nx < 11:
            d1 = str(y) + str(x) + str(ny) + str(nx)
            d2 = str(ny) + str(nx) + str(y) + str(x)
            y = ny
            x = nx
            if d1 not in visit:
                answer += 1
                visit.append(d1)
                visit.append(d2)
            
    return answer