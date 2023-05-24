from collections import Counter

def solution(topping):
    answer = 0
    bro = Counter(topping)
    b = set()
    for i in topping:
        bro[i] -= 1
        if bro[i] == 0:
            del bro[i]
        b.add(i)
        if len(bro) == len(b):
            answer += 1
    return answer