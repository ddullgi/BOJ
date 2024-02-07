n, x = list(map(int, input().split()))
nums = list(map(int, input().split()))

res = sum(nums[:x])
temp = res
days = 1

for i in range(x, n):
    temp -= nums[i - x]
    temp += nums[i]
    if res < temp:
        res = temp
        days = 1
    elif res == temp:
        days += 1

if res > 0:
    print(res)
    print(days)
else:
    print("SAD")