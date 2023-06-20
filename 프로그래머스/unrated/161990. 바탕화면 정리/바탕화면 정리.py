def solution(wallpaper):
    r = []
    c = []
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                r.append(i)
                c.append(j)

    return [min(r), min(c), max(r) + 1, max(c) + 1]