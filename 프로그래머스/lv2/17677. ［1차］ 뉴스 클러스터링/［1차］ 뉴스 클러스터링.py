def new_set(s):
    s = s.lower()
    result = set()
    for i in range(1, len(s)):
        t = s[i - 1:i + 1]
        x = 0
        if t.isalpha():
            if t in result:
                while True:
                    if (t + str(x)) in result:
                        x += 1
                    else:
                        result.add(t + str(x))
                        break
                    
            else:
                result.add(t)
    
    return result

def jacard(set1, set2):
    if len(set1) == 0 and len(set2) == 0:
        return 65536
    
    if len(set1) == 0 or len(set2) == 0:
        return 0
    
    andset = set1 & set2
    orset = set1 | set2
    
    
    
    return len(andset) / len(orset) * 65536


def solution(str1, str2):
    
    set1 = new_set(str1)
    set2 = new_set(str2)
    
    answer = int(jacard(set1, set2))

    return answer