def change(a, skip, idx):
    count = 0
    n = ord(a)
    while count < idx:
        n += 1
        if n > 122:
            n = 97
        if n not in skip:
            count += 1
    return chr(n)

def solution(s, skip, index):
    answer = ''
    skip_ascii = []
    for i in skip:
        skip_ascii.append(ord(i))
    
    for j in s:
        answer += change(j, skip_ascii, index)
    return answer