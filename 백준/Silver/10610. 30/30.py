N = input()

total = 0
flag = False

arr = []

for i in N:
    if int(i) == 0:
        flag = True
    arr.append(i)
    total += int(i)
    
arr.sort(reverse=True)
if flag and total % 3 == 0:
    print("".join(arr))
else:
    print(-1)