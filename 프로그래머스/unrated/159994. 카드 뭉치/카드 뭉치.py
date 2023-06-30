def solution(cards1, cards2, goal):
    answer = 'Yes'
    c1 = 0
    c2 = 0
    l1 = len(cards1)
    l2 = len(cards2)
    
    for i in goal:
        if c1 < l1 and cards1[c1] == i:
            c1 += 1
        elif c2 < l2 and cards2[c2] == i:
            c2 += 1
        else:
            return "No"
        
    return answer