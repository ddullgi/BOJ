def Rev(X):
    a = str(X)
    result = ''
    for i in a:
        result = i + result
    return int(result)

X, Y = map(int, input().split())
print(Rev(Rev(X) + Rev(Y)))