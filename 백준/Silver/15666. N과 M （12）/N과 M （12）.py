N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
temp = []

def back(s):
    if len(temp) == M:
        print(*temp)
        return
    check = 0

    for i in range(s, N):
        if check != nums[i]:
            temp.append(nums[i])
            check = nums[i]
            back(i)
            temp.pop()
back(0)