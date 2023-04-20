def solution(bridge_length, weight, truck_weights):
    time = 0
    p = list(truck_weights) 
    x = [0] * bridge_length 
    s=0
    while (x):
        time += 1
        s -= x.pop(0) 
        if p:
            if ( s + p[0] ) <= weight:
                s += p[0] 
                x.append(p.pop(0))
            else:
                x.append(0) 
            
    return time