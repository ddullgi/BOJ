def solution(numbers):
    l = len(numbers)
    answer = set()
    for i in range(l):
        for j in range(i + 1, l):
            answer.add(numbers[i] + numbers[j])
            
    return sorted(list(answer))