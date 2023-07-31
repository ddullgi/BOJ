N = int(input())
s, e = 0, 2 ** 32

while s <= e:
    m = (s + e) // 2
    if m ** 2 >= N:
        e = m - 1
    else:
        s = m + 1

print(s)