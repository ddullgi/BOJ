def check(mines, pick):
    m = 0
    for mine in mines:
        if pick == "iron" and mine == "diamond":
            m += 5
        elif pick == "stone" and mine == "diamond":
            m += 25
        elif pick == "stone" and mine == "iron":
            m += 5
        else:
            m += 1
    
    return m
            
                
def solution(picks, minerals):
    answer = 0
    total = sum(picks)
    count = 0
    arr = []
    for i in range(len(minerals) // 5 + 1):
        if total == 0:
            break
        m = 0
        l = []
        while count < len(minerals):
            l.append(minerals[count])
            if minerals[count] == "diamond":
                m += 25
            elif minerals[count] == "iron":
                m += 5
            elif minerals[count] == "stone":
                m += 1
                
            count += 1
            if count % 5 == 0:
                break
        arr.append((m, l))
        total -= 1
    arr.sort(key = lambda x: x[0], reverse = True)

    for mines in arr:
        if picks[0]:
            picks[0] -= 1
            answer += check(mines[1], "dia")
        elif picks[1]:
            picks[1] -= 1
            answer += check(mines[1], "iron")
        elif picks[2]:
            picks[2] -= 1
            answer += check(mines[1], "stone")
            
    return answer