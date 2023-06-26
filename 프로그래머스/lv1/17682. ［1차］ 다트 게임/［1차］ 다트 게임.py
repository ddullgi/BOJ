def split_string(s):
    arr = []
    for i in range(len(s) - 1, -1, -1):
        if s[i] == "0" and i - 1 >= 0 and s[i - 1] == "1":
            arr.append(10)
        elif s[i] == "1" and s[i + 1] == "0":
            continue
        elif s[i].isdigit():
            arr.append(int(s[i]))
        else:
            arr.append(s[i])
    
    return(arr)

def solution(dartResult):
    stack = []
    dart_split = split_string(dartResult)
    while dart_split:
        i = dart_split.pop()

        if i == "#":
            stack[-1] = - stack[-1]
        elif i == "*":
            if len(stack) == 1:
                stack[0] *= 2 
            else:
                stack[-1] = stack[-1] * 2
                stack[-2] = stack[-2] * 2
        elif i == "D":
            stack[-1] = stack[-1] ** 2 
        elif i == "T":
            stack[-1] = stack[-1] ** 3
        elif i == "S":
            stack[-1] = stack[-1]
        else:
            stack.append(i)
            
    return sum(stack)