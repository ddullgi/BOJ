t = int(input())
for _ in range(t) :
    j, n = map(int, input().split())

    arr = []
    for _ in range(n) :
        a, b = map(int, input().split())
        arr.append(a*b)

    arr.sort(reverse=True)
    result = 0
    for i in range(len(arr)) :
        j -= arr[i]
        result += 1
        if j <= 0 :
            break

    print(result)