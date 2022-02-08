N = int(input())
n = 1
while True:
    if N > n*(n+1)/2:
        n += 1
    else:
        break
k = int(n*(n+1)/2) - N
if n%2==0:
    x, y =n-k, 1+k
else:
    x, y =1 + k, n-k
print(f'{x}/{y}')