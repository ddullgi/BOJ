import sys
N, K = map(int, sys.stdin.readline().split())
num_list = list(map(int, sys.stdin.readline().split()))
max_num = sum(num_list[0:K])
num = max_num
for i in range(K,N):
    num = num - num_list[i-K] + num_list[i]
    if num > max_num:
        max_num = num

print(max_num)