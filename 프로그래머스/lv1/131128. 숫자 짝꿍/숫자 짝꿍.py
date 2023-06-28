def make_hash(s):
    h = [0] * 10
    
    for n in s:
        h[int(n)] += 1
    
    return h

def solution(X, Y):
    answer = ''
    nums = list(range(9, -1, -1))
    x = make_hash(X)
    y = make_hash(Y)
    for i in nums:
        for _ in range(min(x[i], y[i])):
            answer += str(i)

    answer = answer if answer else "-1"
    
    if answer[0] == "0":
        return "0"
    
    return answer