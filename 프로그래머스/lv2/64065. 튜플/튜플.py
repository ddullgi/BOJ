def solution(s):
    lis = s.lstrip("{")
    lis = lis.rstrip("}")
    string = "aa"
    lis2 = list(lis.split("},{"))
    lis2.sort(key=len)
    lis3 = []
    for j in lis2:
        lis3.append(list(map(int, j.split(","))))
    result = []
    for k in range(len(lis3)):
        if k == 0:
            result.append(lis3[k][0])
        else:
            result.append(list(set(lis3[k]) - set(lis3[k-1]))[0])
            
    answer = [*result]
    return answer