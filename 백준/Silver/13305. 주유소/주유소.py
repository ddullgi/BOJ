n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

c = b[0]
result = 0

for i in range(n - 1):
    if c > b[i]:
        c = b[i]

    result += (c * a[i])
print(result)