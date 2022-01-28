def fac(n):
    result = 1
    for i in range(1,n+1):
        result *= i
    return result

t = int(input())

for i in range(1,t+1):
    n, m =map(int, input().split())
    x = int(fac(m) / (fac(n) * fac(m-n)))
    print(x)
