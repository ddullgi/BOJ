def solution(numbers):
    arr = [0] * 10
    answer = 0
    for i in numbers:
        arr[i] += 1
    for i in range(10):
        if arr[i] == 0:
            answer += i
    return answer