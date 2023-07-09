from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    arr = []
    for order in orders:
        for n in course:
            arr += list(combinations(sorted(order), n)) 
    
    arr = ["".join(s) for s in arr]
    dic = {n: 2 for n in course}
    
    for s, i in sorted(Counter(arr).items(), key = lambda x : -x[1]):
        if dic.get(len(s)) and i >= dic[len(s)]:
            dic[len(s)] = i
            answer.append(s)
        
    return sorted(answer)