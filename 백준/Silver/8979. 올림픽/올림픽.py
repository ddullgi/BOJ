a, b =  map(int, input().split())

list_medal = []
for i in range(a):
    n = 0
    list_medal_a = list(map(int, input().split()))
    list_medal.append(list_medal_a)

for j in range(len(list_medal)):
    if list_medal[j][0] == b:
        k = j 

n = 1
for j in list_medal:
    if j[0] != b:
        if j[1] > list_medal[k][1]:
            n += 1
        elif j[1] == list_medal[k][1]:
            if j[2] > list_medal[k][2]:
                n += 1
            elif j[2] == list_medal[k][2]:
                if j[3] > list_medal[k][3]:
                    n += 1

print(n)