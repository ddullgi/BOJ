from itertools import combinations

def check_num(n):
    N = n ** 0.5
    c = 2
    while c <= N:
        if n % c == 0:
            return 0
        c += 1
    
    return 1

def solution(nums):
    answer = 0
    arr = []
    for i in combinations(nums, 3):
        arr.append(sum(i))


    for j in arr:
        answer += check_num(j)

    return answer