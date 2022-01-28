A, B = map(int, input().split())
cnt = 0
num_list = []

N = 0
K = 0

while K < A:
    N += 1
    K = N * (N + 1) /2

k = int(K) - N

while True:
    for i in range(N):
        num_list += [N]
        cnt += 1
        if cnt == B - k:
            break
    if cnt == B - k:
        break
    N += 1

result = 0
for j in range(A - k-1, B-k):
    result += num_list[j]

print(result)