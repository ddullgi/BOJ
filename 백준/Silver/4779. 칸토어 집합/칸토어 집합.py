def soltion(n):
    if n == 1:
        return "-"
    else:
        left = soltion(n // 3)
        center = " " * (n // 3)
        return left + center + left

while True:
    try:
        N = int(input())

        rst = soltion(3 ** N)
        print(rst)
    except:
        break