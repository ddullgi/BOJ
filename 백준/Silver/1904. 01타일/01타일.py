a = 1
b = 2
c = 0
N = int(input())
for _ in range(3, N+1):
    c = (a + b) % 15746
    a = b
    b = c
if N == 1:
    c = 1
elif N == 2:
    c = 2
print(c)