def change(s, count, z_count):
    if s == "1":
        print([count, z_count])
        return [count, z_count]
    
    d_count = 0
    ds = ""
    
    for i in s:
        if i == "0":
            d_count += 1
        else:
            ds += i
    
    ds = str(bin(len(ds)))[2:]
    
    result = change(ds, count + 1, z_count + d_count)
    return result

def solution(s):
    answer = change(s, 0, 0)
    return answer