def solution(priorities, location):
    answer = 0
    index = -1
    
    while priorities:
        index += 1
        J = priorities.pop(0)
        
        if len(priorities) > 0:
            if max(priorities) <= J:
                answer += 1
                if index == location:
                    return answer
            else:
                priorities.append(J)
                if index == location:
                    location += len(priorities)
        else:
            answer += 1
            
    return answer