B = 1
while B != 0:
    A, B = map(int, input().split())
    if B == 0:
        break
    print(A + B)