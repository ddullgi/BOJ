import sys
input = sys.stdin.readline

def solution(cows):
    count = 0
    for i in range(len(cows)):
        for j in range(i + 1, len(cows)):
            sum_size = cows[i] + cows[j]
            if sum_size <= s:
                count += 1

    return count


n, s = map(int, input().split())
arr = [int(input()) for _ in range(n)]
print(solution(arr))