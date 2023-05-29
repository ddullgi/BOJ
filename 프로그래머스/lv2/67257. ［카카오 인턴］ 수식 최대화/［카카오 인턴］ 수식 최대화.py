def calc(a, b, e):
    if e == "-":
        return a - b
    elif e == "+":
        return a + b
    elif e == "*":
        return a * b

def solution(expression):
    orders = (("-", "+", "*"), ("*", "+", "-"), ("-", "*", "+"), ("+", "*", "-"), ("*", "-", "+"), ("+", "-", "*"))
    oper = [i for i in expression if not i.isdigit()]
    nums = list(map(int, expression.replace("-", " ").replace("+", " ").replace("*", " ").split(" ")))
    
    answers = []
    for order in orders:
        _oper = oper
        _nums = nums
        
        for op in order:
            stack_num = [_nums[0]]
            stack_oper = []
            
            for i in range(len(_oper)):
                stack_num.append(_nums[i + 1])
                stack_oper.append(_oper[i])
                
                if stack_oper[-1] == op:
                    b = stack_num.pop()
                    a = stack_num.pop()
                    e = stack_oper.pop()
                    
                    stack_num.append(calc(a, b, e))
                    
            _nums = stack_num
            _oper = stack_oper
        
        answers.append(abs(_nums[0]))
            

    return max(answers)