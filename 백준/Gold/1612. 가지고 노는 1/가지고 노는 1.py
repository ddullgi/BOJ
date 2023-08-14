def solution():
    N = int(input())
    if N % 2 == 0 or N % 5 == 0:
        return -1

    cnt = 1
    num = 1
    while num % N:
        cnt += 1
        num = (num % N) * 10 + 1

    return cnt

print(solution())