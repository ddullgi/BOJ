a = [1]*1001
a[1] = 0
for i in range(2,int(1001**0.5)+1):
    if a[i] == 1:
        for j in range(i+i, 1001, i):
            a[j] = 0

T = int(input())
b = list(map(int, input().split()))
cnt = 0 
for k in b:
    if a[k] == 1:
        cnt += 1
print(cnt)
