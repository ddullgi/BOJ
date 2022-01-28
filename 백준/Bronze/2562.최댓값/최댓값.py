A = []
for i in range(1,10):
    A += [int(input())]

cnt = 0
max = A[0]
MAX = 1
for j in A:
    cnt += 1
    if j > max:
        max = j
        MAX = cnt

print(max)
print(MAX)