N = int(input())

l = 1
r = 2
cnt = 0

while l < r:
    temp = r ** 2 - l ** 2
    if temp == N:
        print(r)
        cnt += 1
        r += 1
    elif temp < N:
        r += 1
    elif temp > N:
        l += 1

if cnt == 0:
    print(-1)