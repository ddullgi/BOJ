while True:
    S = input()
    if S == '.':
        break
    stack = []
    result = 'yes'
    for i in S:
        if i == '(' or i == '[':
            stack.append(i)
        elif i == ')':
            if len(stack) == 0 or stack.pop() != '(':
                result = 'no'
                break
        elif i == ']':
            if len(stack) == 0 or stack.pop() != '[':
                result = 'no'
                break
    if len(stack) != 0:
        result = 'no'
    print(result)