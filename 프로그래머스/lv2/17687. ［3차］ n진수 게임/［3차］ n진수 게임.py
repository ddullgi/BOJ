def next_num(num, n):
    number_string = "0123456789ABCDEF"
    l = len(num)
    num = list(num)
    new_num = ""
    while l > 0:
        if num[l - 1] == number_string[n - 1]:
            num[l - 1] = "0"
            l -= 1
            if l == 0:
                num = ["1"] + num
        else:
            num[l - 1] = number_string[int(num[l - 1], 16) + 1]
            break
    new_num = "".join(num)
    return new_num
    
def solution(n, t, m, p):
    answer = ''
    num = "0"
    s = "0"
    while len(s) <= t * m:
        num = next_num(num, n)
        s += num

    for i in range(p - 1, t * m, m):
        answer += s[i]
        
    return answer