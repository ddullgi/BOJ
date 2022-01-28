a = int(input())
for i in range(1, a+1):
    h, w, n = map(int, input().split())
    if n % h == 0:
        y = h
        x = n//h
    else:
        y = n % h
        x = n//h + 1
    ho = 100 * y + x
    print(ho)