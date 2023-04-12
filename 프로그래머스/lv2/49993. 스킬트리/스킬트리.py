def solution(skill, skill_trees):
    answer = 0
    arr = []
    for i in skill_trees:
        s = ""
        for j in i:
            if j in skill:
                s += j
        arr.append(s)
        
    for n in arr:
        if skill[:len(n)] == n:
            answer += 1     
    return answer