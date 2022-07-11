string = str(input())
L = len(string)
result = []
for i in range(1, L - 1):
    for j in range(i + 1, L):
        F = string[0:i]
        S = string[i:j]
        T = string[j:]
        result.append(F[::-1] + S[::-1] + T[::-1])
print(sorted(result)[0])