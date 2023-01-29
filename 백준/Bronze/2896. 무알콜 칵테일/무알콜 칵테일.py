a, b, c = map(int, input().split())
l, j, k = map(int, input().split())
min_n = min(a / l, b / j, c / k)
print(a - l * min_n, b - j * min_n, c - k * min_n)