import sys
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().split()))
M = int(input())
start, end = 0, max(arr) 

while start <= end:
    mid = (start+end) 
    total = 0 
    for i in arr:
        if i > mid:
            total += mid
        else:
            total += i
    if total <= M:
        start = mid + 1
    else: 
        end = mid - 1

print(end)