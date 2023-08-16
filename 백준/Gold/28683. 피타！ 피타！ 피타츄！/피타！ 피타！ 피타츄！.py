import math
N = int(input())

if int(math.sqrt(N)) - math.sqrt(N) == 0:
    print(-1)
else:
    cnt1 = 0
    for i in range(1, int(math.sqrt(N/2)) + 1):
        j = N - i**2

        if math.sqrt(j) - int(math.sqrt(j)) == 0:
            cnt1 += 1
        else:
            continue
    cnt2 = 0
    for i in range(1, int(math.sqrt(N)) + 1):
        if N % i == 0:
            if (i + (N // i)) % 2 == 0:
                if i == N // i:
                    continue
                else:
                    cnt2 += 1
        else:
            continue

    print(cnt1 + cnt2)