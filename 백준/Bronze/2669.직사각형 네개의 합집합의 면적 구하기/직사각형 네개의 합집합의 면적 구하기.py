area = [[0]*101 for _ in range(101)]
# maxX = maxY = 0
# minX = minY = 100
for _ in range(4):
    y1, x1, y2, x2 = map(int, input().split())
    # if y2 > maxY:
    #     maxY = y2
    # if x2 > maxX:
    #     maxX = x2
    # if y1 < minY:
    #     minY = y1
    # if x1 < minX:
    #     minX = x1
    for i in range(y1, y2):
        for j in range(x1, x2):
            area[i][j] = 1

result = 0
# for i in range(minY, maxY+1):
#     for j in range(minX, maxY+1):
#         result += area[i][j]
for i in range(100):
    for j in range(100):
        result += area[i][j]


print(result)