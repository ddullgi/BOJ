import sys
input = sys.stdin.readline

def back(cnt, score):
    global result
    if cnt == 11:
        result = max(result, score)
        return

    for i in range(11):
        if order[i] == 1 or arr[cnt][i] == 0:
            continue

        order[i] = 1
        back(cnt + 1, score + arr[cnt][i])
        order[i] = 0

for _ in range(int(input())):
    arr = [list(map(int, input().split())) for _ in range(11)]

    order = [0] * 11
    result = 0

    back(0, 0)
    print(result)