arr = int(input())
nums = list(map(int, input().split()))
t = int(input()) 

nums.append(0)
nums.sort()

answer = 0
for i in range(len(nums) - 1) :
    if nums[i] == t or nums[i+1] == t:
        answer = 0
        break
    elif nums[i] < t and t < nums[i+1]:
        answer = (t - nums[i]) * (nums[i+1] - t) - 1
        break

print(answer)