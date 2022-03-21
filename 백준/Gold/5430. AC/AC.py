from collections import deque

T = int(input())
for _ in range(T):
    process = str(input())
    N = int(input())
    string = str(input())
    if string[1:-1]:
        index = deque(map(int, string[1:-1].split(',')))
    else:
        index = deque()
    check = 1
    lr = 1
    for i in process:
        if i == 'D':
            if index:
                if lr == 1:
                    index.popleft()
                else:
                    index.pop()
            else:
                check = 0
                break
        else:
            if lr == 1:
                lr = 2
            else:
                lr = 1

    if check == 0:
        print('error')
    else:
        print('[', end='')
        if lr == 1:
            print(*list(index), sep=',', end='')
        else:
            print(*list(reversed(index)), sep=',', end='')
        print(']')