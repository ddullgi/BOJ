def shift_alpha(s, n):
    s = ord(s)
    
    while n > 0:
        n -= 1
        if s == 122:
            s = 97
        elif s == 90:
            s = 65
        else:
            s += 1
    
    return chr(s)
    
def solution(s, n):
    answer = ''
    for i in s:
        if i.isalpha():
            answer += shift_alpha(i, n)
        else:
            answer += i
    
    return answer