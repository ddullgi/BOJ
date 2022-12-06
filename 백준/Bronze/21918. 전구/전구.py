import sys

si = sys.stdin.readline
n, m = map(int, si().split())

arr = list(map(int, si().split()))


def command(c):
    global arr
    if c[0] == 1:
        arr[c[1] - 1] = c[2]
    elif c[0] == 2:
        for idx in range(c[1] - 1, c[2]):
            if arr[idx] == 0:
                arr[idx] = 1
            else:
                arr[idx] = 0
    elif c[0] == 3:
        for j in range(c[1] - 1, c[2]):
            arr[j] = 0
    elif c[0] == 4:
        for k in range(c[1] - 1, c[2]):
            arr[k] = 1


for i in range(m):
    line = list(map(int, si().split()))
    command(line)

for ans in arr:
    print(ans)