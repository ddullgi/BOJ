N, M = map(int, input().split())
nums = sorted(list(map(int, input().split())))
flag = [False] * N
temp = []

def back():
    if len(temp) == M:
        print(*temp)
        return
    check = 0

    for i in range(N):
        if not flag[i] and check != nums[i]:
            flag[i] = True
            temp.append(nums[i])
            check = nums[i]
            back()
            flag[i] = False
            temp.pop()

back()