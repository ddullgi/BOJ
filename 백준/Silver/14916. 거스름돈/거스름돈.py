N = int(input())
cnt = 0

if N < 5:
    if N % 2:
        cnt = -1
    else:
        cnt += N // 2
else:
    if N % 2:
        N -= 5
        cnt += 1
    five = N // 10
    cnt += five * 2
    N -= five * 10

    cnt += N // 2

print(cnt)
