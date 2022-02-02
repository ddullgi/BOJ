N = int(input())

for i in range(N):
    x, y = map(str, input().split())
    for j in y:
        print(j*int(x), end='')
    print()
