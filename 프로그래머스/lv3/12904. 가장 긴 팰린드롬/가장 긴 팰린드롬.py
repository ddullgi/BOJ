def solution(s):
    answer = 1

    l = len(s)
    arr = []
    for i in range(2, l):
        if s[i - 2:i + 1] == s[i - 2:i + 1][::-1]:
            arr.append((i - 2, i))
    
    for i in range(1, l):
        if s[i - 1:i + 1] == s[i - 1:i + 1][::-1]:
            arr.append((i - 1, i))
    
    while arr:
        start, end = arr.pop()
        if start - 1 >= 0 and end + 1 < l:
            if s[start - 1] == s[end + 1]:
                arr.append((start - 1, end + 1))
            else:
                answer = max(answer, end - start + 1)  
        else:
            answer = max(answer, end - start + 1)        
            
            
    return answer
