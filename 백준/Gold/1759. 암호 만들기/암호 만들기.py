def backtracking(cnt, s):
    if cnt == L:
        a, b = 0, 0
        for j in s:
            if j in "aeiou":
                a += 1
            else:
                b += 1

        if a > 0 and b > 1:
            print(s)
        else:
            return

    for i in range(C):
        if flag[i]:
            continue

        if s and ord(arr[i]) < ord(s[-1]):
            continue

        flag[i] = 1
        backtracking(cnt + 1, s + arr[i])
        flag[i] = 0


L, C = map(int, input().split())
arr = list(map(str, input().split()))
arr.sort()
flag = [0] * C

backtracking(0, "")