T = int(input())
k = T - 1
n = 0
cnt = 1
while k > 0:
    n += 6
    k = k - n
    cnt += 1

print(cnt)