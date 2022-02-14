T = int(input())
cnt = 1
while T >= 0:
    T -= cnt
    if T <= cnt:
        break
    cnt += 1

print(cnt)