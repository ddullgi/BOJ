N, L = map(int, input().split())
arr = sorted(list(map(int, input().split())))

k = 1
d = 0
for i in range(1, N):
    d += abs(arr[i] - arr[i - 1]) 
    if L > d:
        continue
    else:
        k += 1
        d = 0
        
print(k)