def check(n, times, m):
    return n > sum(m//i for i in times)

def solution(n, times):
    a, b = 0, 1
    while check(n, times, b):
        a, b = b, b*2
    while a < b:
        m = (a + b) // 2
        a, b = (m + 1, b) if check(n, times, m) else (a, m)

    return a