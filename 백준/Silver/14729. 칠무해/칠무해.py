import sys
input = sys.stdin.readline
N = int(input())
arr = []
cnt = 0
for _ in range(N):
    arr.append(float(input()))
    if cnt >= 7:
        arr.sort()
        arr.pop()
    else:
        cnt += 1

for i in arr[:7]:
    print("{:.3f}".format(i))