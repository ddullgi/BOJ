arr = [list(map(int, input().split())) for _ in range(5)]

def xx(arr):
    bingo = 0
    cnt = 0
    for _ in range(5):
        check = list(map(int, input().split()))
        for i in check:
            for y in range(5):
                for x in range(5):
                    if arr[y][x] == i:
                        cnt += 1
                        arr[y][x] = -1
                        cy = 0
                        cx = 0
                        cc = 0
                        cc2 = 0
                        for k in range(5):
                            if arr[y][k] != -1:
                                cy += 1
                            if arr[k][x] != -1:
                                cx += 1
                            if y == x:
                                if arr[k][k] != -1:
                                    cc += 1
                            else:
                                cc = 1
                            if y + x == 4:
                                if arr[k][4 - k] != -1:
                                    cc2 += 1
                            else:
                                cc2 = 1
                        if cx == 0:
                            bingo += 1
                        if cy == 0:
                            bingo += 1
                        if cc == 0:
                            bingo += 1
                        if cc2 == 0:
                            bingo += 1
                        if bingo >= 3:
                            return cnt

print(xx(arr))