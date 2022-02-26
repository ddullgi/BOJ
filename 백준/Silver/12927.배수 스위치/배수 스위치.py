T = list(input())
count = 0
for i in range(len(T)):
    if T[i] == 'Y':
        for j in range(i, len(T), i+1):
            if T[j] == 'Y':
                T[j] = 'N'
            else:
                T[j] = 'Y'
        count += 1
print(count)