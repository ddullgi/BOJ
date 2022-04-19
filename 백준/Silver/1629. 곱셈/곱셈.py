A, B, C = map(int, input().split())


def xx(a, n):
    if n == 1:
        return a % C
    else:
        N = xx(a, n//2)
        if n % 2:
            return (N * N * a) % C
        else:
            return (N * N) % C

print(xx(A, B))