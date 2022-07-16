N = int(input())
T = tuple(map(int, input().split()))
a = 1
b = 1
ans = 1
for i in range(1, len(T)):
    if T[i - 1] > T[i]:
        a += 1
        b = 1
        if ans < a:
            ans = a
    elif T[i - 1] == T[i]:
        a += 1
        b += 1
        if ans < a:
            ans = a
        elif ans < b:
            ans = b
    else:
        a = 1
        b += 1
        if ans < b:
            ans = b

print(ans)