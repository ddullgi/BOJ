a = int(input())
result = 1
if a == 0:
    print(1)
else:
    for i in range(1,a+1):
        result *= i
    print(result)