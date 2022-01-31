T = str(input())

alpha = ['c=', 'c-', 'd-', 'lj', 'nj', 's=', 'z=', 'dz=']
num = [0, 0, 0, 0, 0, 0, 0, 0]


for i in range(len(alpha)):
    n = -1
    while True:
        n = T.find(alpha[i], n+1)
        if n == -1:
            break
        num[i] += 1

# 'z=' 이랑 'dz=' 이 중복되는 경우 제거
num[6] = num[6] - num[7]

cnt_1 = sum(num)
cnt_2 = len(T) - sum(num[:7]) * 2 - num[7] * 3 

print(cnt_1 + cnt_2)