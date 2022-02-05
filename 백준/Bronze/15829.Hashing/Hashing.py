T = int(input())
S = 0
N = str(input())
for i in range(T):
    S += (ord(N[i])-96) * 31 ** i
print(S%1234567891)