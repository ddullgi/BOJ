def solution(s):
    lis = s.lstrip("{")
    lis = lis.rstrip("}")
    string = "aa"
    lis2 = []
    for i in range(2, len(lis)):
        if lis[i - 2:i + 1] == "},{":
            lis2.append(string[2:])
            string=""
        else:
            string += lis[i-2]
    string += lis[-2:]
    lis2.append(string[2:])
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