n = int(input())
cnt = 1
n -= 1
while True:
    if n - cnt*2 -1 < 0:
        break
    else:
        n -= (cnt*2 +1)
        cnt += 1

print(cnt)