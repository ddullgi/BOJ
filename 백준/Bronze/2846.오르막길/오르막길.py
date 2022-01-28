N = int(input())

H = list(map(int, input().split()))

min = H[0]
HILL = 0
for i in range(1,len(H)):
    if H[i] < H[i - 1]:
        if H[i - 1] - min > HILL:
            HILL = H[i - 1] - min
        min = H[i]       
    elif H[i] == H[i - 1]:
        min = H[i] 

if H[i] - min > HILL:
    HILL = H[i] - min

print(HILL)