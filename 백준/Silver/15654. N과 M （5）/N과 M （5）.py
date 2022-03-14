N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
num = [0] * N
stack = []

def NM(ar, lt, nn):
    if len(lt) == M:
        print(*lt)
        return
    for i in range(0, N):
        if nn[i]:
            continue
        else:
            lt.append(ar[i])
            num[i] = 1
            NM(ar, lt, nn)
            num[i] = 0
            lt.pop()

NM(arr, stack, num)