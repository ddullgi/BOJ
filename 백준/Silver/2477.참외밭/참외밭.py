N = int(input())

len_a = []
bb = []
for i in range(6):
    b, a = map(int, input().split())
    len_a.append(a)
    bb.append(b)
max_x = 0
max_y = 0
for j in range(1,7):
    if j%2:
        if len_a[j-1] > max_x:
            max_x = len_a[j-1]
    else:
        if len_a[j-1] > max_y:
            max_y = len_a[j-1]
square = 0
for m in range(1,len(bb)):
    if bb[m] == bb[m-1]:
        square = 1
        break

for k in range(6):
    if bb[k-1] == 3 and bb[k] == 2:
        sarea = len_a[k]*len_a[k-1]
    elif bb[k-1] == 1 and bb[k] == 3:
        sarea = len_a[k]*len_a[k-1]
    elif bb[k-1] == 4 and bb[k] == 1:
        sarea = len_a[k]*len_a[k-1]
    elif bb[k-1] == 2 and bb[k] == 4:
        sarea = len_a[k]*len_a[k-1]


area = max_x*max_y - sarea

if square == 1:
    print(max_x*max_y*N)
else:
    print(area * N)