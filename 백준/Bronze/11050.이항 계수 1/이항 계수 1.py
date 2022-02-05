def a(n):
    if n == 1 or n == 0:
        return 1
    else:
        return n * a(n-1)

N, K = map(int, input().split())

result = a(N) / (a(K) * a(N - K))
print(int(result))