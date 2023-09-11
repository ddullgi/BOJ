def check(num, c):
    global result
    dxy = ((0, 1), (1, 0), (0, -1), (-1, 0))
    y = num // 5
    x = num % 5
    if len(c) == 7:

        result += 1
        return
    for dy, dx in dxy:
        ny = y + dy
        nx = x + dx
        next_num = ny * 5 + nx
        if 0 <= ny < 5 and 0 <= nx < 5 and next_num in p and next_num not in c:
            c.append(next_num)
            check(next_num, c)

    return 0


def backtracking(cnt, idx, Y):
    global result
    y = idx // 5
    x = idx % 5

    if Y > 3 or 25 - idx < 7 - cnt:
        return

    if cnt == 7:
        c = []
        check(p[0], c)
        return

    p.append(idx)
    if arr[y][x] == "Y":
        backtracking(cnt + 1, idx + 1, Y + 1)
    else:
        backtracking(cnt + 1, idx + 1, Y)
    p.pop()
    backtracking(cnt, idx + 1, Y)


arr = [list(input()) for _ in range(5)]
result = 0
p = []

backtracking(0, 0, 0)

print(result)