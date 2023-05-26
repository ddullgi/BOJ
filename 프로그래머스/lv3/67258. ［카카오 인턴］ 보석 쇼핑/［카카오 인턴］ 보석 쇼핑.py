from collections import Counter

def solution(gems):
    l = len(set(gems))
    ret = []

    left = 0
    counter = Counter()
    for right in range(len(gems)):
        counter[gems[right]] += 1
        check = 0
        while len(counter) == l:
            if check == 1:
                ret.pop()
            ret.append((left + 1, right + 1))
            counter[gems[left]] -= 1
            if counter[gems[left]] == 0:
                del counter[gems[left]]
            left += 1
            check = 1
            
    ret.sort(key = lambda x: (x[1] - x[0], x[0]))
    
    return ret[0]