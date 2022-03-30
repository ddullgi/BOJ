v = [0] * 1000001
for _ in range(int(input())):
    n = int(input())
    if v[n]:
        print(v[n])
        continue
    v[1] = 1
    v[2] = 2
    v[3] = 4
    for i in range(4, n+1):
        if v[i]:
            continue
        v[i] = (v[i-1] + v[i-2] + v[i-3])%1000000009
    print(v[n])