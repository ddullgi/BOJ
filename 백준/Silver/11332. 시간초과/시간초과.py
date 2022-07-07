N = int(input())
M = 10 ** 8
def check(S, N, T, L):
    result = False
    time = M * L / T
    X = 1
    if S == 'O(N)':
        X = N
    elif S == 'O(2^N)':
        X = 2 ** N
    elif S == 'O(N^2)':
        X = N ** 2
    elif S == 'O(N^3)':
        X = N ** 3
    elif S == 'O(N!)':
        while N:
            time /= N
            if time < 1:
                X = M + 1
                break
            N -= 1
    if X <= time:
        result = True
    if result == True:
        print('May Pass.')
    elif result == False:
        print('TLE!')


for _ in range(N):
    s, n, t, l = map(str, input().split())
    check(s, int(n), int(t), int(l))
