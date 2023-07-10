def solution(s):
    dic = {"p": 1, "P": 1, "y": -1, "Y": -1}
    b = sum([dic.get(i) or 0 for i in s])

    return False if b else True