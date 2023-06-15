def solution(s):
    answer = 0
    n1, n2 = 0, 0
    f = ""
    for i in s:
        if not f:
            f = i
        if f == i:
            n1 += 1
        else:
            n2 += 1
        
        if n1 == n2:
            n1, n2 = 0, 0
            f = ""
            answer += 1
    if n1 or n2:
        answer += 1
    return answer