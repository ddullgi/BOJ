N, M = map(int, input().split())

arr = [0] * (N+1)
stack = []
k = 0

def NM(ar, lt):
    if len(lt) == M:
        print(*lt)
        return
    for i in range(1, N+1):
        if ar[i]:
            continue
        else:
            lt.append(i)
            ar[i] = 1
            NM(ar, lt)
            ar[i] = 0
            lt.pop()

NM(arr, stack)