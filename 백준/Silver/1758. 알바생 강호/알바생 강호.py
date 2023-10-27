n = int(input())
data = []
for _ in range(n):
    data.append(int(input()))

data.sort(reverse=True)
result = 0

for i in range(n):
    value = data[i] - i
    if value > 0:
        result += value

print(result)