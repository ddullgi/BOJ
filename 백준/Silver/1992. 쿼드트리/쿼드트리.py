n = int(input())
arr = [list(map(int, input())) for _ in range(n)]


def solution(x, y, n):
    check = arr[x][y]
    for i in range(x, x + n):
        for j in range(y, y + n):
            if check != arr[i][j]:
                check = -1
                break

    if check == -1:
        print("(", end='')
        n = n // 2
        solution(x, y, n) 
        solution(x, y + n, n)
        solution(x + n, y, n)
        solution(x + n, y + n, n) 
        print(")", end='')

    elif check == 1:
        print(1, end='')
    else:
        print(0, end='')


solution(0, 0, n)