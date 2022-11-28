N = input()
cnt = 0
result = 0
for i in range(len(N)):
    if N[i] == "(":
        cnt += 1
    else:
        cnt -= 1
        if N[i-1] == "(":
            result += cnt
            save = cnt
        else:
            result += 1
print(result)