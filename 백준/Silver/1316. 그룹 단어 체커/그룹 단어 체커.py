T = int(input())

cnt=0
for _ in range(T):
    alpha = set()
    check = 0
    string = str(input())
    alpha.add(string[0])
    for j in range(1,len(string)):
        if string[j-1] == string[j]:
            continue
        else:
            if string[j] in alpha:
                check = 1
            else:
                alpha.add(string[j])
    if check == 0:
        cnt+=1

print(cnt)
