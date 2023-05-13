def factorial(n):
    if n < 1:
        return 1
    else:
        return n * factorial(n - 1)

def solution(n, k):
    result = []
    arr = [i for i in range(1, n + 1)]
    while(n != 0):
        case = factorial(n - 1)
        idx = k // case
        k = k % case
        if k == 0:
            result.append(arr.pop(idx - 1))
        else:
            result.append(arr.pop(idx))
        n -= 1
    return result