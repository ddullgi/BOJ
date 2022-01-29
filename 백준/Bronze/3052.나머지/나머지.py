T = []
for i in range(10):
    A = int(input())
    T.append(A%42)

print(len(set(T)))