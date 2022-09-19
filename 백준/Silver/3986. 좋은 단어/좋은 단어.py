def check(string):
    stack = []
    for i in range(len(string)):
        if stack:
            if stack[-1] == string[i]:
                stack.pop()
            else:
                stack.append(string[i])
        else:
            stack.append(string[i])
    if stack:
        return 0
    else:
        return 1

result = 0
N = int(input())
for _ in range(N):
    result += check(input())

print(result)