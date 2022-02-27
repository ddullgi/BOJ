import sys; input = sys.stdin.readline
area = [[0]*1001 for _ in range(1001)]
num = [0] * 101

N = int(input())
for n in range(1, N+1):
    x1, y1, x2, y2 = map(int, input().split())
    num[n] = x2 * y2
    for i in range(y1, y1+y2):
        for j in range(x1, x1+x2):
            num[area[i][j]] -= 1
            area[i][j] = n

for n in range(1, N+1):
    print(num[n])
