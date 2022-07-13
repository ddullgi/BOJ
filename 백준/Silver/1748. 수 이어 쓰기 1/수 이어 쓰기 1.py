N = int(input())
result = 0
setting = [0, 9, 99, 999, 9999, 99999, 999999, 9999999, 99999999]
key = 9

for i in range(9):
    if N > setting[i]:
        continue
    if N == setting[i]:
        key = i + 1
        break
    if N <= setting[i]:
        key = i
        break

result = (N - setting[key - 1]) * (key)
for j in range(2, key+ 1):
    result += (setting[j - 1] - setting[j - 2]) * (j - 1)

print(result)