N = int(input())
T = list(map(int, input().split()))
list_num = [1]

for i in range(1,N):
    list_num.insert(i-T[i], i+1)

print(' '.join(map(str, list_num)))