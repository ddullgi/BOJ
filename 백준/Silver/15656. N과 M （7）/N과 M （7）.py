N, M = map(int, input().split())
arr = list(map(int, input().split()))
arr.sort()
stack = []

def NM(ar, lt):
    if len(lt) == M:
        print(*lt)
        return
    for i in range(0, N):
        lt.append(ar[i])
        NM(ar, lt)
        lt.pop()

NM(arr, stack)