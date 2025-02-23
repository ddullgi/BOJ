def solution(data, ext, val_ext, sort_by):
    answer = []
    criteria = { 
                "code": 0,
                "date": 1,
                "maximum": 2,
                "remain":3 
               }
    
    for d in data:
        if d[criteria[ext]] < val_ext:
            answer.append(d)
            
    return sorted(answer, key = lambda x:x[criteria[sort_by]])