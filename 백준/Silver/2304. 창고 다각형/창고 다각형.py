N = int(input())
towers = []
for _ in range(N):
    L, H = map(int, input().split())
    towers.append((L, H))
towers.sort(key=lambda x: -x[1])
maxL = towers[0][1]
towers.sort()
result = 0
index = towers[0][0]
LL = towers[0][1]
for x, y in towers:
    if y == maxL:
        result += (x - index) * LL
        left = x
        break
    elif y > LL:
        result += (x - index) * LL
        LL = y
        index = x

towers.sort(reverse=True)

index = towers[0][0]
LL = 0
for x, y in towers:
    if y == maxL:
        result += (index - x) * LL
        right = x
        break
    elif y > LL:
        result += (index - x) * LL
        LL = y
        index = x

result += maxL * (right - left + 1)
print(result)