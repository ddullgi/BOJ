N = int(input())
STAR = "*"
BLANK = " "
for i in range(N):
    k = N - i - 1
    print(BLANK * k + (STAR + BLANK) * (i + 1))