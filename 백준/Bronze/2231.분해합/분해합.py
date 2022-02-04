T = int(input())
N = 0
for i in range(max(T-54,1),T):
    sum = 0
    for j in range(len(str(i))):
        sum += int(str(i)[j])
    if i + sum == T:
        N = i
        print(i)
        break
if N == 0:
    print(N)