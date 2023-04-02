def solution(s):
    answer = 1
    stack = []
    for i in s:
        if len(stack) and i == stack[-1]:
            stack.pop()
        else:
            stack.append(i)
    
    if len(stack):
        answer = 0
    return answer