import sys
from collections import deque


Q = deque()
for _ in range(int(input())):
    command = list(map(str, sys.stdin.readline().rstrip().split()))
    if command[0] == 'push':
        Q.append(int(command[1]))
    elif command[0] == 'pop':
        if Q:
            print(Q.popleft())
        else:
            print(-1)
    elif command[0] == 'size':
        print(len(Q))
    elif command[0] == 'empty':
        if Q:
            print(0)
        else:
            print(1)
    elif command[0] == 'front':
        if Q:
            print(Q[0])
        else:
            print(-1)
    elif command[0] == 'back':
        if Q:
            print(Q[-1])
        else:
            print(-1)