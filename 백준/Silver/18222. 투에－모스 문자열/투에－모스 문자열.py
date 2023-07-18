N = int(input()) - 1
answer = 0
while N:
    answer += N & 1
    N >>= 1
print(answer % 2)