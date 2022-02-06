def d(n):
    t = str(n)
    a = 0
    for i in t:
        a += int(i)
    return n + a

num_list = [1]*10000
for j in range(1,10001):
    k = d(j)
    if k <= 10000:
        num_list[k-1] = 0

for m in range(10000):
    if num_list[m] == 1:
        print(m+1)