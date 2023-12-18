n = int(input())
numbers = sorted(list(map(int, input().split())))
x = int(input())

answer = 0
l, r = 0, n - 1 
while l < r:
    temp = numbers[l] + numbers[r]
    if temp == x:
        answer += 1
        l += 1
    elif temp < x:
        l += 1
    else:
        r -= 1
print(answer)