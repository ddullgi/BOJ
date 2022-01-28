import math
A = []
for i in range(5):
    A.append(list(map(int, input().split())))
result = 0
cnt = 0
for j in A:
    sum_s = sum(j)
    cnt += 1
    if sum_s > result:
        result = sum_s
        max = cnt

print(max,result)