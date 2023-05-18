def solution(park, routes):
    news = {"N": (-1, 0), "E": (0, 1), "W": (0, -1), "S": (1, 0)}
    y, x, H, W = 0, 0, len(park), len(park[0])
    
    for i in range(H):
        check = 0
        for j in range(W):
            if park[i][j] == "S":
                y, x = i, j
                check = 1
                break
        if check == 1:
            break
    
    for route in routes:
        d, count = route.split()
        count = int(count)
        dy, dx = news[d]
        if 0 <= y + dy * count < H and 0 <= x + dx * count < W:
            ny, nx = y, x
            for _ in range(count):
                ny += dy
                nx += dx
                if park[ny][nx] == "X":
                    break
            else:
                y, x = ny, nx
    
    return [y, x]