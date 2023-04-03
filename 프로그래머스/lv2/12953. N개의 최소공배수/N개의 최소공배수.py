def gcd(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def lcm(a, b):
    return a * b / gcd(a, b)

def solution(arr):
    answer = 0
    c = arr[0]
    for i in range(1, len(arr)):
        c = lcm(c, arr[i])
    answer = int(c)
    return answer