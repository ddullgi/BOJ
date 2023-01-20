for _ in range(int(input())):
    input()
    n = sorted(map(int, input().split()))
    print((n[-1] - n[0])*2)