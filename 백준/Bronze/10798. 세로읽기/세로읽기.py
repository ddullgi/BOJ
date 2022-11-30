result = ""
arr = []
max_L = 0
for i in range(5):
    x = input()
    max_L = max(len(x), max_L)
    arr.append(x)

for i in range(max_L):
    for j in range(5):
        try:
            result += arr[j][i]
        except:
            continue

print(result)
