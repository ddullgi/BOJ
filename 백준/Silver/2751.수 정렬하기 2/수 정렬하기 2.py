import sys
T = int(sys.stdin.readline())

dic = []
for _ in range(T):
    dic.append(int(sys.stdin.readline()))

dic.sort()
for i in dic:
    sys.stdout.write(str(i) + '\n')