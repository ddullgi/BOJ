n, m = map(int, input().split())

s = 1
e = m
d = 0

for _ in range(int(input())):
    p = int(input())

    if p < s:
        d += (s - p)
        s = p
        e = p + m - 1

    elif p > e:
        d += (p - e)
        e = p
        s = e - m + 1

print(d)