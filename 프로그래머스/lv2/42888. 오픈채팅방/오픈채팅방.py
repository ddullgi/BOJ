def solution(record):
    dic = {}
    lis = []
    for i in record:
        data = i.split()
        if data[0] == "Enter":
            dic[data[1]] = data[2]
            lis.append((data[0], data[1]))
        elif data[0] == "Leave":
            lis.append((data[0], data[1]))
        else:
            dic[data[1]] = data[2]
    
    result = []
    for i in lis:
        Add = ""
        if i[0] == "Leave":
            Add = "님이 나갔습니다."
        else:
            Add = "님이 들어왔습니다."
        result.append(dic[i[1]] + Add)
            
    answer = result
    
    return answer