def check(s):
    stack = []
    oc = { "}": "{", "]": "[", ")": "("}
    
    for i in s:
        if i == "]" or i == "}" or i == ")":
            if len(stack) <= 0:
                return 0
            
            if stack.pop() != oc[i]:
                return 0
        else:
            stack.append(i)
                    
    if stack:
        return 0
    
    return 1
    
def solution(s):
    answer = 0
    
    for i in range(len(s)):
        t = s[i:] + s[:i]
        answer += check(t)
    return answer