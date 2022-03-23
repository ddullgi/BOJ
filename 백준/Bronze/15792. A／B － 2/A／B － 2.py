a, b = map(int, input().split())
result=f'{a//b}.'
k = a%b
for _ in range(1000):
    result += str((k*10)//b)
    k = (k*10)%b

print(result)