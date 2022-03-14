N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []

def NM(ar, lt, n):
    if len(lt) == M:
        print(*lt)
        return
    for i in range(n, N):
        if len(lt) > 0 and ar[i] < lt[-1]:
            continue
        lt.append(ar[i])
        NM(ar, lt, n)
        lt.pop()

NM(arr, stack, 0)