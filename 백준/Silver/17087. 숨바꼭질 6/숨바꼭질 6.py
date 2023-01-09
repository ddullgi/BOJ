def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

N, S = map(int, input().split())
arr = list(map(int, input().split()))
for i in range(N):
    arr[i] = abs(arr[i] - S)

result = arr[0]

for i in arr:
    result = gcd(result, i)

print(result)