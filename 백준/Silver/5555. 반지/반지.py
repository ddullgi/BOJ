string = input()
N = int(input())
A = len(string)
result = 0
for _ in range(N):
    S = list(input())
    for i in range(10):
        if ''.join(S[:A]) == string:
            result += 1
            break
        S.append(S.pop(0))
           
print(result)