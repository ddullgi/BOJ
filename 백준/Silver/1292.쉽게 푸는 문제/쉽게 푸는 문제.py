A, B = map(int, input().split())

cnt = 0
num_list = []
n = 0

while cnt < B:
    n += 1
    for i in range(n):
        num_list += [n]
        cnt += 1

result = 0
for j in range(A-1, B):
    result += num_list[j]

print(result)