def check(s):
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
            if count < 0:
                return False
    if count == 0:
        return True
    else:
        return False

def split_uv(s):
    a, b = 0, 0
    for i in range(len(s)):
        if a != 0 and a == b:
            return s[:i], s[i:]
        
        if s[i] == "(":
            a += 1
        elif s[i] == ")":
            b += 1
    
    return s, ""

def solve(s):
    answer = ""
    u, v = split_uv(s)
    if len(s) == 0:
        return ""
    
    if check(u):
        answer = u + solve(v)
    else:
        nu = ""
        for i in u[1:-1]:
            if i == "(":
                nu += ")"
            elif i == ")":
                nu += "("
        answer = "(" + solve(v) + ")" + nu
    
    return answer
    

def solution(p):
    answer = ''
    # if check(p):
    #     return p
    
    answer = solve(p)
        
            
        
    
    return answer